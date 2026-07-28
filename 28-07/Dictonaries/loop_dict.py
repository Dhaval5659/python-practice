mydict = {
 "name": "meet",
 "class": 10,
 "roll number": 25
}
 # only KEY
for x in mydict:
 print(x)

for x in mydict.keys():
 print(x)

# only VALUE
for x in mydict:
 print(mydict[x])

# KEY : VALUE
for x, y in mydict.items():
 print(x, y)

# Copy

thisdict = mydict.copy()
print(thisdict)

thisdict = dict(mydict)
print(thisdict)

# nested 

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
print(myfamily["child2"]["year"])
print(myfamily["child1"])