#!/usr/bin/env python

from os import listdir
from os.path import isfile, join
import csv
import turtle
import math
import random

class GameConfigure:
    def __init__(self, pathToGameData):
        self.pathToGameData = pathToGameData
        self.gameData = []

    def loadRandomData(self):
        onlyfiles = [f for f in listdir(self.pathToGameData) if isfile(join(self.pathToGameData, f))]
        gameFile = self.pathToGameData + "/game_data.csv"
        f = open(gameFile, 'rb')
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        for data in chosen_row:
            self.gameData.append(data.split(";"))
        f.close()

class ComposeRoseGame:
    def __init__(self):
        self.configure = GameConfigure("game_data")
        self.turtleWindow = turtle.Screen()
        self.turtleRose = turtle.Turtle()

    def printTurtleStep(self, turtle, step, isSlant = False):
        index=2
        for x in range(step):
            modulo = index % 2
            self.turtleRose.pencolor((1*modulo,1*(modulo+1)%2,0))
            index = modulo + 1
            distanse = 10
            if isSlant:
                distanse = math.sqrt(2) * 10
                self.turtleRose.forward(distanse)

    def drawSelectedPicture(self):
        for step,direction in self.configure.gameData:
            step = int(step)
            if direction == "S":
                self.turtleRose.setheading(270)
                self.printTurtleStep(turtle,step, False)
            elif direction == "NE":
                self.turtleRose.setheading(45)
                self.printTurtleStep(turtle,step,True)
            elif direction == "E":
                self.turtleRose.setheading(0)
                self.printTurtleStep(turtle,step, False)
            elif direction == "NW":
                self.turtleRose.setheading(135)
                self.printTurtleStep(turtle,step,True)
            elif direction == "W":
                self.turtleRose.setheading(180)
                self.printTurtleStep(turtle,step, False)
            elif direction == "SE":
                self.turtleRose.setheading(315)
                self.printTurtleStep(turtle,step,True)
            elif direction == "SW":
                self.turtleRose.setheading(225)
                self.printTurtleStep(turtle,step,True)
            else:
                self.turtleRose.setheading(90)
                self.printTurtleStep(turtle,step, False)

    def play(self):
        self.configure.loadRandomData()
        self.drawSelectedPicture()

game = ComposeRoseGame()
game.play()
input("Press Enter to continue...")
