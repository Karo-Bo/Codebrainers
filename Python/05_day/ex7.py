

def smorse(text):
    translations = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
    }
    encoded = ""
    for c in text:
        encoded += translations[c]
    return encoded

def test_morse_code():
    assert smorse("sos") == "...---..."
    assert smorse("daily") == "-...-...-..-.--"
    assert smorse("programmer") == ".--..-.-----..-..-----..-."
    assert smorse("bits") == "-.....-..."
    assert smorse("three") == "-.....-..."