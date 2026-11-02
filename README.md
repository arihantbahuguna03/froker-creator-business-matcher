# Froker Creator–Business Matching Agent

Matches local businesses to the right Froker creator using pre-scoring across 4 dimensions + Claude 3.5 Sonnet reasoning. Returns a ranked shortlist with written justification per creator.

> Built Aug 2024 – Aug 2025 using Claude 3.5 Sonnet API directly — before MCP and modern agentic tooling existed in production-ready form. All orchestration is raw Python + direct API calls.

---

## Problem

Froker connects local businesses (cafes, gyms, salons, stores) with content creators for paid campaigns. The operations team was manually going through creator profiles and making gut-feel matches.

**Result:** Wrong matches → bad content → business doesn't renew → Froker loses commission revenue. No way to scale with a small team.

---

## Solution

A two-stage matching pipeline:

**Stage 1 — Rule-based pre-scoring** (fast, deterministic)
- Niche overlap: does the creator post in the business's category?
- Location overlap: is the creator's audience in the business's area?
- Engagement quality: engagement rate weighted toward saves/shares
- Local audience %: what % of followers are in the right city

**Stage 2 — Claude reasoning** (slow, nuanced)
- Top 5 pre-scored creators are passed to Claude with the full business brief
- Claude ranks them and writes 2-sentence reasoning per creator
- Returns a clear recommendation: who to go with and why

---

## Architecture

```
Business submits brief
    └── Pre-score all creators (rule-based)
            └── Top 5 → Claude 3.5 Sonnet
                    └── Ranked shortlist + written reasoning
                            └── Operations team acts on recommendation
```

---

## Files

| File | Description |
|---|---|
| `matcher.py` | Pre-scoring + Claude matching agent |
| `demo_data.py` | Demo creator profiles and business briefs |
| `requirements.txt` | Dependencies |

---

## Sample Output

```
MATCHING: Demo Cafe Koramangala
Brief: We are a new specialty coffee cafe in Koramangala...

Pre-scoring creators...
  Creator Alpha:   pre-score 87.4
  Creator Epsilon: pre-score 81.2
  Creator Beta:    pre-score 43.1
  Creator Gamma:   pre-score 31.8
  Creator Delta:   pre-score 22.4

Asking Claude to rank and explain...

Rank 1 — Creator Alpha
Best fit for this brief. Their niche is food and cafes, and 54% of their
audience is in Koramangala and HSR Layout — exactly the footfall catchment
for this cafe. Their honest, conversational review style aligns with the
brief's ask for authentic content.
Clincher: Their last 3 posts were cafe reviews in Koramangala. Category + location match is exact.

Rank 2 — Creator Epsilon
Strong food creator with good local reach. However, their content style
leans more aesthetic/aspirational than the warm/honest tone the brief asks for.
Clincher: 71% local audience is strong, but their Koramangala content is brunch-focused
rather than specialty coffee — slight niche gap.

...

Recommendation: Go with Creator Alpha. Exact niche, exact location, matching content style.
```

---

## Run locally

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
python matcher.py --business DEMO_BIZ_001
python matcher.py --all
```

---

## Design Decisions

| Decision | Reasoning |
|---|---|
| Two-stage: rules then LLM | Rules eliminate obviously wrong matches cheaply. Claude focuses on nuance among the shortlist, not all 200 creators |
| Audience locality % as a key signal | For a local business, a creator with 5K local followers beats one with 50K national followers |
| Written reasoning per creator | Business owners need to trust the recommendation. A ranked number without reasoning gets ignored |
| Raw Anthropic SDK | Built Aug 2024 — no stable agent framework. Direct API gives deterministic control over the prompt |
