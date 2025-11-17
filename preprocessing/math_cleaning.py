"""
Math Cleaning Module

Handles:
- Replacing unicode math symbols (×, ÷, −)
- Normalizing operators to standard ASCII equivalents
- Cleaning malformed mathematical strings

Purpose:
Ensure mathematical expressions are embedding-friendly and consistent.
"""

# math_cleaning.py
# Normalization helpers for math formulas inside exam questions.

import re

def normalize_math(text: str) -> str:
    if not text:
        return ""

    # Replace unicode math operators with ASCII
    text = text.replace("×", "*").replace("÷", "/")

    # Remove strange characters but keep common math symbols
    text = re.sub(r"[^0-9a-zA-Z\s\^\*\+\-\/=()\[\],.:%]", " ", text)

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text

if __name__ == "__main__":
    s = "Solve: 2×(3 + 4) ÷ 2"
    print(normalize_math(s))
