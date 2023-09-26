import ast 


def Decrypt (hash_key, encripted_word) :
    hash_key = ast.literal_eval(hash_key)
    decrypt_word = ''
    for i in encripted_word.split(' ') :
        for j in range(len(hash_key.values())) : 
            if i == list(hash_key.values())[j] :
                decrypt_word += f'{list(hash_key.keys())[j]}'  
                break
    
    return decrypt_word