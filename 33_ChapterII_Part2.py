def Palindrom(text):
    correct_matches = 0
    text = text.lower()
    for i in range(len(text)):

        if (text[i] == text[-1-i]):
            correct_matches += 1
    if correct_matches == len(text):
        print(text, "is palindrom.")
    else:
        print(text, "is not.")

Palindrom("huuh")
