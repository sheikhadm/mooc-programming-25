# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) >len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else : return 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        a = 0
        b = 0
        for x in player1_word:
            if x in 'aeiou':
                a += 1
        for x in player2_word:
            if x in 'aeiou':
                b += 1
        if a > b:
            return 1
        elif b > a:
            return 2
        else : return 0

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self,player1_word:str ,player2_word:str):
        c = ['rock','paper','scissors']
        p1 = player1_word.lower()
        p2 = player2_word.lower()
        if player1_word.lower() not in c and player2_word.lower() not in c:
            return 0
        elif player1_word.lower() in c and player2_word.lower() in c:
            beats = {
                'rock': 'scissors',
                'scissors': 'paper',
                'paper': 'rock'
            }

            # Determine winner
            if beats[p1] == p2:
                return 1
            elif beats[p2] == p1:
                return 2
            else:
                return 0
            
        elif player1_word.lower() in c and player2_word.lower() not in c:
            return 1
        elif player1_word.lower() not in c and player2_word.lower()  in c:
            return 2


if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()

