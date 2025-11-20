# # Write your solution here
import json
players = None
def main():
    fn = input('File name: ')
    with open(fn) as new_file:
        data = new_file.read()
    players = json.loads(data)
    print(f'read the data of {len(players)} players')
    # print('')
    
    application = PlayersApplication(players)
    application.execute()

def print_player(player):
    name = player['name']
    team = player['team']
    goals = player['goals']
    assists = player['assists']
    total = goals + assists

    # name padded to 20 characters
    return f"{name:21} {team:3} {goals:3} + {assists:3} = {total:3}"

class PlayersApplication:
    def __init__(self, players):
        self.players = players

    def help(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print('3 countries')
        print('4 players in team')
        print('5 players from country')
        print('6 most points')
        print('7 most goals')

        print('command: ')
        
    def search_for_player(self):
        player_name = input("name: ")
        player = ''
        for x in self.players:
            if x['name'] == player_name:
                print(print_player(x))
            
    
    def list_teams(self):
        tasks = set([x['team'] for x in self.players])
        if len(tasks) > 0:
            for x in sorted(tasks):
                print(x)
        else:print('no finished tasks')
    
    def list_countries(self):
        tasks = set([x['nationality'] for x in self.players])
        if len(tasks) > 0:
            for x in sorted(tasks):
                print(x)
        else:print('no finished tasks')
    
    def players_in_team(self):
        team = input('team:')
        tasks = [x for x in self.players if x['team'] == team]
        if len(tasks) > 0:
            for x in sorted(tasks, key = lambda item: item['goals'] + item['assists'], reverse = True):
                print(print_player(x))
        else:print('no finished tasks')
    
    def players_from_country(self):
        country = input('country:')
        tasks = [x for x in self.players if x['nationality'] == country]
        if len(tasks) > 0:
            for x in sorted(tasks, key = lambda item: item['goals'] + item['assists'], reverse = True):
                print(print_player(x))
        else:print('no finished tasks')
    
    def most_points(self):
        many = input('how many: ')
        players = sorted(self.players, key = lambda item: (item['goals'] + item['assists'], item['goals']), reverse = True)
        for x in range(int(many)):
            print(print_player(players[x]))
        
    def most_goals(self):
        many = input('how many: ')
        players = sorted(self.players, key = lambda item: (item['goals'], -item['games']) , reverse = True)
        for x in range(int(many)):
            print(print_player(players[x]))
    

        
    
    def execute(self):
        self.help()
        
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_for_player()
            elif command == "2":
                self.list_teams()
            elif command == '3':
                self.list_countries()
            elif command == '4':
                self.players_in_team()
            elif command == '5':
                self.players_from_country()
            elif command == '6':
                self.most_points()
            elif command == '7':
                self.most_goals()
            else:
                self.help()



        
main()





# # Write your solution here
# # If you use the classes made in the previous exercise, copy them here
# class Task:
#     id = 0
#     def __init__(self,description,name,load):
#         self.description = description
#         self.programmer = name
#         self.workload = load
#         self.finished = False
#         Task.id += 1
#         self.id = Task.id
    
#     def __str__(self):
#         return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.finished else 'NOT FINISHED'}'
    
#     def is_finished(self):
#         return self.finished
    
#     def mark_finished(self):
#         self.finished = True
    
# class OrderBook:
#     def __init__(self):
#         self.orders = []
    
#     def add_order(self,description,name,load):
#         new_order = Task(description,name,load)
#         self.orders.append(new_order)
    
#     def all_orders(self):
#         return self.orders
    
#     def programmers(self):
#         return set([x.programmer for x in self.orders])

#     def mark_finished(self,id:int):
#         c = False
#         for x in self.orders:
#             if x.id == id:
#                 c = True
#                 x.mark_finished()
#                 print('marked as finished')
#                 return c
#         return c
    
#     def finished_orders(self):
#         return [x for x in self.orders if x.is_finished() == True]
#     def unfinished_orders(self):
#         return [x for x in self.orders if x.is_finished() == False]

#     def status_of_programmer(self,programmer:str):
#         finished_task = 0
#         unfinished_task = 0
#         finished_workload = 0
#         unfinished_workload = 0
#         c = False
#         for x in self.orders:
#             if x.programmer == programmer:
#                 if x.is_finished() == True:
#                     c == True
#                     finished_task += 1
#                     finished_workload += int(x.workload)
#                 elif x.is_finished() == False:
#                     c = True
#                     unfinished_task += 1
#                     unfinished_workload += int(x.workload)
#         if c == False:
#             return False
#         return (finished_task,unfinished_task,finished_workload,unfinished_workload)


        
        
    
   

#     
    
#     def list_unfinished_tasks(self):
#         tasks = self.__orderbook.unfinished_orders()
#         if len(tasks) > 0:
#             for x in tasks:
#                 print(x)
#         else:print('no unfinished tasks')
    
#     def mark_task(self):
#         try:
#             i = int(input('id:') )
#             c = self.__orderbook.mark_finished(i)
#             if c == False:
#                 print('erroneous input')
    
#         except  ValueError:
#             print('erroneous input')
        
        
#     def programmers(self):
#         tasks = self.__orderbook.programmers()
#         if len(tasks) > 0:
#             for x in tasks:
#                 print(x)
#         else:print('no programmers')
    
#     def status_of_programmer(self):
#         name = input('programmer: ')
#         status = self.__orderbook.status_of_programmer(name)
#         if status == False:
#             print('erroneous input')
#         else:
#             print(f'tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}')
    


#     def execute(self):
#         self.help()
#         while True:
#             print("")
#             command = input("command: ")
#             if command == "0":
#                 break
#             elif command == "1":
#                 self.add_order()
#             elif command == "2":
#                 self.list_finished_tasks()
#             elif command == '3':
#                 self.list_unfinished_tasks()
#             elif command == '4':
#                 self.mark_task()
#             elif command == '5':
#                 self.programmers()
#             elif command == '6':
#                 self.status_of_programmer()
#             else:
#                 self.help()


# # when testing, no code should be outside application except the following:
# application = OrderBookApplication()
# application.execute()
