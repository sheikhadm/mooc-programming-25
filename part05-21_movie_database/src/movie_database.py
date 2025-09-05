# Write your solution here
def add_movie(database: list, name:str, director: str, year:int, runtime:int):
    c= {}
    c['name'] = name
    c['director'] = director
    c['year'] = year
    c['runtime'] = runtime
    database.append(c)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)
