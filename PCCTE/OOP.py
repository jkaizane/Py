class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.gender)

    def greet_user(self):
        print(f"Hello, {self.first_name}")


user1 = User("Jordan", "Allette", 33, "Male")
user2 = User("Sarah", "Gold", 36, "Female")
user3 = User("Ava", "Myers", 40, "Female")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
