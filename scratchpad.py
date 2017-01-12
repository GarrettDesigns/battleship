def disemvowel(word):
    vowels = 'aeiou'
    no_vowels = list()
    for letter in word.lower():
        if letter not in vowels:
            no_vowels.append(letter)
    word = ''.join(no_vowels)
    return word

no_vowels = disemvowel("garrEttryAnkucInski")

print(no_vowels)
