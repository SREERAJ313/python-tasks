def valid(a):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    special_characters = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'}
    
    in_vowels=False
    in_consonants=False
    for j in special_characters:
        if j in a.lower():
            return False
             
    for i in vowels: 
        if i in a.lower():
            in_vowels= True 
        elif i.isalnum():
            in_consonants=True

    if in_vowels and in_consonants:
            return True
    return False

a=valid("234Adas")
print("valid is:",a)