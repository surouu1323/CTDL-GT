class Youtube:
    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers
        
user1 = Youtube("Elshad")
print(user1.username)
print(user1.subscribers)
user2 = Youtube("Renad")
print(user2.username)
print(user2.subscribers)