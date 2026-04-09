class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def display(self):
        return f"{self.user_id} - {self.name}"

    def to_file(self):
        return f"{self.user_id},{self.name}\n"

    @staticmethod
    def from_file(line):
        parts = line.strip().split(",")
        return User(parts[0], parts[1])
