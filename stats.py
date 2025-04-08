def count_words(text):
    split_text = text.split()
    return len(split_text)

def count_characters(text):
    text_lower = text.lower()
    character_dict = {}
    for char in text_lower:
        character_dict[char] = character_dict.get(char, 0) + 1

    return character_dict

def character_sort_list(character_dictionary):
    character_list = []
    for character in character_dictionary:
        if character.isalpha():
           single_character_dict = {character: character_dictionary.get(character)}
           character_list.append(single_character_dict)

    return sorted(character_list, key=lambda d: list(d.values())[0],reverse= True)