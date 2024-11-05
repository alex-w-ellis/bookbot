def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = character_count(text)
    org_chars = character_list(characters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    org_chars.sort(reverse=True, key=sort_on)
    for char_dict in org_chars:
        char = char_dict['char']
        num = char_dict['num']
        if char.isalpha():
            print(f"the '{char}' chracter was found {num} times")
    print("--- End of report ---")


def sort_on(dict):
    return dict["num"]

def character_list(characters):
    char_list=[]
    for letter, count in characters.items():
        char_list.append({"char": letter, "num": count})
    return char_list

def character_count(text):
    characters = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return(characters)
 
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
