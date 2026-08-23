/* CCA Exam Prep Console — app (self-paced course) */
const { useState, useEffect, useRef, useCallback } = React;
const CCA = window.CCA;
const TOTAL = CCA.tasks.length; // 30

/* ---------- small helpers ---------- */
function useLocal(key, init) {
  const [v, setV] = useState(() => {
    try { const s = localStorage.getItem(key); return s != null ? JSON.parse(s) : init; }
    catch { return init; }
  });
  useEffect(() => { try { localStorage.setItem(key, JSON.stringify(v)); } catch {} }, [key, v]);
  return [v, setV];
}

const Icon = {
  grid: "M3 3h7v7H3zM14 3h7v7h-7zM14 14h7v7h-7zM3 14h7v7H3z",
  layers: "M12 2 2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5",
  book: "M4 4h13a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3V4zM4 4v13a3 3 0 0 0 3 3",
  sun: "M12 17a5 5 0 1 0 0-10 5 5 0 0 0 0 10zM12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4",
  moon: "M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z",
  play: "M7 4l13 8-13 8z",
  arrow: "M5 12h14M13 6l6 6-6 6",
  check: "M20 6 9 17l-5-5",
  chevron: "M9 6l6 6-6 6",
  flag: "M4 21V4M4 4h13l-2 4 2 4H4",
  target: "M12 21a9 9 0 1 1 0-18 9 9 0 0 1 0 18M12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8",
  award: "M12 15a6 6 0 1 0 0-12 6 6 0 0 0 0 12M8.5 13.5 7 22l5-3 5 3-1.5-8.5",
  refresh: "M21 12a9 9 0 1 1-3-6.7M21 4v4h-4",
  menu: "M3 6h18M3 12h18M3 18h18",
  close: "M6 6l12 12M18 6L6 18",
  download: "M12 3v12M7 11l5 5 5-5M4 19h16",
};
function Svg({ d, size = 16, sw = 1.8, fill = "none", cls }) {
  return (
    <svg className={cls} width={size} height={size} viewBox="0 0 24 24" fill={fill}
      stroke="currentColor" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round">
      {d.split("M").filter(Boolean).map((seg, i) => <path key={i} d={"M" + seg} />)}
    </svg>
  );
}

/* ---------- Console runner ----------
   Calls the live backend (api_server.py) to run the real repo demo, and falls
   back to the simulated output in data.js when no server is reachable. */
function Console({ task, autorun }) {
  const [shown, setShown] = useState([]);
  const [running, setRunning] = useState(false);
  const [source, setSource] = useState(null); // 'live' | 'simulated' | null
  const lastLines = useRef([]);
  const timers = useRef([]);
  const clearTimers = () => { timers.current.forEach(clearTimeout); timers.current = []; };

  const stream = (lines, step) => {
    clearTimers();
    lastLines.current = lines;
    setShown([]); setRunning(true);
    lines.forEach((line, i) => {
      timers.current.push(setTimeout(() => {
        setShown((s) => [...s, line]);
        if (i === lines.length - 1) setRunning(false);
      }, 100 + i * step));
    });
  };

  const run = useCallback(async () => {
    const cfg = window.CCA_CONFIG || {};
    if (cfg.live) {
      clearTimers(); setShown([]); setRunning(true); setSource(null);
      try {
        const res = await fetch(cfg.runUrl(task.id), { cache: "no-store" });
        if (res.ok) {
          const data = await res.json();
          if (data && Array.isArray(data.lines) && data.lines.length) {
            setSource("live");
            const n = data.lines.length;
            stream(data.lines, Math.max(6, Math.min(50, Math.round(1400 / n))));
            return;
          }
        }
      } catch (e) { /* fall through to simulated */ }
    }
    setSource("simulated");
    stream(task.output, 230);
  }, [task]);

  const reset = () => { clearTimers(); setShown([]); setRunning(false); setSource(null); lastLines.current = []; };

  useEffect(() => { reset(); if (autorun) run(); /* eslint-disable-next-line */ }, [task.id]);
  useEffect(() => () => clearTimers(), []);

  const glyph = (t) => (t === "bad" ? "✗" : t === "good" ? "✓" : t === "tip" ? "★" : "");
  return (
    <div className="console">
      <div className="console-bar">
        <span className="tl r"></span><span className="tl y"></span><span className="tl g"></span>
        <span className="console-name mono">{CCA.domainById[task.d].folder}task{task.id.replace(".", "_")}.py</span>
        {source && <span className={"src-badge " + source} title={source === "live" ? "Output from running the real demo file" : "Simulated output (no backend reachable)"}>{source === "live" ? "● live" : "○ simulated"}</span>}
        <div style={{ marginLeft: "auto", display: "flex", gap: 8 }}>
          <button className="btn btn-ghost" style={{ height: 30, padding: "0 11px", fontSize: 12 }} onClick={running ? reset : run}>
            <Svg d={Icon.play} size={13} /> {running ? "Running…" : shown.length ? "Run again" : "Run demo"}
          </button>
        </div>
      </div>
      <div className="console-body">
        {shown.length === 0 && !running && (
          <div className="cl cl-dim">{"// press Run demo to execute domains/" + CCA.domainById[task.d].folder + "task" + task.id.replace(".", "_") + "_*.py"}</div>
        )}
        {shown.map((line, i) => {
          const g = glyph(line.type);
          return (
            <div key={i} className={"cl cl-" + line.type}>
              {g && <span className="cl-glyph">{g}</span>}
              <span>{line.text}</span>
            </div>
          );
        })}
        {running && <div className="cl"><span className="cursor"></span></div>}
      </div>
    </div>
  );
}

