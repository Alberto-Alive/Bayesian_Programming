"""
Bayesian (Naive Bayes) spam model with Laplace succession smoothing.

Implements the Chapter 2 model:
- Variables: Spam (binary), W0..W(N-1) (binary presence/absence)
- Decomposition: P(Spam, W) = P(Spam) * Π_i P(W_i | Spam)
- Parametric forms: Laplace succession laws for P(W_i=1 | Spam)
- Identification: counters nf/nt/nfi/nti updated from labeled examples
- Question: compute P(Spam | w) using log-odds (ratio trick, Eq. 2.33)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
import math

# let's make the probabilities limits slightly higher than zero and slightly lower than one

def _clamp_prob(p: float, eps: float = 1e-12) -> float:
    if p < eps:
        return eps
    if p > 1.0 - eps:
        return 1.0 -eps
    return p
      
      
        # so we're just gonna do the naive one bcs interdependance between probs would be too complciated
@dataclass
class NaiveBayesSpamModel:
    