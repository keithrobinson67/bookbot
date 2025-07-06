def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    chars = {}
    for c in text:
        if c.lower() in chars:
            chars[c.lower()] += 1
        else: 
            chars[c.lower()] = 1
    return chars

def sort_on(items):
    return items["count"]

def sorted_chars(chars):
    char_list = []
    for c in chars:
        char_list.append({"char": c, "count": chars[c]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    


