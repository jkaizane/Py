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


class Served:
    def __init__(self, number_served, set_number_served, increment_value, login_attempts = 0):
        self.number_served = number_served
        self.set_number_served = set_number_served
        self.increment_value = increment_value
        self.login_attempts = login_attempts
        
    
    def count_number_served(self):
        print(self.number_served)
        print(self.set_number_served)

    def increment_number_served(self):
        self.number_served += self.increment_value

    def increment_login_attempts(self):
        self.login_attempts =+ 1
        print(self.login_attempts)
        
        


restaurant = Served(10, 55, 2)

restaurant.count_number_served()
restaurant.increment_number_served()
restaurant.count_number_served()
restaurant.increment_login_attempts()

