marks={
    "Maths":100,
    "English":99,
    "Science":98,
    "Hindi":97,
    "Computer":96
}
print(marks.items())
# key value pairs are changed into tuples
print(marks.keys())
# keys are printed with this method
print(marks.values())
# values are printed with this method
marks.update ({"Maths":99}) 
print(marks)
# it is used to change the value of a key
# a new key is changed because dictionaries are immutable
print(marks.get("Maths3")) # prints none
# print(marks["Maths3"]) # prints error because of wrong brackets
