import collections
import math

def calculate_entropy(text):
    # Count the number of occurrences of each character in the text
    frequencies = collections.Counter(text)

    # Total number of characters in text
    total_characters = len(text)

    # Calculation of entropy by formula
    entropy = -sum((count / total_characters) * math.log2(count / total_characters)
        for count in frequencies.values())

    return entropy

# Example of use
text_example = "aaaabbcd"
entropy_value = calculate_entropy(text_example)
print(f"Entropy of text: {entropy_value} bit")