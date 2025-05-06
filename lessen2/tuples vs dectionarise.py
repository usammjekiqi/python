grades={
    ("john","mathe"):5,
    ("alice", "boiology"): 4,
    ("bob", "physice"): 3.5,
    ("eve", "music"): 5,
    ("john", "english"): 4,


}

print(grades[("john","mathe")])
#add a grade to bob in meth
grades[('bob'"math")]=3
print(grades)

#how tp get all the students nema
keys=list(grades.keys())
print(keys)
student, subjects=keys[0]
print(student)