list_1=[{
    "name":"Kanat",
    "last_name":"Erbol",
    "Age":20
},
{
    "name":"Askar",
    "last_name":"Erzhanov",
    "Age":15
},
{
    "name":"Kairat",
    "last_name":"Zhandosov",
    "Age":45
}
]
total=0
for person in list_1:
  total += person["Age"]
 
count =len(list_1)
Age = total/count
print(Age)