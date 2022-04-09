class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1: User = User("001", "Phillip")
user2: User = User("002", "Chrissy")

user1.follow(user2)

print(user1.followers)
print(user1.following)

user2.follow(user1)

print(user2.followers)
print(user2.following)