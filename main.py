def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document.")
    char_dict = get_char_dict(text)
    print(f"Number of times each character appears in the text: {char_dict}")
    



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



def get_book_text(path):
    with open(path) as f:
        return f.read()
    



main()