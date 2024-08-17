def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dict = get_char_dict(text)
    dict_list = get_list_dict(char_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document.")
    print('')

    for char_data in dict_list:
        char = char_data['char']
        count = char_data['count']
        print(f"The '{char}' character was found {count} times")
    print("---End report---")    
    
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    char_dict = {}
    
    for i in text:
        lowered = i.lower()
        if lowered.isalpha() and lowered not in char_dict:
            char_dict[lowered] = 1
        elif lowered.isalpha():
            char_dict[lowered] += 1
    return char_dict

def sort_on(list_of_dict):
    return list_of_dict["count"]


def get_list_dict(char_dict):

    list_of_dict = []

    for k, v in char_dict.items():
        new_dict = {'char': k, 'count': v}
        list_of_dict.append(new_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict




def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()