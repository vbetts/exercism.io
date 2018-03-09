# This works if you need to keep the original string

def reverse(input=''):
    if input == '':
        return ''
    result = ""
    i = len(input) - 1
    for l in input:
        result += input[i]
        i-=1
    return result

# You can't reverse the string 'in place' in python because strings are immutable
# but if you could, this is a more efficient solution to the problem

#def reverse(input=''):
#    if input == '':
#        return ''
#    i = 0
#    r = (len(input)-1)/2
#    while i <= r:
#        lastIndex = len(input)-1-i
#        lastLetter = input[lastIndex]
#        input[input[lastIndex] = input[i]
#        input[i] = lastLetter
#        i+= 1
#    return input
