from stats import get_num_words, get_characters, sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents
book_path = 'books/frankenstein.txt'
text = get_book_text(book_path)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {get_num_words(text)} total words")
print("--------- Character Count -------")

character = get_characters(text)

for item in sorted_dict(character):
    if item["char"].isalpha():
        print(f'{item["char"]}: {item["num"]}')