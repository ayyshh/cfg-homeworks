class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()
#subclass, want to inherit methods from Student class

class Software(Student):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

software_1 = ('Ayesha', 24, '1')

    def add_subject(self, subjects):
        self.subjects.update(subjects)

    def remove_item(self, subjects):
        self.subjects.pop(subjects)

class Data(Student):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

data_2 = ('Louise', 22, '2')

def show_subjects(self):
    for subject in self.tosubjects():
        print(f"{subject}")


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)