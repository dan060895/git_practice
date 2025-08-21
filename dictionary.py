class UserManager:
    def __init__(self):
        self.users = []  # lista de diccionarios {"id": int, "name": str}

    def add_user(self, user_id, name):
        # BUG 1: no valida usuarios repetidos
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        # BUG 2: devuelve solo el último encontrado si hay duplicados
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  # si no existe regresa None (ok), pero no debería permitir duplicados

    def delete_user(self, user_id):
        # BUG 3: borra solo la primera coincidencia
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  # si había más duplicados, quedan vivos

    def get_all_names(self):
        # BUG 4: error lógico, devuelve IDs en lugar de nombres
        return [u["id"] for u in self.users]

    def average_user_id(self):
        # BUG 5: si la lista está vacía, ZeroDivisionError
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    manager = UserManager()

    manager.add_user(1, "Alice")
    manager.add_user(2, "Bob")
    manager.add_user(2, "Charlie")  

    print("Buscar ID=2:", manager.find_user(2))  
    print("Usuarios antes de borrar:", manager.users)

    manager.delete_user(2)  
    print("Usuarios después de borrar ID=2:", manager.users)

    print("Lista de nombres:", manager.get_all_names())  
    print("Promedio de IDs:", manager.average_user_id())  
