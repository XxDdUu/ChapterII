def encrypt(text, size):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + size - 65) % 26 + 65)
        else:
            result += chr((ord(char) + size - 97) % 26 + 97)

    return result
text = "ascd"
size = -1
print(encrypt(text, size))