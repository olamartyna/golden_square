def count_words(string):
    counter = 0
    if string.isspace():
        return 0
    else:
        string_list = string.split(' ')
        for word in string_list:
            if (not word.isspace()) and (len(word) > 0):
                counter += 1                
    return counter    