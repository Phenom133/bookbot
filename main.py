from stats import count_words, count_characters
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    text = get_book_text('books/frankenstein.txt')
    print(f"{count_words(text)} words found in the document")
    print(count_characters(text))

main()