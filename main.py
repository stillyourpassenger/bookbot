def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)
    
def print_report(book_path):
    text = read_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    
    number_of_words = count_words(text)
    print(f"{number_of_words} words found in the document\n")
    
    characters_counted = count_characters(text)
    sorted_dict = dict(sorted(characters_counted.items(), key=lambda x:x[1], reverse=True))
    for k in sorted_dict.keys():
        print(f"The {k} character was found {sorted_dict[k]} times")
    
    print("--- End report ---")

def read_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    text_dict = dict()
    for i in set(text):
        if i.isalpha():
            text_dict[i] = text.count(i)
    return text_dict


main()