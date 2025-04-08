from stats import count_words, count_characters, character_sort_list
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    args = sys.argv
    if len(args) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = args[1]
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    characters_dictionary = count_characters(text)
    sorted_character_list = character_sort_list(characters_dictionary)
    for list_item in sorted_character_list:
        character = list(list_item.keys())[0]
        print(f"{character}: {list_item[character]}")


main()