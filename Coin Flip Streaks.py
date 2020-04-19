""" Assesses the probability of 6 streaks in a row out of 10,000 coil flips. Doing the python wasn't difficult, and
i am sure i can add user inputs as well but a simple 0.5 **6 is a lot simpler to me."""

import random

StreaksCount = 0
ExperimentCount = 0
Total_Experiments = 10000
results = ""
while ExperimentCount < Total_Experiments:
    results += str(random.choice("H" "T"))
    ExperimentCount += 1

for result in results:
    if (result*6) == ("H"*6) or (result*6) == ("T"*6):
        StreaksCount +=1

print("Chance of streak: %s%%" % (StreaksCount/Total_Experiments))



