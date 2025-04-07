def count_words(text):
    split_text = text.split()
    return len(split_text)

def count_characters(text):
    text_lower = text.lower()
    character_dict = {}
    for char in text_lower:
        character_dict[char] = character_dict.get(char, 0) + 1

    return character_dict
