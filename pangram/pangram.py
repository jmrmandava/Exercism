def is_pangram(sentence):
    a = "abcdefghijklmnopqrstuvwxyz"
    input = sentence.lower()
    for x in a:
        if x not in input:
            return False

    return True
