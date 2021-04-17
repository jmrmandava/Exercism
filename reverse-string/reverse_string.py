def test_an_empty_string():
    return ""[::-1]


def test_a_word():
    return "hola"[::-1]


def test_a_capitalized_word():
    return "Rare"[::-1]


def test_a_sentence_with_punctuation():
    return "hey, how ya doing?"[::-1]


def test_a_palindrome():
    return "dad"[::-1]


def test_an_even_sized_word():
    return "laptop"[::-1]
