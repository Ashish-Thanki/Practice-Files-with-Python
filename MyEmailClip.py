#! python 3
# Myclip.py - This programmes is a multi-clipboard programme. That can help you automate your emails.

text = {"Agree": "Yes, I agree. That Sounds fine to me.",
        "Busy": "I am sorry but I have a few meeting this week can we do later on this week or next week?",
        "Grateful": "I would be grateful if you could respond as soon as possible.",
        "Goodbye": "Please let me know if you have any questions.\n\n Thanks \n\n Ash",
        "AL": "Thank you for you email.\n I am currently on annual leave and will respond to your email upon my return."}

import sys, pyperclip
""" 
sys.argv is the command line input, to access the text above, you need write "Myclip.py "AL" into the command line. 
Make sure your directory is in order - I had issues with mine. I suggest typing "cd [insert fil location] for
windows.
"""

if len(sys.argv) < 2:
        print("Usage: python Myclip.py [keyphrase] - copy phrase text")
        sys.exit()

keyphrase = sys.argv[1]
if keyphrase in text.keys():
        pyperclip.copy(text[keyphrase])
        print("Text for " + keyphrase + " has been copied to clipboard successfully.")

else:
        print("There is no associated text with " + keyphrase)
