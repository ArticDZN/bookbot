from stats import get_book_text, count_characters, generate_report
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
def main():
    text = get_book_text(book_path)
    word_count = len(text.split())
    char_counts = count_characters(text)
    sorted_chars = generate_report(char_counts)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
   
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():  
            print(f"{char}: {count}")
    
    print("============= END ===============")
    
main()