/* ---------- Inline quiz (practice: try again until correct) ---------- */
function Quiz({ q, solved = false, onSolved, onGoTask }) {
  const [wrong, setWrong] = useState([]);
  const [done, setDone] = useState(solved);
  const keys = ["A", "B", "C", "D"];
  const choose = (i) => {
    if (done || wrong.includes(i)) return;
    if (i === q.answer) { setDone(true); if (onSolved) onSolved(); }
    else setWrong((w) => [...w, i]);
  };
  return (
    <div className="qcard">
      <div className="qmeta">
        <span className="qtag">{q.id.toUpperCase()}</span>
        <span className="pill">Task {q.task}</span>
        {done && <span className="qsolved">✓ Solved</span>}
      </div>
      <p className="qp" style={{ fontSize: 14, marginBottom: 12 }}>{q.prompt}</p>
      {q.options.map((opt, i) => {
        let cls = "qopt";
        if (done && i === q.answer) cls += " correct";
        else if (wrong.includes(i)) cls += " wrong";
        return (
          <button key={i} className={cls} disabled={done || wrong.includes(i)} onClick={() => choose(i)}>
            <span className="qk">{keys[i]}</span>
            <span>{opt}</span>
            {done && i === q.answer && <Svg d={Icon.check} size={15} cls="" />}
          </button>
        );
      })}
      {!done && wrong.length > 0 && (
        <div className="qhint">Not quite — try again.{wrong.length >= 2 && " Tip: eliminate options that 'sound reasonable' but add infrastructure where a simpler fix works."}</div>
      )}
      {done && (
        <div className="explain">
          <b>Correct! </b>{q.why}
          {onGoTask && <button className="link-row" style={{ marginTop: 10 }} onClick={() => onGoTask(q.task)}>
            <span className="lid">{q.task}</span>
            <span className="ltxt">Open the demo that teaches this</span>
            <Svg d={Icon.arrow} size={14} cls="larr" />
          </button>}
        </div>
      )}
    </div>
  );
}

/* ---------- Confetti (dependency-free) ---------- */
function Confetti() {
  const colors = ["var(--accent)", "var(--good)", "var(--tip)", "var(--info)", "var(--warn)", "var(--bad)"];
  const pieces = useRef(Array.from({ length: 130 }, () => ({
    l: Math.random() * 100, delay: Math.random() * 2.5, dur: 3 + Math.random() * 2.5,
    c: colors[Math.floor(Math.random() * colors.length)], w: 6 + Math.random() * 7,
  })));
  return (
    <div className="confetti" aria-hidden="true">
      {pieces.current.map((p, i) => (
        <i key={i} style={{ left: p.l + "%", background: p.c, animationDelay: p.delay + "s",
          animationDuration: p.dur + "s", width: p.w + "px", height: (p.w * 0.55) + "px" }} />
      ))}
    </div>
  );
}

/* ---------- Start here (welcome) ---------- */
function StartHere({ name, setName, completeCount, firstIncomplete, goTask, goto }) {
  const pages = [
    { icon: Icon.grid, t: "Dashboard", d: "Your progress bar, the five exam domains with their weights, and the three themes that run through everything." },
    { icon: Icon.book, t: "Lessons (30)", d: "One page per task statement. Each is a self-contained lesson with a runnable demo and a question you must answer correctly to complete it." },
    { icon: Icon.layers, t: "Scenarios (6)", d: "The end-to-end production systems the exam is built around — each step links to the lesson that teaches it." },
    { icon: Icon.book, t: "Cheat sheet", d: "The high-yield facts to memorise, grouped by domain, each pointing to the lesson that proves it." },
    { icon: Icon.target, t: "Mock exam", d: "A 60-question exam scored 100–1000 (pass ≥ 720), just like the real exam. Retake with a fresh set anytime." },
  ];
  const anatomy = [
    ["Concept", "the idea in one or two sentences"],
    ["🔗 Analogy", "a plain-language metaphor so it clicks"],
    ["▶ Run the demo", "watch the real code execute, streamed live"],
    ["✗ Anti-pattern / ✓ Right way", "the trap vs the fix"],
    ["⚠ Common confusion", "the mistake learners actually make"],
    ["★ Exam tip", "how it shows up on the test"],
    ["Question", "answer it correctly to complete the lesson"],
  ];
  return (
    <div className="page">
      <span className="eyebrow">Welcome to the course</span>
      <h1 className="h1" style={{ marginTop: 10 }}>Claude Certified Architect — Foundations</h1>
      <p className="lede">A self-paced study course for the Foundations exam. Work through 30 short
        lessons across 5 domains — each with a runnable demo and a question — track your progress, and
        finish with a completion certificate. Everything is saved in your browser.</p>

      <div className="card namebox">
        <label htmlFor="learner-name">What should we call you?</label>
        <input id="learner-name" type="text" value={name} placeholder="Your name"
          onChange={(e) => setName(e.target.value)} maxLength={40} />
        <small>Used to greet you and on your completion certificate. Stored only in this browser — never sent anywhere.</small>
      </div>

      <div className="start-actions">
        <button className="btn btn-primary" onClick={() => goTask(firstIncomplete().id)}>
          {completeCount === 0 ? "Begin the course" : completeCount >= TOTAL ? "Review the lessons" : "Continue where you left off"}
          <Svg d={Icon.arrow} size={15} />
        </button>
        <button className="btn btn-ghost" onClick={() => goto({ view: "dashboard" })}>See the dashboard</button>
      </div>

      <div className="spacer-l"></div>
      <h2 className="section-title" style={{ marginBottom: 14 }}><span className="nav-dot" style={{ background: "var(--accent)" }}></span>What's inside</h2>
      <div className="course-map">
        {pages.map((p) => (
          <div key={p.t} className="card map-card">
            <div className="map-ic"><Svg d={p.icon} size={18} /></div>
            <div><h4>{p.t}</h4><p>{p.d}</p></div>
          </div>
        ))}
      </div>

      <div className="spacer-l"></div>
      <h2 className="section-title" style={{ marginBottom: 14 }}><span className="nav-dot" style={{ background: "var(--accent)" }}></span>How a lesson works</h2>
      <div className="card anatomy">
        {anatomy.map(([t, d], i) => (
          <div key={t} className="anat-step">
            <span className="anat-n">{i + 1}</span>
            <span className="anat-t">{t}</span>
            <span className="anat-d">{d}</span>
          </div>
        ))}
      </div>
      <TutorialDownloads />

      <p className="mono" style={{ marginTop: 18, color: "var(--text-faint)", fontSize: 12.5 }}>
        5 domains · {TOTAL} lessons · 6 scenarios · {CCA.questions.length} questions
      </p>
    </div>
  );
}

