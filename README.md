# 🎵 mp3-organizer-pipeline

> Transform a folder of mystery MP3s into a perfectly organised, fully tagged
> collection — sorted by language, year, and album. No API keys. No accounts.
> Works on macOS, Linux, and Windows.

---

## What it does

Takes a folder of unknown, badly-named MP3s and runs them through a four-stage pipeline:

```
Input/Tamil/mystery_track.mp3
        │
        ▼
┌──────────────────────────────────────────────────┐
│  Stage 1 — ShazamIO fingerprint + identify       │
│  Stage 2 — Manual review + override (no match)   │
│  Stage 3 — Mutagen writes ID3 tags into file     │
│  Stage 4 — File renamed and moved to folder      │
└──────────────────────────────────────────────────┘
        │
        ▼
Music/Tamil/2001/Minnale/Vaseegara.mp3
```

Every file processed is recorded in a local SQLite database (`music.db`) — the pipeline
is fully resume-safe and can be stopped and restarted at any point across a collection
of thousands of files.

---

## Quick start

```bash
# 1. Clone and install
git clone https://github.com/fordevices/mp3-organizer-pipeline.git
cd mp3-organizer-pipeline
python3 -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 main.py --check
```

```
# 2. Sort your files by language and drop them in
Input/Tamil/   Input/Hindi/   Input/English/   Input/Other/
```

```bash
# 3. Run
python3 main.py Input/
```

For full installation instructions including Windows, see [DOCS/USER_GUIDE.md](DOCS/USER_GUIDE.md).

---

## Documentation

| Document | What it covers |
|---|---|
| [User Guide](DOCS/USER_GUIDE.md) | Install on macOS / Linux / Windows, full CLI reference, running the pipeline, manual review, match rate expectations |
| [Architecture](DOCS/ARCHITECTURE.md) | Pipeline stages, modules, file structure, status flow, run logging |
| [Design Decisions](DOCS/DESIGN_DECISIONS.md) | Why ShazamIO was chosen, API comparison table, trade-offs, fallback plan |
| [Database Reference](DOCS/DATABASE.md) | Full schema, song ID format, persistence, interruption safety |
| [Music Files Primer](DOCS/MUSIC_FILES_PRIMER.md) | What MP3s are, how ID3 tags work, what audio fingerprinting does, how Shazam works |
| [Build History](DOCS/BUILD_HISTORY.md) | How the codebase was built session by session using Claude CLI |
| [Contributing](CONTRIBUTING.md) | How to raise bugs and features, PR workflow, issue templates |
| [Claude CLI Workflow](CLAUDE_CLI_WORKFLOW.md) | How to use Claude CLI to implement issues on this repo |

---

## Results

| Music type | Match rate |
|---|---|
| Tamil film music 1990s–2010s | ~90% |
| Tamil film music 1970s–1980s | ~75% |
| Hindi / Bollywood | ~85–90% |
| English mainstream | ~90%+ |
| Obscure / pre-1970 | ~40–60% |

Tested on 26 files including 1970s–2000s Ilaiyaraaja and classic Hindi film music.
86% automated match rate. 0 pipeline errors.

---

## Status

**v1.0.0 — released March 21, 2026**

All future work is tracked as GitHub issues:
https://github.com/fordevices/mp3-organizer-pipeline/issues

Bugs → label `bug` | Features → label `enhancement`
