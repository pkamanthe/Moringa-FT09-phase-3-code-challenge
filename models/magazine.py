class Magazine:
    def __init__(self, id, name, category):
        """
        Initialize a magazine.

        :param id: The ID of the magazine.
        :param name: The name of the magazine.
        :param category: The category of the magazine (e.g., Technology, Fashion).
        """
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'
