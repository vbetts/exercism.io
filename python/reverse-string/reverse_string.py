def reverse(input=''):
    if input == '':
        return ''
    result = ""
    i = len(input) - 1
    for l in input:
        result += input[i]
        i-=1

    return result
