# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self,name):
        self.__name = name
        self.__obs = []

    def __str__(self):
        return f"{self.__name}, {len(self.__obs)} observations"

    def add_observation(self,observation:str):
        self.__obs.append(observation)

    def latest_observation(self):
        if len(self.__obs) > 0:
            return self.__obs[-1]
        else: return ' '

    def number_of_observations(self):
        return len(self.__obs)

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)