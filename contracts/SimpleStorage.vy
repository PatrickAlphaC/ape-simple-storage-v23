# SPDX-License-Identifier: MIT
# @version ^0.3.7

my_favorite_number: uint256

struct Person:
    favorite_number: uint256
    name: String[100]

# Dynamic Array/List
list_of_people: DynArray[Person, 5]

# list_of_people: public(Person[5])
# list_of_people_index: uint256

name_to_favorite_number: HashMap[String[100], uint256]

@external
def store(_favorite_number: uint256):
    self.my_favorite_number = _favorite_number

@external
@view
def retrieve() -> uint256:
    return self.my_favorite_number

@external
def add_person(name: String[100], favorite_number: uint256):
    new_person: Person = Person({favorite_number: favorite_number, name: name})
    # self.list_of_people[self.list_of_people_index] = new_person
    # self.list_of_people_index += 1
    self.list_of_people.append(new_person)

    self.name_to_favorite_number[name] = favorite_number
