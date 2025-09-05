# Write your solution here
def search_by_name(fn : str , word:str):
    c = {}
    d = []
    with open(fn) as new_file:
       content = new_file.read()
    entries = content.strip().split('\n\n')
    for x in entries:
        lines = x.strip().split('\n')
        if len(lines)>= 2:
            key = lines[0]
            count = int(lines[1])
            items_list = lines[2:]
            c[key] = (count,items_list)
    for recipe_name, data in c.items():
        if word.lower() in recipe_name.lower():
            d.append(recipe_name)
    return d

def search_by_time(fn : str , time:int):
    c = {}
    d = []
    with open(fn) as new_file:
       content = new_file.read()
    entries = content.strip().split('\n\n')
    for x in entries:
        lines = x.strip().split('\n')
        if len(lines)>= 2:
            key = lines[0]
            count = int(lines[1])
            items_list = lines[2:]
            c[key] = (count,items_list)
    for recipe_name, data in c.items():
        if data[0] <=  time :
            d.append(f'{recipe_name}, preparation time {data[0]} min')
    return d

def search_by_ingredient(fn : str , word:str):
    c = {}
    d = []
    with open(fn) as new_file:
       content = new_file.read()
    entries = content.strip().split('\n\n')
    for x in entries:
        lines = x.strip().split('\n')
        if len(lines)>= 2:
            key = lines[0]
            count = int(lines[1])
            items_list = lines[2:]
            c[key] = (count,items_list)
    for recipe_name, data in c.items():
        if word in data[1]:
            d.append(f'{recipe_name}, preparation time {data[0]} min')
    return d





if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt",'eggs')
    for recipe in found_recipes:
        print(recipe)

