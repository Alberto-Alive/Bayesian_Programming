"""
We need to take the email text and tokenise the words so that for example
 "Money!!!" and "money" to both produce the token "money"
"""
import re
from typing import List, Optional

#let's create a private constant of allowed letters
_NON_LETTERS = re.compile(r"[^a-z]+")

def normalize_text(text: str) -> str:
    # substitute non a-z chars with " " then remove whitespace from beginning and end of string
    # example: text = "!!!Hello ! World!!!" -> " hello  world " -> "hello  world"
    cleaned = _NON_LETTERS.sub(" ", text.lower()).strip()
    #collapse repeated white space: "hello  world" -> "hello world" 
    # it first "  hello   world \n python  ".split() into ['hello', 'world', 'python'] then joins the list back into a string inserting exactly one space between words
    cleaned = " ".join(cleaned.split())
    return cleaned


def tokenize(text: Optional[str]) -> list[str]:
    """
    Rules:
    - None -> []
    - Only accepts str : Other types raise 
    - normalise else return []
    """
    if text is None:
        return []
    
    if not isinstance(text, str):
        raise TypeError(f"tokenise() was expecting str or Noen but got {type(text).__name__}")
    
    normalized = normalize_text(text)
    
    if not normalized:
        return []
    
    return normalized.split()