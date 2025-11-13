# Write your solution here
def smallest_average(p1:dict,p2:dict,p3:dict):
    l = [p1,p2,p3]
    r = l[0]['result1'] + p1['result2'] +p1['result3']
    low = r/3
    lowest = p1
    i = 0
    for x in l:
        total = x['result1'] + x['result2'] + x['result3']
        avg = total/3
        if avg < low:
            low = avg
            lowest = x
        i += 1
    return lowest

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 9, "result2": 9, "result3": 9}
    person2 = {"name": "Gary", "result1": 7, "result2": 7, "result3": 7}
    person3 = {"name": "Larry", "result1": 8, "result2": 8, "result3": 8}

    print(smallest_average(person1, person2, person3))
