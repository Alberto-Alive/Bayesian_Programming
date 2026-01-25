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


# Vocabulary / feature configuration
VocabMode = Literal["fixed", "top_n"]


# The fixed vocab would reproduce the tables/results in chapter 2 whereas top_n is for general training
DEFAULT_VOCAB_MODE: VocabMode = "fixed"

# The 5 words hand pciked in chapter two (Table 2.1/2.2 example)

CHAPTER2_FIXED_VOCAB: tuple[str, ...] = (
    "fortune",
    "next",
    "programming",
    "money",
    "you",
)


# Tokenization / filtering knobs
DEFAULT_TOKEN_MIN_LEN: int = 2
DEFAULT_ALLOW_NUMBERS: bool = False

DEFAULT_ASCII_ONLY: bool = False


# -----------------------------
# Optional default paths
# -----------------------------
DEFAULT_MODEL_PATH: str = "models/spam_model.json"
DEFAULT_TRAIN_DATA_PATH: str = "data/processed/train.jsonl"


@dataclass(frozen = True)
class Settings:
    """
    Immutable settings bundle that can be passed around instead of importing each individual constant
    """
    # Feature space
    n_vocab: int = DEFAULT_N_VOCAB
    vocab_mode: VocabMode = DEFAULT_VOCAB_MODE
    # we''l make it a sequence to be more flexible
    fixed_vocab: Sequence[str] = CHAPTER2_FIXED_VOCAB


    # Prior
    prior_mode: PriorMode = DEFAULT_PRIOR_MODE
    prior_spam_true: float = DEFAULT_PRIOR_SPAM_TRUE


    # Decision rule
    threshold: float = DEFAULT_THRESHOLD


    # Token controls (used by preprocessing/features)
    token_min_len: int = DEFAULT_TOKEN_MIN_LEN
    allow_numbers: bool = DEFAULT_ALLOW_NUMBERS
    ascii_only: bool = DEFAULT_ASCII_ONLY


    # Paths
    model_path: str = DEFAULT_MODEL_PATH
    train_data_path: str = DEFAULT_TRAIN_DATA_PATH  
        