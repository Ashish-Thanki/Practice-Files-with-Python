print("Enter the English message you would like to translate to Pig Latin:")
message = input()
Vowels = ("a", "e", "i", "o", "u")
PigLatin = []
for word in message.split():
    prefixNonLetters = " "
    while len(word)>0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) ==0:
        PigLatin.append(word)
        continue

    SuffixNonLetters = " "
    while not word[-1].isalpha():
        SuffixNonLetters += word[-1]
        word = word[:-1]
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()
    prefixConsonants = " "
    while len(word)>0 and not word[0] in Vowels:
        prefixConsonants += word[0]
        word = word[1:]
    if prefixConsonants != " ":
        word +=prefixConsonants + "yay"
    else:
        word += "ay"
    if wasTitle:
        word = word.title()
    if wasUpper:
        word = word.upper()

    PigLatin.append(prefixNonLetters + word + SuffixNonLetters)
print(" ".join(PigLatin))



