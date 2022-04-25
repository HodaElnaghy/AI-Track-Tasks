dict1= {
    "name":"Doja",
    "age":53
}
dict2 = {
    "job": "Teacher"
}

#Method 1
Merged1={**dict1,**dict2}
print(Merged1)

#method 2

Merged2 ={key : value for dict in (dict1,dict2) for key , value in dict.items()}
print(Merged2)

#method 3
Merged3= dict1.copy()
Merged3.update(dict2)
print(Merged3)

#method 4
Merged4= dict1 | dict2
print(Merged4)
