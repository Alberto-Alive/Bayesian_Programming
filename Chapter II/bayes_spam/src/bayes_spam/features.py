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
        self._rebuild_index()
        
    @property
    def n_features(self) -> None:
        return len(self.vocab)
    
    def _rebuild_index(self) -> None:
        self.word_to_idx = {w:i for i, w in enumerate(self.vocab)}
        
        
    def fit(
        self, 
        tokenized_emails: Iterable[Collection[str]],
        N: int,
        *,
        min_df: int = 1,
        min_len: int = 2,
        max_len: Optional[int] = None,
    ) -> "BinaryWordVectorizer":
        if N <= 0: 
            raise ValueError("N must be a positive integer.")
        df_counter: Counter[str] = Counter()
        
        for tokens in tokenized_emails:
            seen = set(tokens)
            filtered: List[str] = []
            for t in seen:
                if not isinstance(t, str):
                    continue
                if len(t) < min_len:
                    continue
                if max_len is not None and len(t) > max_len:
                    continue
                filtered.append(t)
            df_counter.update(filtered)
            # min_diff helps us filter out words that are quite rare i.e. seen in a few emails only
        items = [(tok, df) for tok, df in df_counter.items() if df >= min_df]
        
        # sort these pairs by df firstly then by letters
        # bcs sort does ascending order by default we have to times it by -1 to inverse that ordering.. trick
        items.sort(key=lambda x: (-x[1], x[0]))
        
    