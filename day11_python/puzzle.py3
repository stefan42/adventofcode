#!/usr/bin/python3

def is_valid_password(password):
    pw_len = len(password)
    if (pw_len < 3):
        return False
    index = 2
    row_indexes = []
    pair_indexes = []
    if (is_pair(password[0], password[1])):
        pair_indexes.append(0)
    all_chars_valid = is_valid_char(password[0]) and is_valid_char(password[1])
    while ((index < pw_len) and all_chars_valid):
        c1 = password[index-2]
        c2 = password[index-1]
        c3 = password[index]
        if (is_char_row(c1,c2,c3)):
            row_indexes.append(index)
        if (is_pair(c2,c3)):
            pair_indexes.append(index)
        all_chars_valid = all_chars_valid and is_valid_char(c3)
        index += 1
    return all_chars_valid and (len(row_indexes) > 0) and is_valid_pairs(pair_indexes)

def is_valid_pairs(pair_indexes):
    if (len(pair_indexes) < 2):
        return False
    else:
        old_index = None
        for current_index in pair_indexes:
            if old_index and old_index < (current_index-1):
                return True
            old_index = current_index
        return False

def is_valid_char(c):
    return not (c == 'i' or c == 'l' or c == 'o')

def is_char_row(c1,c2,c3):
    return ((ord(c1)+2) == (ord(c2)+1)) and ((ord(c1)+2) == ord(c3))

def is_pair(c1,c2):
    return c1 == c2

def increment_password(old_password):
    new_password = ''
    index = len(old_password) - 1
    overflow = True
    while (index >= 0):
        if (overflow):
            new_char = ''
            new_char_ord = ord(old_password[index]) + 1
            if (new_char_ord > ord('z')):
                new_char = 'a'
                overflow = True
            else:
                new_char = chr(new_char_ord)
                overflow = False
            new_password = new_char + new_password
        else:
            new_password = old_password[index] + new_password
        index -= 1
    return new_password

def main():
    password = 'hxbxwxba'
    password = increment_password(password)
    while (not is_valid_password(password)):
        password = increment_password(password)
    print('new password: ' + password)
    password = increment_password(password)
    while (not is_valid_password(password)):
        password = increment_password(password)
    print('new password: ' + password)

main()
