import pyinputplus as pyip
import os
from pathlib import Path
import glob, re

prompt= "What do you want to search (use regex expressions only): "
search_word = re.compile(pyip.inputRegex(prompt=prompt, regex=".*"), re.IGNORECASE)

text_files = list(Path.cwd().glob("*.txt"))
for file in text_files:
    current_txt_file = open(str(file), "r+")
    print(search_word.findall(current_txt_file.read()))
