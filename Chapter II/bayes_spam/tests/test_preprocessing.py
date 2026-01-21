import pytest

from bayes_spam.preprocessing import normalize_text, tokenize

def test_normalize_lowercase_and_punct():
    assert normalize_text("Win MONEY now!!!") == "win money now"

def test_tokenize_basic():
    assert tokenize("Win MONEY now!!!") == ["win", "money", "now"]


def test_tokenize_empty_string():
    assert tokenize("") == []


def test_tokenize_none():
    assert tokenize(None) == []


def test_tokenize_rejects_non_string():
    with pytest.raises(TypeError):
        tokenize(123)  # type: ignore[arg-type]