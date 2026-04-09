class Transaction:
    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

    def to_file(self):
        return f"{self.user_id},{self.book_id}\n"

    @staticmethod
    def from_file(line):
        parts = line.strip().split(",")
        return Transaction(parts[0], parts[1])
