import re

def identify_numbers_and_texts(input_string):
    
    number_pattern = r'\d+'
    text_pattern = r'[A-Za-z]+'

    
    numbers = re.findall(number_pattern, input_string)
    texts = re.findall(text_pattern, input_string)

    return numbers, texts

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    numbers, texts = identify_numbers_and_texts(input_string)

    print("Numbers found: ", numbers)
    print("Texts found: ", texts)
