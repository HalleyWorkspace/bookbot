def get_book_text(file):
    with open(file) as f:
        return f.read()

def num_words(book_text):
    text_list=book_text.split()
    return len(text_list)

def main():
    file_path="books/frankenstein.txt"
    book_text=get_book_text(file_path)
    word_count=num_words(book_text)
    print(f"{word_count} words found in the document")

main()