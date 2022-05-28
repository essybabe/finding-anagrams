# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


from ast import If


def find_anagrams(str1, str2):
    print(sorted(str1),sorted(str2))
    return sorted(str1)==sorted(str2)
    # [assignment] Add your code here

find_anagrams("racecar","carrace")
print(find_anagrams("racecar","racecar"))

find_anagrams("listen","silent")
print(find_anagrams("listen","silent"))

