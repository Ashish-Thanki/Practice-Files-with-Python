import pyinputplus as pyip
import time, random

NumberofQuestions = 10
NumberofCorrect = 0

for question in range(NumberofQuestions):
    num1 = random.randrange(0, 10)
    num2 = random.randrange(0, 10)
    prompt = "What is {} x {}? ".format(num1, num2)
    try:
       pyip.inputInt(prompt, allowRegexes=["^{}$".format(num1*num2)], blockRegexes=[("^.*$", "That is Incorrect!")],
                     timeout=10, limit=3)
       print("Correct")
       time.sleep(1)
       NumberofCorrect += 1
    except pyip.TimeoutException:
        print("Out of Time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
print("{}/{}".format(NumberofCorrect, NumberofQuestions))