/* ---------- Progress panel (Dashboard) ---------- */
function ProgressPanel({ completeCount, goTask, firstIncomplete, goto, resetProgress }) {
  const pct = Math.round((completeCount / TOTAL) * 100);
  return (
    <div className="card progress-panel">
      <div className="row-between" style={{ marginBottom: 10 }}>
        <b>Your course progress</b>
        <span className="mono" style={{ fontSize: 13, color: "var(--accent)", fontWeight: 600 }}>{completeCount}/{TOTAL} lessons · {pct}%</span>
      </div>
      <div className="bigbar"><i style={{ width: pct + "%" }} /></div>
      <div className="start-actions" style={{ marginTop: 14 }}>
        <button className="btn btn-primary" onClick={() => goTask(firstIncomplete().id)}>
          {completeCount >= TOTAL ? "Review lessons" : completeCount === 0 ? "Start lesson 1.1" : "Continue where you left off"}
          <Svg d={Icon.arrow} size={15} />
        </button>
        {completeCount >= TOTAL && <button className="btn btn-ghost" onClick={() => goto({ view: "complete" })}><Svg d={Icon.award} size={15} /> View certificate</button>}
        <button className="btn btn-ghost" onClick={() => { if (window.confirm("Reset all lesson progress and answers? This can't be undone.")) resetProgress(); }}>
          <Svg d={Icon.refresh} size={14} /> Reset
        </button>
      </div>
    </div>
  );
}

