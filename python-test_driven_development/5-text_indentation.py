#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    specialCharacters = ['.', '?', ':']
    formatted_text = ""
    for char in text:
        formatted_text += char
        if char in specialCharacters:
            formatted_text += '\n\n'
    print(formatted_text.strip())
