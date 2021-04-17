def is_pangram(sentence):
    a = "abcdefghijklmnopqrstuvwxyz"
    for x in a:
        if x not in sentence.lower():
            return False

    return True
