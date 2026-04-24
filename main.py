class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        print(f"My name is {self.name}. I am from section {self.section}. My favorite subject is {self.favorite_subject}.")


# 1. Create at least 5 classmates
c1 = Classmate("Ana", "10-A", "Math")
c2 = Classmate("Ben", "10-A", "Science")
c3 = Classmate("Cara", "10-B", "English")
c4 = Classmate("David", "10-B", "History")
c5 = Classmate("Ella", "10-C", "Computer Science")

# 2. Store in a list
classmates = [c1, c2, c3, c4, c5]

# 3. Display all introductions using loop
print("Classmates List:\n")
for c in classmates:
    c.introduce()

# 4. Allow user to add a new classmate
print("\nAdd a new classmate:")
name = input("Enter name: ")
section = input("Enter section: ")
subject = input("Enter favorite subject: ")

new_classmate = Classmate(name, section, subject)
classmates.append(new_classmate)

# 5. Display updated list
print("\nUpdated Classmates List:\n")
for c in classmates:
    c.introduce()