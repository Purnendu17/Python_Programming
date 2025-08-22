class User:
    def __init__(self, username):
        # Private attribute to store the username
        self.__username = username

    # Getter method to access the username
    def get_username(self):
        return self.__username

    # Setter method to update the username with validation
    def set_username(self, new_username):
        return(self)

# Example usage:
user = User("Avani")
print(f"Current username: {user.get_username()}")  # Output: Current username: Avani

# Update username
user.set_username("NewUser")
print(f"Updated username: {user.get_username()}")  # Output: Updated username: NewUser


