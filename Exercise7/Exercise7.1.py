# File name: Exercise7.1.py
# Author: Yolanda Theodorakis
# Description: Answer the following questions.

# a. What does polymorphism (in object-oriented programming) mean? Also give a 
#    short (coding) example, e.g. google for examples).
#    - Polymorphism is applied to functions or methods. It allows us to perform 
#      a task in multiple forms or ways. The object can decide which form of 
#      the function to implement at compile-time as well as run-time. Example:
def add(x, y, z = 0):
    return x + y + z

print(add(2, 3))
print(add(2, 3, 4))

# b. What is a class variable and how are they used?
#    - A class variable is a special type of class attribute. It is declared 
#      with the static modifier of which a single copy exists. To access class 
#      variables, an object does not have to be created, for example 
#      'class_name.variable_name' works.

# c. What is an instance variable and how is it different from the class variable?
#    - Instance variables are non-static and are declared in a class outside any 
#      method, constructor or block.

# d. What is a UML sequence diagram used for? 
#    - A UML sequence diagram depicts interaction between objects in the order in 
#      which these interactions take place. Sequence diagrams are used to document 
#      and understand requirements for new and existing systems.

# e. What is a lifeline in UML sequence diagrams?
#    - A lifeline in UML sequence diagrams is a named element which depicts an 
#      individual participant in a sequence diagram. This means that each instance 
#      in a sequence diagram is represented bya lifeline.
