def count_words(text: str) -> int:
    if not text.strip():
        return 0
    return len(text.split())
