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
        
        if len(items) < N:
            raise ValueError(
                f"Not enough unique tokens to build vocab of size {N}"
                f"Have {len(items)} after filtering (min_df={min_df}, min_len={min_len}, max_len={max_len})"
            )
        
        self.vocab = [tok for tok, _df in items[:N]]
        self._rebuild_index()
        self.last_fit_params = {"N": N, "min_df": min_df, "min_len": min_len, "max_len": max_len}
        return self
    
    def transform(self, tokens: Collection[str]) -> List[int]:
        if not self.vocab:
            raise ValueError("Vectorizer has no vocab. Call fit(....) or construct with a fixed vocab first")
        vec = [0] * len(self.vocab)
        for t in tokens:
            i = self.word_to_idx.get(t)
            if i is not None:
                vec[i] = 1
        return vec
    
    def transform_many(self, tokenized_emails: Iterable[Collection[str]]) -> List[List[int]]:
        return [self.transform(tokens) for tokens in tokenized_emails]
    
    
    def fit_transform(
        self, tokenized_emails: list[Collection[str]],
        N: int,
        *,
        min_df: int =1,
        min_len: int =2,
        max_len: Optional[int] =None,
    ) -> List[List[int]]:
        self.fit(tokenized_emails, N, min_df=min_df, min_len=min_len, max_len=max_len)
        return self.transform_many(tokenized_emails)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "vocab": list(self.vocab),
            "last_fit_params": dict(self.last_fit_params),
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "BinaryWordVectorizer":
        vocab = d.get("vocab")
        if not isinstance(vocab, list) or not all(isinstance(x, str) for x in vocab):
            raise ValueError("Invalid vectorizer dict: expected key 'vocab' as list[str]" )
        vec = cls(vocab=vocab)
        params = d.get("last_fit_params")
        if isinstance(params, dict):
            vec.last_fit_params = dict(params)
        return vec