import pyinputplus
#x = pyinputplus.inputNum("Input a Number: ", limit=3)
#print(x)

#y = pyinputplus.inputNum("Input a number, this is a timeout: ", timeout=10, default="Timeout")
#print(y)

#r = pyinputplus.inputNum("Input Your Roman Numeral or Integers in 10 seconds: ", allowRegexes=[r"(I|V|W|L|C|D|M|X)+", r"zero"])
#print(r)

def addsuptoten(numbers):
    numberList = list(numbers)
    for i, integer in enumerate(numberList):
        numberList[i] = int(integer)
    if sum(numberList) != 10:
        raise Exception("the numbers must add upto to 10, not %s." % (sum(numberList)))
    return int(numbers)


response = pyinputplus.inputCustom(addsuptoten)
print(response)