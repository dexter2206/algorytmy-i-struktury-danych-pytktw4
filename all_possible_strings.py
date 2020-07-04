def all_possible_strings(chars, length):
    if length == 1:
        for char in chars:
            yield char
        return
    #return [
    #   char + word for char in chars for word in all_possible_strings(chars, length-1)
    #]

    for char in chars:
        for word in all_possible_strings(chars, length-1):
            yield char + word



if __name__ == '__main__':
#    for word in all_possible_strings(["a", "b", "c"], 4):
#        print(word)

    strings = iter(all_possible_strings(["a", "b", "c"], 4))
    for _ in range(3):
        print(next(strings))
