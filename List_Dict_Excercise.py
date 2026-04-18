
# Function tha removes duplicates from a lis while preserving the original 
# order. Do not use dict.fromkeys -- implement it manually


def unique_ordered(main_list: list[int]) -> list[int]:
    """
    Remove duplicates from the main_list

    Args:
        main_list (list[int]): List with duplicate values.

    Returns:
        list[int]: List with unique elements.


    """
    unique_list = []
    
    for i in main_list:
        if i not in unique_list:
            unique_list.append(i)

    
    return unique_list


unique = unique_ordered([3,1,2,1,3,4,2])
print(unique)



# Function that swaps keys and values. If any values are duplicated, the last key wins



def invert_dict(raw_dict: dict) -> dict:
    """
    Inverts the raw dictionary; i.e keys and values change places

    Args:
        raw_dict (dict): Initial dictionary 

    Returns:
        dict : Dictionay that has swapped key: value from the initial dictionary

    
    """

    return {v:k for k, v in raw_dict.items()}


transformed_dict = invert_dict({"x": 5, "y": 5, "z": 5})
print(transformed_dict)


# Function that groups words by their character length

def group_by_length(animals: list[str]) -> dict:
    """
    Function groups the words by their character length.

    Args: 
        diff_list (list[str]): list that contains the words

    Returns:
        dict: Dictionary where the key is the word length and the value is the words with that specific length

    
    """

    animal_dict = {}

    for animal in animals:
        if len(animal) in animal_dict:
            animal_dict[len(animal)].append(animal)
        else:
            animal_dict[len(animal)] = [animal]

    return animal_dict

animal = group_by_length(["cat","dog","elephant","ox","bee"])

print(animal)


# Function that returns elements common to two lists, with no duplicates
# sorted ascending. 

def common_list(list1: list[int], list2: list[int]) -> list[int]:
    """
    Function that retuns intersecting elements of the two list in sorted order

    Args:
        list1 (list[int]): First list 
        list2 (list[int]): Second list

    Returns:
        list: list with intersecting elements of the two lists in sorted order

    
    """

    set1, set2 = set(list1), set(list2)
    common = []

    for i in set1:
        if i in set2:
            common.append(i)


    sorted_list = sorted(common)

    return sorted_list



s = common_list([1,2,2,3,4], [2,3,3,5] )

print(s)
    

# Given a list of student dicts with name, score, subject.
# Return a dict mapping each subject to a list of passing
# students (score >= 50)


students = [
    {"name":"Anna","score":72,"subject":"Math"},
    {"name":"Ben","score":45,"subject":"Science"},
    {"name":"Clara","score":88,"subject":"Math"},
    {"name":"David","score":55,"subject":"Science"},
    {"name":"Eva","score":39,"subject":"Math"},
    {"name":"Faraz","score":91,"subject":"Science"},
    {"name":"Gita","score":60,"subject":"Math"},
]

# Output {"Math":["Anna","Clara","Gita"],"Science":["David","Faraz"]}


def pass_student_filter(students: list) -> dict:
    """
    Function that takes list of students and filters out the passed student

    Args:
        students (list): List of the students with their name, score and subject

    Returns:
        dict: dictionary containing the name of student that have passed in their respective subjects

    """

    passed_students = {}

    for student in students:
        if student["score"] >= 50:
            if student["subject"] not in passed_students:
                passed_students[student["subject"]] = []

            passed_students[student["subject"]].append(student["name"])


    return passed_students


student_names = pass_student_filter(students)

print(student_names)



# Function that takes a string and returns the word with their frequency


text = "the cat sat on the mat the cat sat"

# Output [("the",3),("cat",2)]


def top_n_words(sentence:str) -> list:
    """
    Function that takes a string and returns the word frequency

    Args:
        sentenct (str): The string with various words

    Returns:
        list: List with the words and their frequency
        
    
    """

    words = sentence.split()
    word_frequency = []
    seen = []
    

    for word in words:
        if word not in seen:
            count = 0
            for i in range(0, len(words)):
                if words[i] == word:
                    count = count + 1
            seen.append(word)
            word_frequency.append((word, count))
    return word_frequency


result = top_n_words(text)
print(result)



# Given a list of dicts with city, department, name - return a nested dict
# grouping first by city, then by department and then a list of names

employees = [
    {"city":"Berlin","dept":"Eng","name":"Zara"},
    {"city":"Berlin","dept":"Eng","name":"Alex"},
    {"city":"Berlin","dept":"HR","name":"Mia"},
    {"city":"Munich","dept":"Eng","name":"Tom"},
]

def employees_city_sorting(employees: list)-> dict:
    """
    Function that takes a list with employee information and 
    sorts them on the basis on city, department
    

    Args:
        employees: list that contains employee information
        in inner dictionary

    Returns:
        dict: dictionary with employees sorted on the basis of 
        city and department
    """

    city = {}

    for employee in employees:
        if employee["city"] not in city:
            city[employee["city"]] = {}
        
        if employee["dept"] not in city[employee["city"]]:
            city[employee["city"]][employee["dept"]] = []

        city[employee["city"]][employee["dept"]].append(employee["name"])
    
    return city



sorted_employee = employees_city_sorting(employees)

print(sorted_employee)
            







