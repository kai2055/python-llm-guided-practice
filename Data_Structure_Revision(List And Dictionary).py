

# Fundamental List Operations


def add_number(n,lst1):
    lst1.append(n)
    return lst1

lst3 = [1,2,3,4,5,0,0,0,0]
n = 6

mod_list = add_number(6, lst3)
print(mod_list)

def remove_last_element(lst1):
    
    return lst1.pop(), lst1


lst4 = remove_last_element(lst3)
print(lst4)



def sort_element(lst3):
    lst3.sort()
    return lst3


print(f"{sort_element(lst3)}")


def delete_element(lst3):
    lst3.remove(1)
    return lst3


print(f"{delete_element(lst3)}")

def slicing_list(lst3):
    return lst3[0:5]


print(f"{slicing_list(lst3)}")



# Fundamental Dictionary operations


main_dict = {"a":1, "b":2, "c":3, "d":4, "e":5}

def fun_keys(d):
    return [k for k in d.keys()]


print(f"{fun_keys(main_dict)}")


def fun_values(d):
    return list(d.values())


print(f"{fun_values(main_dict)}")


def fun_all(d):
    return list(d.items())


print(f"{fun_all(main_dict)}")



def add_key_value(d):
    d["z"] = 100
    return list(d.items())

print(f"{add_key_value(main_dict)}")


def get_evens(nums):
    return [x for x in nums if x % 2 == 0]



numb = [1,2,3,4,5,6,7,8,8]


print(f"{get_evens(numb)}")


def long_words_upper(words):
    return [word.upper() for word in words if len(word) > 3]



words = ["abc", "efgh", "ikjslkdhd"]

print(f"{long_words_upper(words)}")


students = [
    {"name": "Anna", "score": 72, "subject": "Math"},
    {"name": "Ben", "score": 45, "subject": "Science"},
    {"name": "Clara", "score": 88, "subject": "Math"},
    {"name": "David", "score": 55, "subject": "Science"},
    {"name": "Eva", "score": 39, "subject": "Math"},
    {"name": "Faraz", "score": 91, "subject": "Science"},
    {"name": "Gita", "score": 60, "subject": "Math"},
]


""" 
Write a single function called passing_by_subject that:
    - takes the list above as input
    - filters anyone who scored below 50
    - returns a dict where each key is a subject and each value is an
        alphabetically sorted list of name of student who passed in that subject


Expected output shape:

    {
    "Math": ["Anna", "Clara", "Gita"],
    "Science": ["David", "Faraz"]
    }



"""

def passing_by_subject(lst1):
    for student in students:
        if student["score"] >= 50:
            
            

        



    


