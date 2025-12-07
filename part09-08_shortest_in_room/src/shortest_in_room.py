# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self,person: Person):
        if person in self.persons:
            pass
        else: 
            self.persons.append(person)
    
    def is_empty(self):
       return False  if len(self.persons) > 0 else True
    
    def print_contents(self):
        for x in self.persons:
            print(f'{x.name} ({x.height})')
    
    def shortest(self):
        
        if self.is_empty():
            return None
        else:
            short = self.persons[0]
            for x in self.persons:
                if x.height <= short.height:
                    short = x
            return short

    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            short = self.shortest()
            per = [n for n in self.persons if n.name != short.name]
            for n in self.persons:
                 if n.name == short.name:
                    self.persons = per
                    return n
        


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
        