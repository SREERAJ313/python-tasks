def first_non_repeating_char(s):
   
    char_count = {}
    
    for char in s:
       
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None


string = "swiss"
result = first_non_repeating_char(string)
if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("No non-repeating character found.")
