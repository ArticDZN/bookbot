def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_characters(text):
    char_count = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1 
        else:
            char_count[lowered] = 1
    return char_count

def generate_report(char_count):
    char_list = []
    for char, count in char_count.items():
        char_dict = {'char': char, 'num': count}
        char_list.append(char_dict)
    
    
    def sort_on(dict):
        return dict['num']
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
