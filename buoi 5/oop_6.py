class Youtube:
    def __init__(self, username, subscribers):
        self.username = username
        self.subscribers = subscribers
        
        
user1 = Youtube("Elshad", 0)
print(user1.username)
print(user1.subscribers)