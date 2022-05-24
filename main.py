# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

# ejena_black
def find_anagrams(first_word, second_word):
    # [assignment] Add your code here
    """This function checks if the two strings passed are anagrams"""
    
    if sorted(first_word) == sorted(second_word):
        return True
    return False

