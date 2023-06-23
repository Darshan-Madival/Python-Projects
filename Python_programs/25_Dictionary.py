dictionary={
       "Darshan":"Madival",
       "Harry"  :"Top Coder",
       "List"   :[1,2,3,4,5,6]
       
}
print(dictionary["Darshan"])
print(dictionary["Harry"])
print(dictionary["List"])
dictionary["Darshan"]="Coder"
print(dictionary["Darshan"])

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())
updatedict={
    "Pratheek":"Friend",
    "sahil": "friend"
}
dictionary.update(updatedict)
print(dictionary)
print(dictionary.get("Pratheek"))
print(dictionary["Pratheek"])


