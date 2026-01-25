"""
This is to manage the fixed vocab/dict and convert a token collection into the binary 
vector W (takes either present or absent vals).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from collections import Counter
from typing import Collection, Iterable, List, Dict, Any, Optional

@dataclass
class BinaryWordVectorizer:
    vocab: List[str] = field(default_factory=list)
    word_to_idx: Dict[str, int] = field(default_factory=dict, init=False)
    
    last_fit_params: Dict[str, Any] = field(default_factory=dict, init=False)
    
    def __post_init__(self) -> None:
        