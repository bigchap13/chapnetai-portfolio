from flask import Flask
from pathlib import Path
import json

app = Flask(__name__)

PROJECT_HISTORY = Path.home() / "chapnetai-project-history"
REGISTRY_JSON = PROJECT_HISTORY / "registry" / "milestones" / "milestone_registry.json"

def registry_stats():
    folders = PROJECT_HISTORY / "milestones"
    milestone_folders = len([p for p in folders.iterdir() if p.is_dir()]) if folders.exists() else 0
    milestone_docs = len(list(folders.rglob("MILESTONE.md"))) if folders.exists() else 0

    projects = {}
    if REGISTRY_JSON.exists():
        try:
            data = json.loads(REGISTRY_JSON.read_text())
            for item in data:
                project = item.get("project", "General")
                projects[project] = projects.get(project, 0) + 1
        except Exception:
            pass

    return milestone_folders, milestone_docs, projects

@app.route("/")
def home():
    milestone_folders, milestone_docs, projects = registry_stats()

    project_rows = ""
    for name, count in sorted(projects.items(), key=lambda x: x[1], reverse=True)[:10]:
        project_rows += f"""
        <div class="metric-card">
            <strong>{count}</strong>
            <span>{name}</span>
        </div>
        """

    if not project_rows:
        project_rows = """
        <div class="metric-card"><strong>Live</strong><span>Registry Pending</span></div>
        """

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>ChapNetAI Portfolio</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
*{{box-sizing:border-box}}
body{{
    margin:0;
    font-family:Arial,sans-serif;
    color:#f8fafc;
    background:
        radial-gradient(circle at top left,rgba(56,189,248,.16),transparent 30%),
        radial-gradient(circle at top right,rgba(124,255,178,.12),transparent 34%),
        linear-gradient(135deg,#020617,#071426 60%,#020617);
}}
.wrap{{width:min(1120px,100%);margin:auto;padding:24px 16px 60px}}
.hero{{
    text-align:center;
    padding:54px 12px 34px;
}}
.kicker{{
    color:#7CFFB2;
    font-weight:950;
    text-transform:uppercase;
    letter-spacing:3px;
    margin-bottom:14px;
}}
h1{{
    font-size:clamp(46px,10vw,86px);
    line-height:.95;
    margin:0 0 18px;
}}
.sub{{
    color:#cbd5e1;
    font-size:clamp(18px,4vw,24px);
    line-height:1.4;
    max-width:860px;
    margin:auto;
}}
.panel,.system,.metric-card{{
    background:linear-gradient(145deg,rgba(255,255,255,.13),rgba(255,255,255,.06));
    border:1px solid rgba(255,255,255,.16);
    border-radius:30px;
    box-shadow:0 24px 70px rgba(0,0,0,.30);
}}
.panel{{padding:26px;margin:22px 0}}
.panel h2{{font-size:34px;margin:0 0 12px}}
.panel p,.panel li{{color:#d8dee9;font-size:18px;line-height:1.55}}
.grid{{display:grid;grid-template-columns:1fr;gap:18px}}
.system{{padding:24px;border-left:8px solid #38BDF8}}
.system h3{{font-size:26px;margin:0 0 8px}}
.system p{{margin:0;color:#d8dee9;font-size:17px;line-height:1.45}}
.local{{border-left-color:#38BDF8}}
.support{{border-left-color:#22C55E}}
.journey{{border-left-color:#F6C453}}
.grant{{border-left-color:#A855F7}}
.watchman{{border-left-color:#7CFFB2}}
.exec{{border-left-color:#F59E0B}}
.metrics{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:18px}}
.metric-card{{padding:20px;text-align:center}}
.metric-card strong{{display:block;font-size:34px;color:#7CFFB2}}
.metric-card span{{display:block;color:#cbd5e1;font-weight:800;margin-top:6px}}
.badges{{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}}
.badge{{
    padding:10px 14px;
    border-radius:999px;
    background:rgba(124,255,178,.10);
    border:1px solid rgba(124,255,178,.25);
    color:#7CFFB2;
    font-weight:950;
}}
.footer{{text-align:center;color:#94a3b8;margin-top:34px}}
@media(min-width:760px){{
    .grid{{grid-template-columns:repeat(2,1fr)}}
    .metrics{{grid-template-columns:repeat(4,1fr)}}
}}
</style>
</head>
<body>
<div class="wrap">

<section class="hero">
    <div class="kicker">Built From A Samsung S23 Ultra · Termux · GitHub · Flask</div>
    <h1>ChapNetAI<br>Portfolio</h1>
    <p class="sub">
        A multi-platform community technology ecosystem built, validated, documented,
        and archived through a mobile-first development workflow.
    </p>
    <div class="badges">
        <span class="badge">Mobile-First Developer</span>
        <span class="badge">Multi-App Ecosystem</span>
        <span class="badge">Milestone-Driven Workflow</span>
        <span class="badge">Operational Validation</span>
    </div>
</section>

<section class="panel">
    <h2>Proof of Work</h2>
    <div class="metrics">
        <div class="metric-card"><strong>{milestone_folders}</strong><span>Milestone Folders</span></div>
        <div class="metric-card"><strong>{milestone_docs}</strong><span>Milestone Docs</span></div>
        <div class="metric-card"><strong>6</strong><span>Active Systems</span></div>
        <div class="metric-card"><strong>4</strong><span>Live Engines</span></div>
    </div>
</section>

<section class="panel">
    <h2>ChapNetAI Ecosystem</h2>
    <div class="grid">
        <div class="system local">
            <h3>Local Loop</h3>
            <p>Walker County digital town square with posts, photos, community feed, and local mapping.</p>
        </div>
        <div class="system support">
            <h3>Community Support Network</h3>
            <p>Structured service coordination for needs, referrals, outreach, volunteers, and partners.</p>
        </div>
        <div class="system journey">
            <h3>Joshua's Journey</h3>
            <p>Recovery, housing, workforce, resident operations, success plans, and alumni workflows.</p>
        </div>
        <div class="system grant">
            <h3>Grant Finder</h3>
            <p>Funding discovery, application drafting, pipeline, calendar, reporting, and submission workflow.</p>
        </div>
        <div class="system watchman">
            <h3>Watchman</h3>
            <p>Operational intelligence, monitoring, action queues, verification, closure, and executive briefing.</p>
        </div>
        <div class="system exec">
            <h3>Executive Command</h3>
            <p>Ecosystem integration, project history, platform health, portfolio management, and executive oversight.</p>
        </div>
    </div>
</section>

<section class="panel">
    <h2>Live Ecosystem Links</h2>
    <div class="grid">
        <div class="system journey"><h3>Command Hub</h3><p><a href="http://127.0.0.1:5056/command-landing">Open ChapNetAI Command Hub</a></p></div>
        <div class="system local"><h3>Local Loop</h3><p><a href="http://127.0.0.1:5063">Open Local Loop</a></p></div>
        <div class="system grant"><h3>Grant Finder</h3><p><a href="http://127.0.0.1:5057">Open Grant Finder</a></p></div>
        <div class="system exec"><h3>Executive Command</h3><p><a href="http://127.0.0.1:8082/ecosystem">Open Executive Command</a></p></div>
    </div>
</section>

<section class="panel">
    <h2>Founder Timeline</h2>
    <ul>
        <li><strong>March 1, 2025:</strong> ChapNetAI vision established.</li>
        <li><strong>May 2026:</strong> Major platform build cycle begins across public safety, grant funding, recovery, and ecosystem systems.</li>
        <li><strong>June 2026:</strong> Command Hub, Local Loop, Watchman, Executive Command, Milestone Registry, and Portfolio layers connected.</li>
        <li><strong>Current:</strong> Six-system ChapNetAI ecosystem running through a mobile-first development workflow.</li>
    </ul>
</section>

<section class="panel">
    <h2>Development Environment</h2>
    <div class="metrics">
        <div class="metric-card"><strong>S23</strong><span>Samsung Ultra</span></div>
        <div class="metric-card"><strong>Termux</strong><span>Mobile Linux</span></div>
        <div class="metric-card"><strong>Flask</strong><span>Python Apps</span></div>
        <div class="metric-card"><strong>GitHub</strong><span>Version Control</span></div>
    </div>
</section>

<section class="panel">
    <h2>Development Workflow</h2>
    <p>
        ChapNetAI uses a repeatable milestone workflow: build, validate, screenshot,
        archive, commit, push, and index. Each major checkpoint is preserved in
        Project History and tracked through the Milestone Registry.
    </p>
    <ul>
        <li>Mobile development environment using Samsung S23 Ultra and Termux.</li>
        <li>Multiple Flask services running as a local ecosystem.</li>
        <li>GitHub-backed project history and milestone archive.</li>
        <li>Smoke tests, route checks, screenshots, and documented stable checkpoints.</li>
    </ul>
</section>

<section class="panel">
    <h2>Milestone Registry Snapshot</h2>
    <p>
        The Project History repository indexes milestone folders and formal milestone records
        across the ChapNetAI ecosystem.
    </p>
    <div class="metrics">
        {project_rows}
    </div>
</section>

<section class="panel">
    <h2>Portfolio Positioning</h2>
    <p>
        This portfolio is designed to show the strongest professional signal:
        a complete ecosystem built from limited hardware, with disciplined validation,
        documentation, and operational thinking.
    </p>
</section>

<div class="footer">
    Powered by ChapNetAI<br>
    Operational Intelligence by Watchman
</div>

</div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5064, debug=False)
