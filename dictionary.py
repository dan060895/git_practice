class UserManager:
    def __init__(self):
        self.users = [] 

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]


if __name__ == "__main__":
    manager = UserManager()

    manager.add_user(1, "Alice")
    manager.add_user(2, "Bob")
    manager.add_user(2, "Charlie")  

    print("Search ID=2:", manager.find_user(2))  
    print("Users before deletion:", manager.users)

    manager.delete_user(2)  
    print("Users after deletion ID=2:", manager.users)

    print("List of names", manager.get_all_names())  
