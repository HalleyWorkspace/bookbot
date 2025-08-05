from stats import num_words,char_counts,list_char_counts
import sys

def get_book_text(file):
    with open(file) as f:
        return f.read()
    
def get_file():
    system_input=sys.argv
    print(len(system_input))
    if len(system_input) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    return system_input[1]

def main():
    file_path=None
    try:
        file_path=sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text=get_book_text(file_path)
        
    word_count=num_words(book_text)
    char_count_dict=char_counts(book_text)
    char_count_list=list_char_counts(char_count_dict)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in char_count_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

main()