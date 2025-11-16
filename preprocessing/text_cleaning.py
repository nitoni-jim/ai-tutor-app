# text_cleaning.py
# Utilities for normalizing and cleaning WAEC/NECO/JAMB question text.

import re
import unicodedata

def normalize_unicode(text: str) -> str:
    """Normalize unicode to NFKC form."""
    return unicodedata.normalize("NFKC", text)

def remove_extra_whitespace(text: str) -> str:
    """Collapse repeated whitespace and strip."""
    return re.sub(r"\s+", " ", text).strip()

def normalize_dashes(text: str) -> str:
    """Convert long dashes to normal ASCII dash."""
    return text.replace("—", "-").replace("–", "-").replace("−", "-")

def clean_text(text: str) -> str:
    """Full cleaning pipeline for general text."""
    if not text:
        return ""
    text = normalize_unicode(text)
    text = normalize_dashes(text)
    text = remove_extra_whitespace(text)

    # Remove control characters
    text = re.sub(r"[\x00-\x1f\x7f]", "", text)
    return text

if __name__ == "__main__":
    s = "  Solve — for x:   2x + 5 = 11   "
    print(clean_text(s))
