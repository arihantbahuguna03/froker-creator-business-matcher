"""
Creator–Business Matching Config — Example
===========================================
Copy this file to matching_config.py and fill in your calibrated values.
matching_config.py is gitignored — this example shows the structure only.

Weights were calibrated against historical deal outcomes (renewal rate,
content quality scores, business satisfaction surveys). They determine how
much each dimension contributes to a creator's pre-score for a business.
The four weights must sum to 100.
"""

# ── Pre-scoring dimension weights (must sum to 100) ───────────────────────────
# Calibration: proprietary — available on request.
NICHE_WEIGHT    = None   # how much niche/category overlap matters
LOCATION_WEIGHT = None   # how much local audience overlap matters
ENGAGE_WEIGHT   = None   # how much engagement rate matters
LOCAL_AUD_WEIGHT = None  # how much % local audience matters
