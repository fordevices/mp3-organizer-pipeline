# Design Decisions

## The problem

A collection of 1000+ Tamil, Hindi, and English MP3 files with garbled filenames, missing
or wrong ID3 tags, and no consistent naming convention. Existing tools (MusicBrainz Picard,
beets, mp3tag) either require manual matching or rely on AcoustID — which has poor coverage
of Indian film music pre-2000. The goal was a zero-configuration pipeline that could handle
the entire collection overnight, with a review step for anything it couldn't identify
automatically.

---

## Key decisions

| Decision | Choice | Reason |
|---|---|---|
| Fingerprint engine | ShazamIO | Largest database, best Indian music coverage, no key, no binary required |
| Language classification | User pre-sorts input folders | Zero guesswork, full control, no language detection code needed |
| Output structure | `Language/Year/Album/` | Clean, chronological per language, mirrors how people browse music |
| Persistence | SQLite | Resume-safe, zero setup, single file, no server needed |
| Tagging library | Mutagen | Battle-tested ID3 writer, UTF-8 support, handles missing headers |

---

## Fingerprinting API comparison

| Criterion | AcoustID + MusicBrainz | **ShazamIO** ✅ | ACRCloud |
|---|---|---|---|
| Database size | ~30M fingerprints, ~10M linked to MusicBrainz | **~200M+ tracks** (Shazam's full database) | 150M+ tracks |
| Tamil coverage | Moderate — community-submitted, gaps pre-2000 | **Excellent** — Shazam is widely used in India; Tamil film music well represented | Good — commercial DB, India coverage strong |
| Hindi / Bollywood | Good, some gaps | **Excellent** | Excellent |
| English | Excellent | Excellent | Excellent |
| Cost | Free, register for key at acoustid.org | **100% Free — no key, no signup** | 14-day trial, then paid (pricing hidden behind login) |
| Python install | `pip install pyacoustid` + **fpcalc binary must be OS-installed** | **`pip install shazamio` — nothing else** | SDK available, heavier setup |
| Binary required? | ✅ Yes — Chromaprint (`fpcalc`) must be installed via brew/apt | **❌ No — pure Python + Rust wheel** | No |
| Rate limits | MusicBrainz: strict 1 req/sec | No documented limit; reasonable throttling recommended | Trial limits unlisted |
| Metadata returned | Title, Artist, Album, Year, MusicBrainz IDs | **Title, Artist, Album, Genre, Cover art URL, Apple Music / Spotify links** | Title, Artist, Album, Year, ISRC, UPC |
| Stability | Open spec, very stable | Reverse-engineered — could break if Shazam changes internals (actively maintained since 2021, v0.8.1 Jun 2025) | Commercial SLA |
| Best for | Open-source purists, Western music-heavy libraries | **Indian music libraries, zero-cost, fastest to start** | Commercial apps, highest reliability |

---

## Why ShazamIO wins for this use case

- Shazam is the dominant music recognition app in India — Tamil and Hindi film music from the
  1970s onward is heavily indexed because millions of Indian users have Shazamed those songs.
- No `fpcalc` binary to install. No API key to register. Just `pip install shazamio` and go.
- The metadata package is richer out of the box — cover art URL is included in the response,
  no separate Cover Art Archive call needed.
- The library has been actively maintained for 4+ years through multiple Shazam API changes,
  which is a reasonable signal of durability for a personal project.

---

## Honest trade-off

ShazamIO reverse-engineers Shazam's private API. It is not an officially supported
integration. It could break if Apple/Shazam changes their internal endpoints. The library
has survived multiple such changes since 2021 (it is on v0.8.1 as of Jun 2025), but this
remains a real risk for a long-running project.

If it breaks, the fallback plan is AcoustID + MusicBrainz — fully documented below.

---

## Fallback plan — if ShazamIO breaks

1. `pip install pyacoustid`
2. Install Chromaprint:
   - macOS: `brew install chromaprint`
   - Linux: `sudo apt install libchromaprint-tools`
   - Windows: download `fpcalc` from https://acoustid.org/chromaprint
3. Register a free API key at https://acoustid.org (takes 2 minutes, no payment)
4. Replace `pipeline/identify.py` with an AcoustID implementation

The DB schema, all other stages, the review CLI, and the folder structure are completely
unchanged. Only Stage 1 needs to be swapped.

Match rate for Indian music will drop from ~86% to an estimated 40–70% on older tracks,
as AcoustID's community database has fewer Indian music submissions than Shazam's.

---

## Metadata search pass — design rationale

The `--metadata-search` pass (`pipeline/filename_pass.py`) is a text-based identification
pass for files that Shazam and AcoustID both failed on. It is distinct from audio
fingerprinting: rather than analysing the sound, it constructs a text query from whatever
signals are available and searches music metadata APIs.

### Signal priority

Many badly-named files have perfectly good ID3 tags embedded — the filename was garbled
by the ripper or download tool but the tags were set correctly at rip time. The pass
reads ID3 tags from the file before falling back to the cleaned filename:

1. **`TIT2` (title) + `TPE1` (artist)** — most precise; used when both are present
2. **`TIT2` (title) alone** — used when the artist tag is missing or empty
3. **Cleaned filename** — last resort; strips track numbers, underscores, brackets,
   year tokens, and square-bracket content before searching

### Query cascade

Rather than sending one query and giving up, the pass tries progressively simpler queries
until a result above a confidence threshold is found:

```
tags: title + artist  →  any result?  →  show candidates
          ↓ no
tags: title alone     →  any result?  →  show candidates
          ↓ no
cleaned filename      →  any result?  →  show candidates
          ↓ no
→ mark as no_mb_match, move on
```

### Search source comparison

| Service | Auth required | Strengths for this use case |
|---|---|---|
| **MusicBrainz** | None | Open database; strong for Western, classical, and well-catalogued Indian film music; returns confidence scores |
| **iTunes Search API** (Apple) | None | Apple Music catalog; excellent coverage of Tamil and Hindi film music; clean structured data; no rate limit documented |
| **Deezer API** | None | Good mainstream coverage; decent Indian music catalog; straightforward JSON response |

Both MusicBrainz and iTunes are queried with no API key or account. MusicBrainz enforces
a strict 1 req/sec rate limit (handled by `time.sleep(1.1)` between calls). iTunes has no
published rate limit but is used conservatively. Deezer is available as a future extension.

The pass labels each candidate with which signal was used (tags vs filename) so the user
can judge the result in context.

---

## Links

[README.md](../README.md) | [Architecture](ARCHITECTURE.md) | [Database Reference](DATABASE.md)
