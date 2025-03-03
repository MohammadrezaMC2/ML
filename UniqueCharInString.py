def is_unique_str(test_str):
    char_set = [False] * 26
    for char in test_str:
        val = ord(char)

        if char_set[val]:
            return False

        char_set[val] = True
    return True

print(is_unique_str('salam'))