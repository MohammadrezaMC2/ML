
def delete_duplicate_char(string: str)->str:
    list_str = list(string)
    bool_char = [False] * 256
    for i in range(0, len(list_str)):
        val = ord(list_str[i])

        if bool_char[val]:
            list_str[i] = ''

        bool_char[val] = True

    return ''.join(list_str)



s = 'salaaaaaaaaam'
print(delete_duplicate_char(s))

