class student:
    # class Variable
    Class ="MCA"

pr=student()
Is=student()

# intance Variable Of Class
pr.id=1001
pr.name="Prateek"

Is.id=1001
Is.name="Ishika"

print(Is.name)
print(Is.Class)

print(student.Class)

print(pr.Class)
print(Is.__dict__)

# We Can Change The Class Variable For Paticular object
# Mainly Class variable And It's Value Is Not Changable
Is.Class="Mca"
print(Is.Class)

# object_Name.__dict__ : it retune the dictionary which is All Tha Object Variable with It's Value
print(Is.__dict__)
print(student.Class)

# if We Want To change the class variable and it's Value wich is predefine in a class then we can only one with the class name exp.
student.Class="MMCA"

print(pr.Class)