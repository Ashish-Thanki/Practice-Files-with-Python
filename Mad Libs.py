import pyinputplus as pyip
# This is great introduction to what open, write and close does. It creates a .txt file your working directory.
Adjective = pyip.inputStr("Enter an adjective:\n")
Noun1 = pyip.inputStr("Enter an Noun:\n")
Verb = pyip.inputStr("Enter an Verb:\n")
Noun2 = pyip.inputStr("Enter an Noun:\n")

text = ("This %s panda walked to the %s and then %s. A nearby %s was unaffected by these events."
        % (Adjective, Noun1, Verb, Noun2))

print(text)
text_file = open(f'text_file.txt', 'w')
text_file.write(text)
text_file.close()