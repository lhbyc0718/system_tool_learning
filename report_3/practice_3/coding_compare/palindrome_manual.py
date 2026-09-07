def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_cases = ["A man a plan a canal Panama", "racecar", "hello"]
    for t in test_cases:
        print(f"'{t}' -> {is_palindrome(t)}")
