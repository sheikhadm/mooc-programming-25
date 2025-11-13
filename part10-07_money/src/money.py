# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        # Normalize total cents so we always store consistent values
        total_cents = euros * 100 + cents
        self.__euros = total_cents // 100
        self.__cents = total_cents % 100

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __ne__(self, another):
        return not self.__eq__(another)

    def __lt__(self, another):
        if self.__euros == another.__euros:
            return self.__cents < another.__cents
        return self.__euros < another.__euros

    def __gt__(self, another):
        if self.__euros == another.__euros:
            return self.__cents > another.__cents
        return self.__euros > another.__euros

    def __add__(self, another):
        euros = self.__euros + another.__euros
        cents = self.__cents + another.__cents
        if cents >= 100:
            euros += cents // 100
            cents = cents % 100
        return Money(euros, cents)

    def __sub__(self, another):
        total_self = self.__euros * 100 + self.__cents
        total_other = another.__euros * 100 + another.__cents
        if total_self < total_other:
            raise ValueError("A Money object cannot have a negative value.")
        diff = total_self - total_other
        euros = diff // 100
        cents = diff % 100
        return Money(euros, cents)


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)
    e3 = e1 + e2
    e4 = e1 - e2

    print(e1)
    print(e2)
    print(e3)
    print(e4)

    # Try the "cheat"
    e1.euros = 1000  # creates a *new* public attribute, doesn’t affect internal state
    print(e1)  # still prints correctly as 4.05 eur
