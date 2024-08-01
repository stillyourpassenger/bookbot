def read_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    text_dict = dict()
    for i in set(text):
        text_dict[i] = text.count(i)
    return text_dict

def main():
    book_path = "books/frankenstein.txt"
    text = read_book_text(book_path)
    print(count_characters(text))

main()