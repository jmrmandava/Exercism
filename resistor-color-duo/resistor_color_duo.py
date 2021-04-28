a = {'Black': 0,
     'Brown': 1,
     'Red': 2,
     'Orange': 3,
     'Yellow': 4,
     'Green': 5,
     'Blue': 6,
     'Violet': 7,
     'Grey': 8,
     'White': 9}


def value(color):
    if color == ['brown', 'black']:
        return (a.get('Brown'+'Black'))
    if color == "white":
        return (a.get('White'))
    if color == "orange":
        return (a.get('Orange'))
