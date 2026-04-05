def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents

def get_book_words(contents):
    list_of_words = contents.split()
    return len(list_of_words)

main = get_book_text('books/frankenstein.txt')
print(f"Found {get_book_words(main)} total words")