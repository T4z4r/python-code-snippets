str1="listen"
str2="silent"


str1=str1.replace(" ","").upper()
str2=str2.replace(" ","").upper()

if sorted(str1)==sorted(str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")





