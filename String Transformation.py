"""You are given a sentence consisting of strings of uppercase and lowercase letters. You need to transform each string based on the following rules:

The first character remains unchanged.
For each subsequent character, transform it to uppercase if the preceding character comes earlier in the alphabet, or lowercase if it comes later."""
def transformSentence(sentence):
    words = sentence.split()
    transformed_words = []
    
    for word in words:
        transformed_word = word[0]
        for i in range(1, len(word)):
            if word[i-1] < word[i]:
                transformed_word += word[i].upper()
            elif word[i-1] > word[i]:
                transformed_word += word[i].lower()
            else:
                transformed_word += word[i]
        transformed_words.append(transformed_word)
    
    return ' '.join(transformed_words)
