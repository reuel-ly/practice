def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    sample = ""
    for i in range(len(string_)):
        if string_[i] not in vowels:
            sample += string_[i]
    string_ = sample
    return string_