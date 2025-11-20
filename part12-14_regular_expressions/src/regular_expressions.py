# Write your solution here
import re

def is_dotw(my_string:str):
    if re.search(r"\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b", my_string):
        return True
    else: return False

def all_vowels(my_string:str):
    for x in my_string:
        if re.search(r"[aeiou]", x):
             continue
        else: return False
    return True

def time_of_day(my_string:str):
    pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$"
    return bool(re.match(pattern, my_string))

if __name__ == "__main__":
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))
