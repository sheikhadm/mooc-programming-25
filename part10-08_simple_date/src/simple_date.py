# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self,day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __eq__(self,another):
        return self.day == another.day and self.month == another.month and self.year == another.year
    
    def __ne__(self,another):
        return not self.__eq__(another)
    
    def __gt__(self,another):
        if self.year == another.year:
            if self.month == another.month:
                return self.day > another.day
            else: return self.month > another.month
        return self.year > another.year
    
    def __lt__(self,another):
        if self.year == another.year:
            if self.month == another.month:
                return self.day < another.day
            else: return self.month < another.month
        return self.year < another.year
    
    def __add__(self,nm:int):
        day = self.day
        month = self.month
        year =self.year
        for x in range(nm):
            day += 1
            if day == 31:
                day = 1
                month += 1
                if month == 13:
                    month = 1
                    year += 1
        return SimpleDate(day,month,year)
    
    def __sub__(self,another):
        c = 0
        if self.year >= another.year:
            c =self.year -another.year
            c = c * 12
            c = c * 30
            d = self.month - another.month
            d = d * 30
            c = c + d
            e = self.day -another.day
            c = c + e
        return abs(c)

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
