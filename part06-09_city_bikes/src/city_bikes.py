# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(fn:str):
    stations = {}
    with open(fn) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(';')
            if parts[0] == 'Longitude':
                continue
            name = parts[3]
            longitude = float(parts[0])
            latitude = float(parts[1])
            stations[name]=(longitude, latitude)
        return stations

def distance(station: dict, station1:str , station2:str):
    long1, lat1 = station[station1] 
    long2, lat2 = station[station2]
    x_km = (long1 - long2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict) -> tuple:
    max_distance = 0
    station_pair = ("", "", 0.0)
    names = list(stations.keys())

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            d = distance(stations, names[i], names[j])
            if d > max_distance:
                max_distance = d
                station_pair = (names[i], names[j], d)
    
    return station_pair

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    


