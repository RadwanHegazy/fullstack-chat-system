import string, random, ast



def Generator () :
    letters = [x for x in string.ascii_lowercase ] + [x for x in string.ascii_uppercase ] + [' '] + [x for x in string.printable]
    key = {}



    for i in range(0,len(letters)) :
        letter_code = ''
        for j in range(0,random.randrange(2,100)) : letter_code += f'{random.choice(string.ascii_letters)}'
        key[ letters[i] ] = letter_code

    key[' '] = '99'

    return key