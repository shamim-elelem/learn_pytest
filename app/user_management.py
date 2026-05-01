class User:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age can not be negative")
        self.name = name 
        self.age = age 


def is_adult(user):
    return user.age >= 18
