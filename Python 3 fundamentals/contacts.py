contact={
    "number":3,
    "students":
    [
        {"name":"Prince raja","email":"rajaprince941@gmail.com"},
        {"name":"Harish Narayana","email":"harish1@gmail.com"},
        {"name":"Leema selvaraj","email":"Kaima@gmail.com"},
    ]
}

print("student email id's are:")
for i in range(contact["number"]):
    print(contact["students"][i]["email"])