/* ---------- Dashboard ---------- */
function Dashboard({ progress, goDomain, goTask, completeCount, firstIncomplete, goto, resetProgress }) {
  const covered = (d) => CCA.tasks.filter((t) => t.d === d.id && progress[t.id]).length;
  const total = (d) => CCA.tasks.filter((t) => t.d === d.id).length;
  return (
    <div className="page">
      <span className="eyebrow">Foundations · Study Course</span>
      <h1 className="h1" style={{ marginTop: 10 }}>Dashboard</h1>
      <p className="lede">Five domains, thirty lessons, six scenarios. Complete a lesson by answering its question correctly — your progress is tracked below.</p>

      <div className="spacer-m"></div>
      <ProgressPanel completeCount={completeCount} goTask={goTask} firstIncomplete={firstIncomplete} goto={goto} resetProgress={resetProgress} />

      <div className="spacer-l"></div>
      <div className="stat-row">
        <div className="card stat"><div className="n accent mono">5</div><div className="k">Domains</div></div>
        <div className="card stat"><div className="n mono">{TOTAL}</div><div className="k">Lessons</div></div>
        <div className="card stat"><div className="n mono">6</div><div className="k">Scenarios</div></div>
        <div className="card stat"><div className="n mono">{completeCount}<span style={{ fontSize: 16, color: "var(--text-faint)" }}>/{TOTAL}</span></div><div className="k">Completed</div></div>
      </div>

      <div className="spacer-l"></div>
      <div className="row-between" style={{ marginBottom: 14 }}>
        <h2 className="section-title"><span className="nav-dot" style={{ background: "var(--accent)" }}></span>The five domains</h2>
        <span className="mono" style={{ fontSize: 11.5, color: "var(--text-faint)" }}>click a card to open it</span>
      </div>
      <div className="grid-domains">
        {CCA.domains.map((d) => {
          const c = covered(d), tt = total(d);
          return (
            <div key={d.id} className="card dcard" onClick={() => goDomain(d.id)}>
              <div className="dcard-top">
                <div className="dcard-num">{d.n}</div>
                <div style={{ minWidth: 0 }}>
                  <h3>{d.title}</h3>
                  <p className="blurb">{d.blurb}</p>
                </div>
              </div>
              <div>
                <div className="row-between" style={{ marginBottom: 6 }}>
                  <span className="mono" style={{ fontSize: 11, color: "var(--text-faint)" }}>exam weight</span>
                  <span className="mono" style={{ fontSize: 12, fontWeight: 600, color: "var(--accent)" }}>{d.weight}%</span>
                </div>
                <div className="weightbar"><i style={{ width: d.weight + "%" }}></i></div>
              </div>
              <div className="dcard-foot">
                <span>Tasks {CCA.tasks.filter(t=>t.d===d.id)[0].id}–{CCA.tasks.filter(t=>t.d===d.id).slice(-1)[0].id}</span>
                <span className="prog-mini">
                  <span className="prog-track"><i style={{ width: (tt ? c / tt * 100 : 0) + "%" }}></i></span>
                  {c}/{tt}
                </span>
              </div>
            </div>
          );
        })}
      </div>

      <div className="spacer-l"></div>
      <h2 className="section-title" style={{ marginBottom: 14 }}><span className="nav-dot" style={{ background: "var(--accent)" }}></span>Three themes that run through everything</h2>
      <div className="themes">
        {CCA.themes.map((t, i) => (
          <div key={t.id} className="card theme">
            <div className="tnum">{String(i + 1).padStart(2, "0")}</div>
            <h4>{t.title}</h4>
            <p>{t.body}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ---------- Demo (task / lesson) view ---------- */
function DemoView({ task, progress, setCovered, goTask, solvedMap, onSolved }) {
  const domain = CCA.domainById[task.d];
  const domainTasks = CCA.tasks.filter((t) => t.d === task.d);
  const idx = domainTasks.findIndex((t) => t.id === task.id);
  const isDone = !!progress[task.id];
  const globalIdx = CCA.tasks.findIndex((t) => t.id === task.id);
  const linkedQs = (task.q || []).map((id) => CCA.questionById[id]).filter(Boolean);

  return (
    <div className="page page-wide">
      <div className="row-between" style={{ marginBottom: 18 }}>
        <div>
          <span className="eyebrow">{domain.title} · Lesson {globalIdx + 1} of {TOTAL}</span>
          <h1 className="h1" style={{ marginTop: 8 }}>{task.title}</h1>
        </div>
        <button className={"btn " + (isDone ? "btn-primary" : "btn-ghost")} onClick={() => setCovered(task.id, !isDone)}>
          <Svg d={Icon.check} size={15} /> {isDone ? "Completed" : "Mark complete"}
        </button>
      </div>

      <div className="demo-layout">
        <div className="demo-main">
          <div className="card concept">
            <span className="eyebrow" style={{ marginBottom: 8, display: "block" }}>Concept</span>
            <p>{task.concept}</p>
          </div>

          {task.analogy && (
            <div className="card analogy-card">
              <span className="eyebrow" style={{ marginBottom: 8, display: "block" }}>🔗 Analogy</span>
              <p>{task.analogy}</p>
            </div>
          )}

          <Console task={task} />

          <div className="compare">
            <div className="cmp bad">
              <div className="lbl"><span>✗</span> Anti-pattern</div>
              <p>{task.antipattern}</p>
            </div>
            <div className="cmp good">
              <div className="lbl"><span>✓</span> The right way</div>
              <p>{task.right}</p>
            </div>
          </div>

          {task.pitfall && (
            <div className="cmp warn">
              <div className="lbl"><span>⚠</span> Common confusion</div>
              <p>{task.pitfall}</p>
            </div>
          )}

          <div className="tipbar">
            <span className="star">★</span>
            <p><b>Exam tip</b>{task.tip}</p>
          </div>

          <div className="row-between" style={{ marginTop: 6 }}>
            <button className="btn btn-ghost" disabled={globalIdx === 0} style={{ opacity: globalIdx === 0 ? 0.4 : 1 }}
              onClick={() => globalIdx > 0 && goTask(CCA.tasks[globalIdx - 1].id)}>
              <span style={{ display: "inline-flex", transform: "scaleX(-1)" }}><Svg d={Icon.arrow} size={14} /></span> Previous
            </button>
            <span className="mono" style={{ fontSize: 12, color: "var(--text-faint)" }}>{idx + 1} / {domainTasks.length} in Domain {domain.n}</span>
            <button className="btn btn-ghost" disabled={globalIdx === TOTAL - 1} style={{ opacity: globalIdx === TOTAL - 1 ? 0.4 : 1 }}
              onClick={() => globalIdx < TOTAL - 1 && goTask(CCA.tasks[globalIdx + 1].id)}>
              Next <Svg d={Icon.arrow} size={14} />
            </button>
          </div>
        </div>

        <div className="demo-side">
          {linkedQs.length > 0 && (
            <div className="card side-card">
              <h5>Complete this lesson</h5>
              <p className="side-hint">Answer correctly to mark the lesson complete — keep trying until you get it.</p>
              {linkedQs.map((q) => (
                <Quiz key={q.id + (solvedMap[task.id] ? "-s" : "")} q={q}
                  solved={!!solvedMap[task.id]} onSolved={() => onSolved(task.id)} onGoTask={goTask} />
              ))}
            </div>
          )}
          {task.links && task.links.length > 0 && (
            <div className="card side-card">
              <h5>Related concepts</h5>
              {task.links.map((id) => {
                const t = CCA.taskById[id];
                if (!t) return null;
                return (
                  <button key={id} className="link-row" onClick={() => goTask(id)}>
                    <span className="lid">{id}</span>
                    <span className="ltxt">{t.title}</span>
                    <Svg d={Icon.arrow} size={14} cls="larr" />
                  </button>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

/* ---------- Scenarios ---------- */
function Scenarios({ goTask }) {
  return (
    <div className="page">
      <span className="eyebrow">End-to-end</span>
      <h1 className="h1" style={{ marginTop: 10 }}>Six runnable scenarios</h1>
      <p className="lede">Fuller systems that compose the lesson concepts — a real support agent, a multi-agent research pipeline, an extraction pipeline, and more. Each step links to the lesson that teaches it.</p>
      <div className="spacer-l"></div>
      {CCA.scenarios.map((s) => (
        <div key={s.id} className="card scn">
          <div className="scn-head">
            <div className="scn-n">{s.n}</div>
            <div>
              <h3>{s.title}</h3>
              <p>{s.summary}</p>
              <div className="scn-dtags">
                {s.domains.map((d) => <span key={d} className="pill">D{CCA.domainById[d].n} · {CCA.domainById[d].short}</span>)}
              </div>
            </div>
          </div>
          <div className="steps">
            {s.steps.map((st, i) => (
              <div key={i} className="step">
                <div className="sdot">{i + 1}</div>
                <div className="stxt"><b>{st.t}</b><span>{st.d}</span></div>
                <button className="slink" onClick={() => goTask(st.task)}>lesson {st.task} →</button>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

/* ---------- Cheat sheet ---------- */
function CheatSheet({ goTask }) {
  return (
    <div className="page">
      <span className="eyebrow">High-yield</span>
      <h1 className="h1" style={{ marginTop: 10 }}>Cheat sheet</h1>
      <p className="lede">The facts to memorise, grouped by domain. Every line points to the lesson that proves it — jump there to study it live.</p>
      <div className="spacer-l"></div>
      {CCA.domains.map((d) => {
        const items = CCA.cheat.filter((c) => c.d === d.id);
        if (!items.length) return null;
        return (
          <div key={d.id} className="cheat-group">
            <h3>
              <span className="dcard-num" style={{ width: 26, height: 26, fontSize: 12, borderRadius: 7 }}>{d.n}</span>
              {d.title}
              <span className="cg-w">{d.weight}%</span>
            </h3>
            <div className="cheat-list">
              {items.map((c, i) => (
                <div key={i} className="card cheat-item">
                  <span className="ci-mark">→</span>
                  <span className="ci-fact">{c.fact}</span>
                  <button className="ci-link" onClick={() => goTask(c.task)}>lesson {c.task}</button>
                </div>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}

/* ---------- Mock exam ---------- */
function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}
const EXAM_WEIGHTS = { d1: 27, d2: 18, d3: 20, d4: 20, d5: 15 };
/* Draw n questions in proportion to the real exam's domain weights. */
function pickWeighted(pool, n) {
  const byDom = {};
  pool.forEach((q) => { (byDom[q.domain] = byDom[q.domain] || []).push(q); });
  Object.keys(byDom).forEach((k) => { byDom[k] = shuffle(byDom[k]); });
  const picks = [], chosen = new Set();
  Object.keys(EXAM_WEIGHTS).forEach((d) => {
    const want = Math.min((byDom[d] || []).length, Math.round((n * EXAM_WEIGHTS[d]) / 100));
    (byDom[d] || []).slice(0, want).forEach((q) => { picks.push(q); chosen.add(q.id); });
  });
  if (picks.length < n) {
    shuffle(pool.filter((q) => !chosen.has(q.id))).slice(0, n - picks.length).forEach((q) => picks.push(q));
  }
  return shuffle(picks.slice(0, n));
}
function fmtTime(s) {
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), r = s % 60;
  const mm = String(m).padStart(2, "0"), ss = String(r).padStart(2, "0");
  return h > 0 ? `${h}:${mm}:${ss}` : `${m}:${ss}`;
}
const SEC_PER_Q = 120;   // 2 min/question — the full 60-question exam = 120 min, like the real exam

function MockExam({ goTask }) {
  const bank = (CCA.mock && CCA.mock.length) ? CCA.mock : CCA.questions;
  const maxN = bank.length;
  const lengths = [60, 20, 10].filter((n) => n <= maxN);
  if (!lengths.includes(maxN) && maxN < 60) lengths.unshift(maxN);
  const [phase, setPhase] = useState("setup");   // setup | run | done
  const [mode, setMode] = useState("exam");       // exam | practice
  const [length, setLength] = useState(lengths[0]);
  const [exam, setExam] = useState([]);
  const [answers, setAnswers] = useState({});
  const [timeLeft, setTimeLeft] = useState(0);
  const [onlyWrong, setOnlyWrong] = useState(false);
  const keys = ["A", "B", "C", "D"];

  const begin = (len, m) => {
    setExam(pickWeighted(bank, len)); setAnswers({}); setLength(len); setMode(m);
    setTimeLeft(len * SEC_PER_Q); setOnlyWrong(false); setPhase("run");
    if (window.scrollTo) window.scrollTo(0, 0);
  };
  const finish = () => { setPhase("done"); if (window.scrollTo) window.scrollTo(0, 0); };
  const reset = () => { setPhase("setup"); setExam([]); setAnswers({}); };

  // one overall countdown (exam mode only); auto-submits when it reaches zero
  useEffect(() => {
    if (phase !== "run" || mode !== "exam") return;
    if (timeLeft <= 0) { setPhase("done"); if (window.scrollTo) window.scrollTo(0, 0); return; }
    const t = setTimeout(() => setTimeLeft((s) => s - 1), 1000);
    return () => clearTimeout(t);
  }, [phase, mode, timeLeft]);

  const answered = exam.filter((q) => answers[q.id] != null).length;
  const correctCount = exam.filter((q) => answers[q.id] === q.answer).length;
  const scaled = Math.round(100 + (correctCount / (exam.length || 1)) * 900);
  const pass = scaled >= 720;

  // ---------- Setup ----------
  if (phase === "setup") {
    return (
      <div className="page">
        <span className="eyebrow">Mock exam</span>
        <h1 className="h1" style={{ marginTop: 10 }}>Mock exam</h1>
        <p className="lede">A verified, blueprint-aligned question bank covering all 30 task statements. The full exam is
          60 questions, scored 100–1000 — passing is ≥ 720, like the real exam. Questions are drawn in
          proportion to the official domain weights.</p>
        <div className="setup-card">
          <div className="setup-row">
            <div className="setup-label">Length</div>
            <div className="chip-row">
              {lengths.map((n) => (
                <button key={n} className={"chip" + (length === n ? " on" : "")} onClick={() => setLength(n)}>
                  {n === 60 ? "Full · 60" : n + " questions"}
                </button>
              ))}
            </div>
          </div>
          <div className="setup-row">
            <div className="setup-label">Mode</div>
            <div className="chip-row">
              <button className={"chip" + (mode === "exam" ? " on" : "")} onClick={() => setMode("exam")}>
                Exam · reveal at end
              </button>
              <button className={"chip" + (mode === "practice" ? " on" : "")} onClick={() => setMode("practice")}>
                Practice · instant feedback
              </button>
            </div>
          </div>
          <div className="setup-foot">
            <span className="mono setup-hint">
              {mode === "exam" ? `⏱ ${fmtTime(length * SEC_PER_Q)} timer · no feedback until you submit` : "Untimed · each answer is graded as you go"}
            </span>
            <button className="btn btn-primary" onClick={() => begin(length, mode)}>
              <Svg d={Icon.target} size={15} /> Start exam
            </button>
          </div>
        </div>
      </div>
    );
  }

  const done = phase === "done";
  // per-domain breakdown for the results screen
  const domStats = Object.keys(EXAM_WEIGHTS).map((d) => {
    const qs = exam.filter((q) => q.domain === d);
    const ok = qs.filter((q) => answers[q.id] === q.answer).length;
    return { d, total: qs.length, ok, pct: qs.length ? Math.round((ok / qs.length) * 100) : 0 };
  }).filter((s) => s.total > 0);

  const shown = done && onlyWrong ? exam.filter((q) => answers[q.id] !== q.answer) : exam;

  return (
    <div className="page">
      <span className="eyebrow">Mock exam · {mode === "exam" ? "exam mode" : "practice"}</span>
      <h1 className="h1" style={{ marginTop: 10 }}>{done ? "Your results" : `${exam.length}-question exam`}</h1>

      {/* sticky status bar */}
      <div className="exam-bar">
        <span className="mono">{answered}/{exam.length} answered</span>
        <span className="minibar" style={{ flex: 1 }}><i style={{ width: (answered / exam.length * 100) + "%" }} /></span>
        {!done && mode === "exam" && (
          <span className={"exam-timer mono" + (timeLeft <= 300 ? " low" : "")}>⏱ {fmtTime(timeLeft)}</span>
        )}
        {!done && <button className="btn btn-primary" style={{ height: 30 }} onClick={finish}>Submit</button>}
        <button className="btn btn-ghost" style={{ height: 30 }} onClick={reset}><Svg d={Icon.refresh} size={14} /> New exam</button>
      </div>

      {done && (
        <>
          <div className={"exam-result " + (pass ? "pass" : "fail")}>
            <div className="score mono">{scaled}<span>/1000</span></div>
            <div className="score-txt">
              <b>{pass ? "Pass 🎉" : "Below passing"}</b>
              <span>{correctCount} / {exam.length} correct · passing is 720</span>
            </div>
            <button className="btn btn-primary" onClick={() => begin(length, mode)}><Svg d={Icon.refresh} size={15} /> Retake (new questions)</button>
          </div>
          <div className="dombreak">
            <div className="dombreak-h mono">Score by domain</div>
            {domStats.map((s) => (
              <div key={s.d} className="dombar-row" onClick={() => goDomainFromMock(goTask, s.d)} title="Open this domain">
                <span className="dombar-name">{CCA.domainById[s.d].short}</span>
                <span className="dombar-track"><i className={s.pct >= 72 ? "ok" : "low"} style={{ width: s.pct + "%" }} /></span>
                <span className="dombar-num mono">{s.ok}/{s.total}</span>
              </div>
            ))}
          </div>
          <div className="exam-bar" style={{ marginTop: 4 }}>
            <button className={"chip" + (onlyWrong ? " on" : "")} onClick={() => setOnlyWrong((v) => !v)}>
              {onlyWrong ? "Showing incorrect only" : "Review incorrect only"}
            </button>
            <span className="mono setup-hint">Reference links below each question open the matching lesson.</span>
          </div>
        </>
      )}

      <div className="spacer-m"></div>
      {shown.map((q, qi) => {
        const chosen = answers[q.id];
        const revealed = mode === "practice" ? chosen != null : done;
        const num = exam.indexOf(q) + 1;
        return (
          <div key={q.id} className="card exam-q">
            <div className="qmeta">
              <span className="qtag">{num}</span>
              <span className="pill">Task {q.task}</span>
              {revealed && <span className={chosen === q.answer ? "qsolved" : "qsolved bad"}>{chosen === q.answer ? "✓ correct" : (chosen == null ? "✗ unanswered" : "✗ incorrect")}</span>}
            </div>
            <p className="qp">{q.prompt}</p>
            {q.options.map((opt, i) => {
              let cls = "qopt";
              if (revealed) { if (i === q.answer) cls += " correct"; else if (i === chosen) cls += " wrong"; }
              else if (i === chosen) cls += " chosen";
              return (
                <button key={i} className={cls} disabled={revealed} onClick={() => setAnswers((a) => ({ ...a, [q.id]: i }))}>
                  <span className="qk">{keys[i]}</span><span>{opt}</span>
                  {revealed && i === q.answer && <Svg d={Icon.check} size={15} />}
                </button>
              );
            })}
            {revealed && (
              <div className="explain">
                <b>{chosen === q.answer ? "Correct. " : "Incorrect. "}</b>{q.why}
                {q.ref && <div className="qref">📖 {q.ref}</div>}
                <button className="link-row" style={{ marginTop: 10 }} onClick={() => goTask(q.task)}>
                  <span className="lid">{q.task}</span><span className="ltxt">Open the lesson to review</span><Svg d={Icon.arrow} size={14} cls="larr" />
                </button>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
function goDomainFromMock(goTask, d) {
  const first = CCA.tasks.find((t) => t.d === d);
  if (first) goTask(first.id);
}

/* ---------- Course complete (congratulations + certificate) ---------- */
function Complete({ name, goto, resetProgress }) {
  const today = new Date().toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" });
  return (
    <div className="page complete-page">
      <Confetti />
      <div className="complete-inner">
        <div className="cert">
          <div className="cert-ribbon">Certificate of Completion</div>
          <div className="cert-badge"><Svg d={Icon.award} size={40} /></div>
          <p className="cert-pre">This certifies that</p>
          <h1 className="cert-name">{name && name.trim() ? name.trim() : "You"}</h1>
          <p className="cert-body">has completed all {TOTAL} lessons of the<br /><b>Claude Certified Architect — Foundations Study Course</b></p>
          <div className="cert-stats">{CCA.domains.length} domains · {CCA.scenarios.length} scenarios · {TOTAL}/{TOTAL} lessons · {(CCA.mock && CCA.mock.length) || 60} questions solved</div>
          <div className="cert-foot"><span>Self-paced study course</span><span>{today}</span></div>
        </div>

        <h2 className="congrats">🎉 Congratulations{name && name.trim() ? `, ${name.trim()}` : ""}!</h2>
        <p className="congrats-sub">You've worked through every domain, run every demo, and answered every question correctly.
          You're ready to put these patterns to work — and to sit the exam with confidence.</p>

        <div className="start-actions" style={{ justifyContent: "center" }}>
          <button className="btn btn-primary" onClick={() => goto({ view: "mock" })}><Svg d={Icon.target} size={15} /> Try the mock exam</button>
          <button className="btn btn-ghost" onClick={() => window.print()}>Print / save certificate</button>
          <button className="btn btn-ghost" onClick={() => goto({ view: "dashboard" })}>Back to dashboard</button>
          <button className="btn btn-ghost" onClick={() => { if (window.confirm("Reset all progress and start over?")) { resetProgress(); goto({ view: "start" }); } }}>
            <Svg d={Icon.refresh} size={14} /> Start over
          </button>
        </div>
      </div>
    </div>
  );
}

/* ---------- Tutorial downloads ----------
   Rendered from the course's own config (window.CCA_CONFIG.tutorials), so a new
   handbook is a config + file drop — no app code changes. Renders nothing when
   the course has no PDFs yet. */
function tutorialList() {
  const cfg = window.CCA_CONFIG || {};
  return Array.isArray(cfg.tutorials) ? cfg.tutorials : [];
}
function TutorialDownloads() {
  const items = tutorialList();
  if (!items.length) return null;
  return (
    <>
      <div className="spacer-l"></div>
      <h2 className="section-title" style={{ marginBottom: 14 }}><span className="nav-dot" style={{ background: "var(--accent)" }}></span>Download the tutorial</h2>
      <div className="course-map">
        {items.map((t) => (
          <a key={t.file} className="card dl-card" href={t.file} download target="_blank" rel="noopener">
            <div className="map-ic"><Svg d={Icon.download} size={18} /></div>
            <div className="dl-body">
              <h4>{t.title}</h4>
              <p>{t.blurb}</p>
              <span className="dl-meta mono">{t.meta}</span>
            </div>
          </a>
        ))}
      </div>
    </>
  );
}

/* ---------- Sidebar ---------- */
function Sidebar({ route, goto, goTask, progress, completeCount, drawerOpen, onClose }) {
  const [open, setOpen] = useState(() => ({ [route.taskId ? CCA.taskById[route.taskId]?.d : "d1"]: true }));
  const toggle = (id) => setOpen((o) => ({ ...o, [id]: !o[id] }));
  const top = [
    { v: "start", label: "Start here", icon: Icon.flag, key: "0" },
    { v: "dashboard", label: "Dashboard", icon: Icon.grid, key: "1" },
    { v: "scenarios", label: "Scenarios", icon: Icon.layers, key: "2" },
    { v: "cheat", label: "Cheat sheet", icon: Icon.book, key: "3" },
    { v: "mock", label: "Mock exam", icon: Icon.target, key: "4" },
  ];
  const pct = Math.round((completeCount / TOTAL) * 100);
  return (
    <aside className={"sidebar" + (drawerOpen ? " open" : "")}>
      <div className="sb-head">
        <div className="brand">
          <div className="brand-mark">CC</div>
          <div className="brand-txt"><b>Architect Course</b><span>foundations · self-paced</span></div>
        </div>
        <button className="sb-close" onClick={onClose} aria-label="Close menu"><Svg d={Icon.close} size={18} /></button>
      </div>
      <nav className="sb-nav">
        <div className="nav-group">
          {top.map((t) => (
            <button key={t.v} className={"nav-item" + (route.view === t.v ? " active" : "")} onClick={() => goto({ view: t.v })}>
              <Svg d={t.icon} size={16} /> {t.label}
              <span className="nav-key">{t.key}</span>
            </button>
          ))}
        </div>
        <div className="nav-group">
          <div className="nav-label">Lessons · {completeCount}/{TOTAL} done</div>
          <div className="sb-progress"><i style={{ width: pct + "%" }} /></div>
          <div className="dnav">
            {CCA.domains.map((d) => {
              const tasks = CCA.tasks.filter((t) => t.d === d.id);
              const isOpen = open[d.id];
              return (
                <div key={d.id}>
                  <button className={"dnav-row" + (route.view === "demo" && CCA.taskById[route.taskId]?.d === d.id ? " active" : "")} onClick={() => toggle(d.id)}>
                    <span className="dnum">{d.n}</span>
                    <span style={{ flex: 1, minWidth: 0, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{d.short}</span>
                    <Svg d={Icon.chevron} size={14} cls="" />
                    <span style={{ display: "none" }}>{isOpen}</span>
                  </button>
                  {isOpen && (
                    <div style={{ padding: "2px 0 6px 8px" }}>
                      {tasks.map((t) => (
                        <button key={t.id} className={"nav-item" + (route.taskId === t.id ? " active" : "")}
                          style={{ padding: "6px 10px", fontSize: 12.5 }} onClick={() => goTask(t.id)}>
                          {progress[t.id]
                            ? <Svg d={Icon.check} size={13} cls="nav-check" />
                            : <span className="nav-dot"></span>}
                          <span className="mono" style={{ fontSize: 11.5, color: "var(--text-faint)", width: 24 }}>{t.id}</span>
                          <span style={{ flex: 1, minWidth: 0, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{t.title}</span>
                        </button>
                      ))}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
        {tutorialList().length > 0 && (
          <div className="nav-group">
            <div className="nav-label">Downloads</div>
            {tutorialList().map((t) => (
              <a key={t.file} className="nav-item" href={t.file} download target="_blank" rel="noopener">
                <Svg d={Icon.download} size={16} /> {t.title}
              </a>
            ))}
          </div>
        )}
      </nav>
      <div className="sb-foot">
        <div className="mono" style={{ fontSize: 11, color: "var(--text-faint)", lineHeight: 1.6 }}>
          python3 run_all.py ui<br />→ 127.0.0.1:8000
        </div>
      </div>
    </aside>
  );
}

/* ---------- App ---------- */
function App() {
  const [theme, setTheme] = useLocal("cca-theme", "light");
  const [route, setRoute] = useLocal("cca-route", { view: "start", taskId: null });
  const [progress, setProgress] = useLocal("cca-progress", {});
  const [solvedMap, setSolvedMap] = useLocal("cca-solved", {});
  const [name, setName] = useLocal("cca-name", "");
  const [navOpen, setNavOpen] = useState(false);
  const scrollRef = useRef(null);

  const completeCount = CCA.tasks.filter((t) => progress[t.id]).length;

  useEffect(() => { document.documentElement.setAttribute("data-theme", theme); }, [theme]);
  useEffect(() => { if (scrollRef.current) scrollRef.current.scrollTop = 0; }, [route]);
  useEffect(() => { setNavOpen(false); }, [route]);   // close the mobile drawer on navigation

  const goto = (r) => setRoute({ taskId: null, ...r });
  const goTask = (id) => setRoute({ view: "demo", taskId: id });
  const goDomain = (id) => goTask(CCA.tasks.filter((t) => t.d === id)[0].id);
  const setCovered = (id, val) => setProgress((p) => ({ ...p, [id]: val }));
  const onSolved = (id) => { setSolvedMap((s) => ({ ...s, [id]: true })); setProgress((p) => ({ ...p, [id]: true })); };
  const resetProgress = () => { setProgress({}); setSolvedMap({}); };
  const firstIncomplete = () => CCA.tasks.find((t) => !progress[t.id]) || CCA.tasks[0];

  // celebrate when the learner transitions to all-complete
  const prevComplete = useRef(completeCount);
  useEffect(() => {
    if (prevComplete.current < TOTAL && completeCount === TOTAL) goto({ view: "complete" });
    prevComplete.current = completeCount;
  }, [completeCount]);

  // keyboard nav
  useEffect(() => {
    const onKey = (e) => {
      if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
      if (e.key === "0") goto({ view: "start" });
      else if (e.key === "1") goto({ view: "dashboard" });
      else if (e.key === "2") goto({ view: "scenarios" });
      else if (e.key === "3") goto({ view: "cheat" });
      else if (e.key === "4") goto({ view: "mock" });
      else if (e.key.toLowerCase() === "t") setTheme((t) => (t === "light" ? "dark" : "light"));
      else if ((e.key === "ArrowRight" || e.key === "ArrowLeft") && route.view === "demo") {
        const i = CCA.tasks.findIndex((x) => x.id === route.taskId);
        const ni = e.key === "ArrowRight" ? Math.min(i + 1, CCA.tasks.length - 1) : Math.max(i - 1, 0);
        goTask(CCA.tasks[ni].id);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [route]);

  const task = route.taskId ? CCA.taskById[route.taskId] : null;
  const labels = { start: "Start here", dashboard: "Dashboard", scenarios: "Scenarios", cheat: "Cheat sheet", mock: "Mock exam", complete: "Course complete" };
  const crumbLabel = route.view === "demo" && task
    ? <><b>{CCA.domainById[task.d].short}</b><span className="crumb-sep">/</span><span>Task {task.id}</span></>
    : <b>{labels[route.view] || "Dashboard"}</b>;
  const pct = Math.round((completeCount / TOTAL) * 100);

  return (
    <div className="shell">
      <Sidebar route={route} goto={goto} goTask={goTask} progress={progress} completeCount={completeCount} drawerOpen={navOpen} onClose={() => setNavOpen(false)} />
      {navOpen && <div className="nav-backdrop" onClick={() => setNavOpen(false)} />}
      <div className="main">
        <div className="topbar">
          <button className="hamburger" onClick={() => setNavOpen(true)} aria-label="Open menu"><Svg d={Icon.menu} size={18} /></button>
          <div className="crumbs">
            <span style={{ color: "var(--text-faint)" }}>course</span>
            <span className="crumb-sep">/</span>
            {crumbLabel}
          </div>
          <div className="topbar-spacer"></div>
          <div className="tb-progress" title={completeCount + " of " + TOTAL + " lessons complete"}>
            <span className="minibar"><i style={{ width: pct + "%" }} /></span>
            <span className="mono" style={{ fontSize: 11.5, color: "var(--text-faint)" }}>{completeCount}/{TOTAL}</span>
          </div>
          {name && name.trim() && <span className="greet">Hi, {name.trim().split(" ")[0]}</span>}
          <a className="tb-btn" href="../" title="Back to the Certification Hub">
            <Svg d={Icon.grid} size={15} cls="tb-icon" />
            Hub
          </a>
          <button className="tb-btn" onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
            <Svg d={theme === "light" ? Icon.moon : Icon.sun} size={15} cls="tb-icon" />
            {theme === "light" ? "Dark" : "Light"}
          </button>
        </div>
        <div className="scroll app-bg" ref={scrollRef}>
          {route.view === "start" && <StartHere name={name} setName={setName} completeCount={completeCount} firstIncomplete={firstIncomplete} goTask={goTask} goto={goto} />}
          {route.view === "dashboard" && <Dashboard progress={progress} goDomain={goDomain} goTask={goTask} completeCount={completeCount} firstIncomplete={firstIncomplete} goto={goto} resetProgress={resetProgress} />}
          {route.view === "demo" && task && <DemoView task={task} progress={progress} setCovered={setCovered} goTask={goTask} solvedMap={solvedMap} onSolved={onSolved} />}
          {route.view === "scenarios" && <Scenarios goTask={goTask} />}
          {route.view === "cheat" && <CheatSheet goTask={goTask} />}
          {route.view === "mock" && <MockExam goTask={goTask} />}
          {route.view === "complete" && <Complete name={name} goto={goto} resetProgress={resetProgress} />}
          <footer className="app-foot">
            <p className="foot-verse">
              “Whatever you do, work at it with all your heart, as working for the Lord.”
              <span className="foot-verse-ref">— Colossians 3:23</span>
            </p>
            <p className="foot-built">Built by <b>Jacinth Paul</b> — to help aspirants on their Claude Certification journey.</p>
            <p className="foot-disclaimer">
              This is an independent, community-made study aid — <b>not an official Anthropic
              product</b> and not affiliated with or endorsed by Anthropic. It’s supporting
              material to help you prepare for the Claude certification exams.
              Always refer to Anthropic’s official Exam Guides as the authoritative source.
            </p>
          </footer>
        </div>
      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
