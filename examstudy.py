def get_letter_count(inp_string):
    count_dict = {}
    for char in inp_string:
        count_dict[char] = count_dict.get(char, 0) + 1
    
    return count_dict

print(get_letter_count("The quick brown fox jumps over the lazy dog"))

