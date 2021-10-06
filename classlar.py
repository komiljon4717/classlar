
#property -> varible
#metod    -> function

class User:
    def __init__(self, username, paswword, age):
        self.username = username
        self.paswword = paswword
        self.age = age

    def get_username(self):
        return self.username

    def get_age(self):
        return self.age


person1 = User("Ahmadjon", "941", 42)
person2 = User("Komiljon", "980", 22)

print(person1.get_username())
print(person1.get_age())






# if person1.age > person2.age:
#     print(person1.username)
# else:
#     print(person2.username)
