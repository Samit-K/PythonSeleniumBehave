import re


def extract_number_from_string(string_value):
    cleaned_string = re.sub(r'[^\d.]', '', string_value)
    return str(cleaned_string)
