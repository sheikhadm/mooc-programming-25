# # # Write your solution here
# import json
# players = None
# def main():
#     fn = input('File name: ')
#     with open(fn) as new_file:
#         data = new_file.read()
#     players = json.loads(data)
#     print(f'read the data of {len(players)} players')
#     # print('')
    
#     application = PlayersApplication(players)
#     application.execute()

# def print_player(player):
#     name = player['name']
#     team = player['team']
#     goals = player['goals']
#     assists = player['assists']
#     total = goals + assists

#     # name padded to 20 characters
#     return f"{name:21} {team:3} {goals:3} + {assists:3} = {total:3}"

# class PlayersApplication:
#     def __init__(self, players):
#         self.players = players

#     def help(self):
#         print("commands: ")
#         print("0 quit")
#         print("1 search for player")
#         print("2 teams")
#         print('3 countries')
#         print('4 players in team')
#         print('5 players from country')
#         print('6 most points')
#         print('7 most goals')

#         print('command: ')
        
#     def search_for_player(self):
#         player_name = input("name: ")
#         player = ''
#         for x in self.players:
#             if x['name'] == player_name:
#                 print(print_player(x))
            
    
#     def list_teams(self):
#         tasks = set([x['team'] for x in self.players])
#         if len(tasks) > 0:
#             for x in sorted(tasks):
#                 print(x)
#         else:print('no finished tasks')
    
#     def list_countries(self):
#         tasks = set([x['nationality'] for x in self.players])
#         if len(tasks) > 0:
#             for x in sorted(tasks):
#                 print(x)
#         else:print('no finished tasks')
    
#     def players_in_team(self):
#         team = input('team:')
#         tasks = [x for x in self.players if x['team'] == team]
#         if len(tasks) > 0:
#             for x in sorted(tasks, key = lambda item: item['goals'] + item['assists'], reverse = True):
#                 print(print_player(x))
#         else:print('no finished tasks')
    
#     def players_from_country(self):
#         country = input('country:')
#         tasks = [x for x in self.players if x['nationality'] == country]
#         if len(tasks) > 0:
#             for x in sorted(tasks, key = lambda item: item['goals'] + item['assists'], reverse = True):
#                 print(print_player(x))
#         else:print('no finished tasks')
    
#     def most_points(self):
#         many = input('how many: ')
#         players = sorted(self.players, key = lambda item: (item['goals'] + item['assists'], item['goals']), reverse = True)
#         for x in range(int(many)):
#             print(print_player(players[x]))
        
#     def most_goals(self):
#         many = input('how many: ')
#         players = sorted(self.players, key = lambda item: (item['goals'], -item['games']) , reverse = True)
#         for x in range(int(many)):
#             print(print_player(players[x]))
    

        
    
#     def execute(self):
#         self.help()
        
#         while True:
#             print("")
#             command = input("command: ")
#             if command == "0":
#                 break
#             elif command == "1":
#                 self.search_for_player()
#             elif command == "2":
#                 self.list_teams()
#             elif command == '3':
#                 self.list_countries()
#             elif command == '4':
#                 self.players_in_team()
#             elif command == '5':
#                 self.players_from_country()
#             elif command == '6':
#                 self.most_points()
#             elif command == '7':
#                 self.most_goals()
#             else:
#                 self.help()



        
# main()





import json

# ---- Helper function for consistent formatting ----

def format_player(p):
    name = p['name'].strip()
    team = p['team']
    goals = p['goals']
    assists = p['assists']
    total = goals + assists

    return (
        f"{name:<21}"
        f"{team:>3}"
        f"{goals:>4}"
        f" +"
        f"{assists:>3}"
        f" ="
        f"{total:>4}"
    )


# ---- Main program ----

def main():
    filename = input("file name: ")
    try:
        with open(filename) as f:
            data = json.load(f)
    except:
        print("Invalid file")
        return

    print(f"read the data of {len(data)} players\n")

    print("commands:")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")
    print()

    while True:
        cmd = input("command: ")

        # ---- Quit ----
        if cmd == "0":
            break

        # ---- Search for a player ----
        elif cmd == "1":
            name = input("name: ")
            for p in data:
                if p["name"] == name:
                    print()
                    print(format_player(p))
                    break
            print()

        # ---- List teams ----
        elif cmd == "2":
            teams = sorted({p["team"] for p in data})
            for t in teams:
                print(t)
            print()

        # ---- List countries ----
        elif cmd == "3":
            countries = sorted({p["nationality"] for p in data})
            for c in countries:
                print(c)
            print()

        # ---- Players in a team by points ----
        elif cmd == "4":
            team = input("team: ")
            print()
            players = [p for p in data if p["team"] == team]
            players.sort(key=lambda p: (p["goals"] + p["assists"], p["goals"]), reverse=True)
            for p in players:
                print(format_player(p))
            print()

        # ---- Players from a country by points ----
        elif cmd == "5":
            country = input("country: ")
            print()
            players = [p for p in data if p["nationality"] == country]
            players.sort(key=lambda p: (p["goals"] + p["assists"], p["goals"]), reverse=True)
            for p in players:
                print(format_player(p))
            print()

        # ---- Players with most points ----
        elif cmd == "6":
            n = int(input("how many: "))
            print()
            players = sorted(
                data,
                key=lambda p: (p["goals"] + p["assists"], p["goals"]),
                reverse=True
            )
            for p in players[:n]:
                print(format_player(p))
            print()

        # ---- Players with most goals ----
        elif cmd == "7":
            n = int(input("how many: "))
            print()
            players = sorted(
                data,
                key=lambda p: (p["goals"], -p["games"]),
                reverse=True
            )
            for p in players[:n]:
                print(format_player(p))
            print()

        else:
            print("unknown command\n")


main()
