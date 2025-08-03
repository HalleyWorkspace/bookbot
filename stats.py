def num_words(book_text):
    text_list=book_text.split()
    return len(text_list)

def char_counts(book_text):
    count_dict = {}
    for char in book_text.lower():
        if char not in count_dict.keys():
            count_dict[char]=1
        else:
            count_dict[char]+=1
    return count_dict