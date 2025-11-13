# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    # Remove punctuation
    for ch in string.punctuation:
        text = text.replace(ch, "")

    # Split into words
    words = text.split()

    # Count word frequencies using dictionary comprehension
    counts = {word: words.count(word) for word in set(words)}

    # Filter based on lower_limit
    result = {word: count for word, count in counts.items() if count >= lower_limit}

    return result


# Example usage
if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))