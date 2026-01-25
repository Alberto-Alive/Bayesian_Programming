"""
bayes_spam.config


Central configuration for the Bayesian spam filter project.


Principles:
- Pure data: constants + a small Settings object.
- No side effects (no file I/O, no CLI parsing, no imports from other project modules).
- Makes it easy to switch between:
(1) Chapter-2 demo mode (fixed 5-word vocab, fixed prior),
(2) "real" mode (top-N vocab from data, learned prior).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Sequence


# Default dictionary size (N)
DEFAULT_N_VOCAB: int = 5

# Default threshold for converting P(Spam|w) into spam/non-spam
DEFAULT_THRESHOLD: float = 0.5

# Prior (P(Spam)) configuration
PriorMode = Literal["fixed", "learned"]

# Default prior mode and prior spam is true
DEFAULT_PRIOR_MODE: PriorMode = "fixed"
DEFAULT_PRIOR_SPAM_TRUE: float = 0.75 # complement is (1 - this)
