import sys
from stats import get_num_words, get_char_count, sorted_chars

def get_boot_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_boot_text(book)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars = get_char_count(text)
    char_list = sorted_chars(chars)
    for e in sorted_chars(chars):
        c = e["char"]
        count = e["count"]
        if c.isalpha():
            print(f"{c}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()