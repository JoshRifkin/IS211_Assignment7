# Assignment 7
# By: Joshua Rifkin

import argparse
import random
from itertools import cycle


class Dice(object):
    def __init__(self):
        self.sides = 6


    def rollDie(self):
        return random.randint(1, 6)


class Player(object):
    def __init__(self, name):
        self.playerScore = 0
        self.playerName = name

    def addScore(self, score):
        self.playerScore += score

    def getScore(self):
        return self.playerScore

    def getPlayer(self):
        return self.playerName


class Game(object):
    def __init__(self, players):
        self.numPlayers = players
        self.players = []
        self.playerCycle = cycle(self.players)
        self.turnScore = 0
        self.currPlayer = None

    def newTurn(self):
        return next(self.playerCycle)

    def play(self, numPlayers):
        die = Dice()

        for i in range(numPlayers):
            player = Player("player " + str(i + 1))
            self.players.append(player)

        self.currPlayer = self.newTurn()
        print(self.currPlayer.getPlayer() + "'s turn.")

        while (self.currPlayer.getScore() + self.turnScore) < 100:

            move = input("\nWhat would you like to do?\n \'r\' = roll\n \'h\' = hold\n")

            if move == 'r':
                turn = die.rollDie()
                if turn == 1:
                    print(self.currPlayer.getPlayer() + " rolled  a 1! End of your turn.")
                    self.turnScore = 0
                    self.currPlayer = self.newTurn()
                    print("\n" + self.currPlayer.getPlayer() + "'s turn.")
                else:
                    print("You rolled a " + str(turn))
                    self.turnScore += turn
                    print("Total round score = " + str(self.turnScore))
                    print(self.currPlayer.getPlayer() + "'s total score is: " +
                          str((self.currPlayer.getScore() + self.turnScore)))
            elif move == 'h':
                self.currPlayer.addScore(self.turnScore)
                self.turnScore = 0
                print("End of " + self.currPlayer.getPlayer() + "'s turn.")
                self.currPlayer = self.newTurn()
                print(self.currPlayer.getPlayer() + "'s turn.")
            elif move == 'quit':
                quit()
            else:
                print("Please enter a valid move option.")

        print(self.currPlayer + " wins! Your score was " + str((self.currPlayer.getScore + self.turnScore)))
        quit()


def main():
    parser = argparse.ArgumentParser(description="How many people want to play the game of pig?")
    parser.add_argument('-n', '--numPlayers', type=int, help='How many people are playing the game?')
    args = parser.parse_args()

    print("Welcome to Pig!")
    # Seed placed for sake of simplification of testing for Professor
    random.seed(0)

    if args.numPlayers <= 1:
        print("You need at least 2 players to play Pig!")
    else:
        game = Game(args.numPlayers)
        game.play(args.numPlayers)


if __name__ == '__main__':
    main()
