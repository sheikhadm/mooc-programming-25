# Write your solution here:
class Series():
    def __init__(self,name:str,seas:int,genre:list):
        self.title = name
        self.seas = seas
        self.genre = genre
        self.rating = 0
        self.total = 0

    def __str__(self):
        if self.rating == 0:
            return f"{self.title} ({self.seas} seasons)\ngenres: {', '.join(self.genre)}\nno ratings"
        average = self.total / self.rating
        return f"{self.title} ({self.seas} seasons)\ngenres: {', '.join(self.genre)}\n{self.rating} ratings, average {average:.1f} points"

    def rate(self,number:int):
        self.rating += 1
        self.total += number

def minimum_grade(rat:float,s:list):
    c = []
    for x in s:
        d = x.total/x.rating
        if d >= rat:
            c.append(x)
    return c

def includes_genre(g:str,s:list):
    c= []
    for x in s:
        if g in x.genre:
            c.append(x)
    return c

if __name__ == "__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

