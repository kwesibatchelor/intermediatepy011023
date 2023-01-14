mydict = {"name": "Kwesi", "age": 39, "ticker": "NBS"}
mydict2 = dict(name="K",  age=40, city="Tampa")

#"merges dictionary"

mydict.update(mydict2)
print(mydict)