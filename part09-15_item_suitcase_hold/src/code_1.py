# Write your solution here:
class Item:
    def __init__(self,name,weight):
        self.__name = name
        self.__weight = weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    

    def name(self):
        return self.__name

    
    def weight(self):
        return self.__weight

class Suitcase():
    def __init__(self,max_w):
        self.max_w = max_w
        self.items = []

    def add_item(self,item:Item):
        total = sum(item.weight() for item in self.items)
        tot = total + item.weight()
        if tot <= self.max_w:
            self.items.append(item)

    
    def __str__(self):
        
        return f"{len(self.items)} {'item' if len(self.items) == 1 else 'items'} ({sum(item.weight() for item in self.items)} kg)"
    
    def print_items(self):
        for x in self.items:
            print(x)
    
    def heaviest_item(self):
        if not self.items:  # suitcase is empty
            return None
        return max(self.items, key=lambda item: item.weight())
    
    def weight(self):
        return sum(item.weight() for item in self.items)

class CargoHold:
    def __init__(self,max_w:int):
        self.max_w = max_w
        self.items = []

    def add_suitcase(self,suit:Suitcase):
        total = sum(item.weight() for item in self.items)
        tot = total + suit.weight()
        if tot <= self.max_w:
            self.items.append(suit)

    



    def __str__(self):
        return f"{len(self.items)} {'suitcase' if len(self.items) == 1 else 'suitcases'}, space for {self.max_w - sum(item.weight() for item in self.items) } kg"

    def print_items(self):
        for x in self.items:
            x.print_items()



if __name__ == "__main__":
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    suitcase.heaviest_item()
        