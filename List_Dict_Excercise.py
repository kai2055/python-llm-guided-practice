
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
    
            



