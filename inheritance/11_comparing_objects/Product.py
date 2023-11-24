class Product:

    def __init__(self, name, cost, retail):
        self.name = name
        self.cost = cost
        self.retail = retail

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        if self.name != other.name:
            return False
        if self.cost != other.cost:
            return False
        if self.retail != other.retail:
            return False

        return True

    def __str__(self):
        return f"{self.name} costs €{self.cost} to manufacture, but sells for €{self.retail}, at a profit of €{self.calc_profit()}"

    def __repr__(self):
        return f"Product[name={self.name}, cost={self.cost}, retail={self.retail}]"

    def calc_profit(self):
        return self.retail - self.cost