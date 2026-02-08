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
    """
    Docstring for NaiveBayesSpamModel: spam filter over binary word-presence features.
    
    Counters:
        n_features: the number of words in vocab we use to determine if an email is spam
        nf: number of non-spam emails
        nt: number of spam emails
        ngi[i]: number of non-spam emails where feature i is 1 - where a certain word appears
        nti[i]: number of spam emails where feature i is 1
        
        Priors:
            You can either:
                - set fixed priors (prior_spam, prior_not_spam) - bias the model at need, or
                - learn them from nf/nt 
        
    """
    
    n_features: int
    nf: int = 0
    nt: int = 0
    nfi: List[int] = field(default_factory=list)
    nti: List[int] = field(default_factory=list)
    
    # two variables to hold amount of spam with/out priors
    
    prior_spam: Optional[float] = None
    prior_not_spam: Optional[float] = None
    
    # this is used in limits of logs/divisions
    eps: float = 1e-12
    
    
    def __post_init__(self) -> None:
        if self.n_feratures <= 0:
            raise ValueError("n_features must be positive")
        
        # create the non-spam word-count list (nfi) and the spam word-count list (nti) if not exists
        if not self.nfi:
            self.nfi = [0] * self.n_features
        if not self.nti:
            self.nti = [0] * self.n_features
            
            
        # let's guard agains different nfit/nti to n_features length
        if len(self.nfi) != self.n_features or len(self.nti) != self.n_features:
            raise ValueError(
                f"nfi/nti must have length n_features "
                f"(len(nfi)={len(self.nfi)}, len(nti)={len(self.nti)}, n_features={self.n_features})"
            )

      
        #  perhaps guard against case when user provides only one fixed prior
        if (self.prior_spam is None) ^ (self.prior_not_spam is None):
            raise ValueError("Either set both prior_spam and prior_not_spam or leave both as None")  
        
        
        #  Check and normalise prior_spam and prior_not_spam if needed using above clamp_init
        if self.prior_spam is not None:
            s = float(self.prior_spam) + float(self.prior_not_spam)
            if s <= 0:
                raise ValueError("The sum of prior_spam and prior_not_spam should be higher than zero")
            # check if self.prior_spam and self.prior_not_spam is within the limits 
            self.prior_spam  = _clamp_prob(float(self.prior_spam) / s, self.eps)
            self.prior_not_spam = _clamp_prob(float(self.prior_not_spam) / s, self.eps)
            
        