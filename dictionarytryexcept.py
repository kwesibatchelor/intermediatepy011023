mydict = {"name": "Kwesi", "age": 39, "ticker": "NBS"}
print(mydict)

try:
    print(mydict["lastname"])
except:
    print("Error")
    