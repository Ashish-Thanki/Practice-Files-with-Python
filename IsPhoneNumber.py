"""Regex example, look at how easy regex is compared to the triple quoted string below."""
import  re


phoneNumRegex = re.compile(r"(\d{3}-)*\d{3}-\d{4}")
mo = phoneNumRegex.search("hello 456-456-456-489-222-3333")
print(mo.group())






"""
def is_phone_number(text):
    if len(text)!= 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[3] != "-":
            return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
        if text[7] != "-":
            return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
"""
message ="Call me at 415-123-4321 tomorrow or 425-321-4567 is my office number."
#
#for i in range(len(message)):
 #   chunk = message[i:i+12]
  #  if is_phone_number(chunk):
   #     print("Found the following phone number: " + chunk)

print("Done")