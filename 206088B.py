import re
from collections import Counter

def identify_numbers_and_texts(input_string):
    
    number_pattern = r'\d+'
    text_pattern = r'[A-Za-z]+'

    
    numbers = re.findall(number_pattern, input_string)
    texts = re.findall(text_pattern, input_string)

    
    number_counts = Counter(numbers)
    text_counts = Counter(texts)

    return number_counts, text_counts

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    number_counts, text_counts = identify_numbers_and_texts(input_string)

    print("Numbers found: ", number_counts)
    print("Texts found: ", text_counts)

