def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)


str1 = 'hello'
str2 = 'loleh'

print(is_anagram(str1, str2))
