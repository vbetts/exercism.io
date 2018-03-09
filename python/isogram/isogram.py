def is_isogram(string):
    string = string.replace(' ', '').replace('-', '').lower()
    letterSet = set()
    for s in string:
        if s in letterSet:
            return False
        else:
            letterSet.add(s)

    return True
