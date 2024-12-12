def main():

    def split_str(str):
        return str.split()

    def count_words(str):
        return len(split_str(str))

    def count_characters(str):
        char_dict = {}
        formatted_str = split_str(str)

        for word in formatted_str:
            for char in word.lower():
                if char.isalpha():
                    if char in char_dict:
                        char_dict[char] += 1
                    else:
                        char_dict[char] = 1
        return char_dict

    def convert_dict(dict):
         return [{"char" :key , "num": value} for key, value in dict.items()]

    def sort_on(dict):
        return dict["num"]

    def print_report(str):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(str)} words found in the document \n")

        book_char_stats = convert_dict(count_characters(str))
        book_char_stats.sort(reverse=True, key=sort_on)
        for char in book_char_stats:
            print(f'The {char["char"]} character was found {char["num"]} times')

        print("--- End report ---")

    with open("books/frankenstein.txt") as book:
        book_content = book.read()
        print_report(book_content)

main()