def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document.")

def word_count(text):
    words = text.split()
    return len(words)




def get_book_text(path):
    with open(path) as f:
        return f.read()
    



main()