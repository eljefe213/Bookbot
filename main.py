from stats import get_num_words, get_characters, sorted_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents

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

print("============= END ===============")