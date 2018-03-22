import re

def verify(isbn):
    isbn = isbn.strip().replace("-", "").replace(" ", "").lower()
    #check if the string is empty, not the right length, or contains an invalid character
    if (isbn=="") or not(len(isbn)==10) or not(re.match("^[0-9]{9}[0-9xX]$",isbn)):
        return False
    i = 0
    total = 0
    for x in range(len(isbn), 0, -1):
        if isbn[i] == "x" or isbn[i] == "X":
            y = 10
        else:
            y = int(isbn[i])
        total+=y*x
        i+=1
    return (total%11 ==0)
