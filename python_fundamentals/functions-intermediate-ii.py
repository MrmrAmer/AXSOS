x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)

students = [
{'first_name': 'Michael', 'last_name': 'Jordan'},
{'first_name': 'John', 'last_name': 'Rosales'},
{'first_name': 'Mark', 'last_name': 'Guillen'},
{'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(some_list):
    for dictionary in some_list:
        # for key, value in dictionary.items():
        # print(key, "-", value, end="\n")
        print(f"First name: {dictionary["first_name"]} - Last name: {dictionary["last_name"]}")
    print("***********")
            

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC',
'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh',
'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key.upper())
        for i in value:
            print(i)

printInfo(dojo)