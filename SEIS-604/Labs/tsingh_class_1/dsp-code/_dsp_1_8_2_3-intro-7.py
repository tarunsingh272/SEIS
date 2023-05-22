# _dsp-1_8_2_3-intro-7.py

capitals = {"Iowa": "Des Moines", "Wisconsin": "Madison"}
print(capitals["Iowa"])
capitals["Utah"] = "Salt Lake City"
print(capitals)
capitals["California"] = "Sacramento"
print(len(capitals))
for k in capitals:
    print(capitals[k],"is the capital of", k)
