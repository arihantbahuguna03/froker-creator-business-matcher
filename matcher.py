"""
Creator–Business Matching Agent
=======================================
Matches local businesses to the right creator using
profile scoring + Claude 3.5 Sonnet reasoning.

Built Aug 2024 – Aug 2025 using raw Anthropic SDK.
No LLM orchestration frameworks — direct API calls only.

Problem:
  Local businesses on the platform get manually matched to creators by the
  operations team — a gut-feel process that produces wrong matches,
  bad content, and businesses that don't renew.

Solution:
  Business fills a brief. Each creator is pre-scored against it on
  4 dimensions: niche fit, location overlap, engagement quality,
  content style. Top 5 are passed to Claude, which returns a ranked
  shortlist with written reasoning per creator.

Usage:
    python matcher.py --business DEMO_BIZ_001
    python matcher.py --all
"""

import argparse
import json
import os

import anthropic

from demo_data import DEMO_BUSINESSES, DEMO_CREATORS


# ── Pre-scoring (rule-based) ──────────────────────────────────────────────────

def niche_overlap(creator: dict, business: dict) -> float:
    creator_niches = set(creator["niche"] + creator["past_brand_categories"])
    biz_category   = business["category"].lower()
    return 1.0 if biz_category in creator_niches else 0.0


def location_score(creator: dict, business: dict) -> float:
    biz_locality = business["locality"].lower()
    creator_locs = [l.lower() for l in creator["localities"]]
    if biz_locality in creator_locs:
        return creator["audience_local_pct"]
    return creator["audience_local_pct"] * 0.5


def pre_score(creator: dict, business: dict) -> float:
    niche    = niche_overlap(creator, business) * 40
    location = location_score(creator, business) * 30
    engage   = creator["avg_engagement_rate"] * 100 * 20
    local    = creator["audience_local_pct"] * 10
    return round(niche + location + engage + local, 2)


def shortlist_creators(business: dict, top_n: int = 5) -> list[dict]:
    scored = [
        {**c, "_pre_score": pre_score(c, business)}
        for c in DEMO_CREATORS
    ]
    scored.sort(key=lambda x: x["_pre_score"], reverse=True)
    return scored[:top_n]


# ── Claude matching ───────────────────────────────────────────────────────────

def claude_match(business: dict, candidates: list[dict]) -> str:
    client = anthropic.Anthropic()

    creators_text = "\n\n".join(
        f"Creator ID: {c['creator_id']}\n"
        f"Name: {c['name']}\n"
        f"Niche: {', '.join(c['niche'])}\n"
        f"City/Localities: {', '.join(c['localities'])}\n"
        f"Followers: {c['followers']}\n"
        f"Avg Engagement Rate: {c['avg_engagement_rate']*100:.1f}%\n"
        f"Local Audience %: {c['audience_local_pct']*100:.0f}%\n"
        f"Content Style: {c['content_style']}\n"
        f"Past Categories: {', '.join(c['past_brand_categories'])}\n"
        f"Avg Reach/Post: {c['avg_reach_per_post']}"
        for c in candidates
    )

    prompt = f"""You are a creator-brand matching expert for a creator marketplace that connects local businesses with content creators.

A local business has submitted a campaign brief. Your job is to rank the shortlisted creators and explain your reasoning.

BUSINESS BRIEF:
Business: {business['name']}
Category: {business['category']}
Location: {business['locality']}, {business['city']}
Budget: ₹{business['budget_inr']} per post
Brief: {business['brief']}

SHORTLISTED CREATORS:
{creators_text}

Rank these creators from best to worst fit for this business. For each creator, write:
1. Rank and creator name
2. A 2-sentence reason why they are or aren't the right fit
3. One specific thing about their profile that clinches or hurts the match

End with a 1-line recommendation: which creator to go with and why."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text.strip()


# ── Main ──────────────────────────────────────────────────────────────────────

def match_business(business_id: str) -> None:
    business = next((b for b in DEMO_BUSINESSES if b["business_id"] == business_id), None)
    if not business:
        print(f"Business {business_id} not found.")
        return

    print(f"\n{'='*65}")
    print(f"  MATCHING: {business['name']}")
    print(f"  Brief: {business['brief'][:80]}…")
    print(f"{'='*65}\n")

    print("Pre-scoring creators…")
    candidates = shortlist_creators(business)
    for c in candidates:
        print(f"  {c['name']}: pre-score {c['_pre_score']}")

    print("\nAsking Claude to rank and explain…\n")
    result = claude_match(business, candidates)
    print(result)
    print()


def match_all() -> None:
    for biz in DEMO_BUSINESSES:
        match_business(biz["business_id"])
        print("\n" + "─"*65 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--business", help="Business ID to match")
    parser.add_argument("--all", action="store_true", help="Match all demo businesses")
    args = parser.parse_args()

    if args.all:
        match_all()
    elif args.business:
        match_business(args.business)
    else:
        print("Usage: python matcher.py --business DEMO_BIZ_001")
        print("       python matcher.py --all")
