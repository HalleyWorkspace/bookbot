def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    file_path="books/frankenstein.txt"
    print(get_book_text(file_path))

main()