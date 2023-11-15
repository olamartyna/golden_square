def make_snippet(string):
    # Checking if string is longer than 5 words
    string_list = string.split(' ')
    if len(string_list) > 5:
        return ' '.join(string_list[0:5]) + '...'
    else:
        return string
    