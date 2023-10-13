import re
from collections import Counter

def identify_numbers_and_texts(input_string):
    number_pattern = r'\d+'
    text_pattern = r'[A-Za-z]+'

    numbers = re.findall(number_pattern, input_string)
    texts = re.findall(text_pattern, input_string)

    number_counts = Counter(numbers)
    text_counts = Counter(texts)
    
    # Calculate the total count of characters in the input string
    total_characters = len(input_string)

    return number_counts, text_counts, total_characters

if __name__ == "__main":
    input_string = input("Enter a string: ")
    number_counts, text_counts, total_characters = identify_numbers_and_texts(input_string)

    print("Numbers found: ", number_counts)
    print("Texts found: ", text_counts)
    print("Total characters in the input string: ", total_characters)
