def anagrams(str1,str2):

    a=sorted(str1.lower())
    b=sorted(str2.lower())
    if a==b :
        return "is a anagram"
    else:
        return "not a anagram"
        
a="listen"
b="silent"
print(f"{a} & {b} {anagrams(a,b)}")