import ast, random, string

def Encrypt (text, sender) :
    
    hash_key = ast.literal_eval(sender.user_hash_key)
    encripted_text = ''

    
    for i in text:
        try :
            encripted_text += hash_key[i] + ' '
        except KeyError :
            letter_code = ''
            for j in range(0,random.randrange(2,100)) : letter_code += f'{random.choice(string.ascii_letters)}'
            hash_key[ i ] = letter_code
            encripted_text += letter_code + ' '

    sender.user_hash_key = hash_key
    sender.save()
    
    return encripted_text

