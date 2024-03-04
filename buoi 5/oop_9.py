class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
        
user1 = Youtube("Elshad")
user2 = Youtube("Renad")
print(user1)
print(user2)

print(f"User 1 subscribers: {user1.subscribers}")
print(f"User 1 subscriptions: {user1.subscriptions}")
print(f"User 2 subscribers: {user2.subscribers}")
print(f"User 2 subscriptions: {user2.subscriptions}")