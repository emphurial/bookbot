def main():
    with open("books/frankenstein.txt") as f:
        book_contents = f.read()
    print(book_contents)
    

def num_of_words():
    with open("books/frankenstein.txt") as f:
        book_words = f.read()
        word_amount = book_words.split()
        word_counter = len(word_amount)    
    print(f"{word_counter} words in the provided text")

def num_of_letters():
    with open("books/frankenstein.txt") as f:
        book_words = f.read()
        book_words = book_words.lower()
        letters = {}
        for i in book_words:
            if i.isalpha():
                if i not in letters:
                    letters[i] = 1
                else:
                    letters[i] += 1
        processed_letters = sorted(letters.items(), key=lambda x:x[1], reverse = 1)
        for i in processed_letters:
            print(f"The letter '{i[0]}' was found {i[1]} times")

            





if __name__ == "__main__":
    main()
    num_of_words()
    num_of_letters()