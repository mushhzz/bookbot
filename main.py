from stats import get_book_words, count_of_each_character, get_character_counts, sort_character_counts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def format_character_report(char_counts_dict):
    sorted_counts = sorted(char_counts_dict.items(), key=lambda x: x[1], reverse=True)
    lines = [f"{char}: {count}" for char, count in sorted_counts]
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    try:
        word_count_num = get_book_words(path)
        print("----------- Word Count ----------")
        print(f"Found {word_count_num} total words")
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    try:
        char_counts_dict = count_of_each_character(path)
        char_count_report = format_character_report(char_counts_dict)
        print("--------- Character Count -------")
        print(char_count_report)
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("============= END ===============")

main()