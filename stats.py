def get_book_words(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    book_words = file_contents.split()
    return len(book_words)

def count_of_each_character(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read().lower()
    char_counts = {char: file_contents.count(char) for char in set(file_contents) if char.isalpha()}
    return char_counts

def get_character_counts(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_character_counts(char_counts_dict):
    filtered = {k: v for k, v in char_counts_dict.items() if k.isalpha()}
    list_of_dicts = [{"char": char, "num": count} for char, count in filtered.items()]
    def get_num(item):
        return item["num"]
    list_of_dicts.sort(key=get_num, reverse=True)
    return list_of_dicts

