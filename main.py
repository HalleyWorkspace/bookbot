from stats import num_words,char_counts

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    file_path="books/frankenstein.txt"
    book_text=get_book_text(file_path)
    word_count=num_words(book_text)
    print(f"{word_count} words found in the document")
    print(char_counts(book_text))

main()