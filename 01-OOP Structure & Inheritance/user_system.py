class User:
    """Represents a standard system user."""
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in.")

class Admin(User):
    """Admin user with privileges."""
    def __init__(self, username, access_level):
        super().__init__(username)
        self.access_level = access_level

    def login(self):
        """Overrides parent login to show access level."""
        print(f"{self.username} logged in with access level {self.access_level}")

    def delete_user(self, target_user):
        print(f"Admin {self.username} deleted {target_user}")

normal_user = User("Oli")
admin_user = Admin("Boss", 20)

normal_user.login()
admin_user.login()
admin_user.delete_user(normal_user.username)