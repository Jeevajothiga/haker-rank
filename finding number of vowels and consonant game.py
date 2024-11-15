def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        # Points for each substring starting at index i
        if string[i] in "AEIOU":  # Vowels for Kevin
            kevin_score += length - i
        else:  # Consonants for Stuart
            stuart_score += length - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")
