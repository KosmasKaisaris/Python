class User:
    pass

user_1 = User()

def function():
    pass

print("hello")

user_1.id = "001"
user_1.userName = "Kosmas"

print(user_1.userName)

class Users:
    def __init__(self,user_id,username):
        print("new user being created..")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1

user_2 = Users("001","kosmas")
user_3 = Users("001","kosmas")
print(user_3.id)


user_3.follow(user_2)
print(user_2.followers)
print(user_2.following)
print(user_3.followers)
print(user_3.following)

