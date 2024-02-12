class Game:
    categories = ["BOARD", "CARD", "CONSOLE", "PC"]

    def __init__(self, name, num_players, category = "BOARD"):
        self.name = name
        self.num_players = num_players
        if category.upper() in Game.categories:
            self.category = category.upper()

    def __eq__(self, other):
        if not isinstance(other, Game):
            return NotImplemented
        if self.name != other.name:
            return False
        if self.num_players != other.num_players:
            return False
        if self.category != other.category:
            return False
        return True

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((self.name, self.num_players, self.category))

    def __str__(self):
        return f"{self.name}: A {self.category.lower()} game for {self.num_players} players."

    def __repr__(self):
        return f"Game[name={self.name}, num_players={self.num_players}, category={self.category}]"

    def __format__(self, format_spec):
        return "From __format__(): " + self.__str__()

    @staticmethod
    def add_category(new_category):
        if new_category.upper() not in Game.categories:
            Game.categories.append(new_category.upper())
            return True
        return False