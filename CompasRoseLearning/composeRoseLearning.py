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

gameConfigure = GameConfigure("game_data")
gameConfigure.loadRandomData()
turtleWindow = turtle.Screen()
turtle = turtle.Turtle()
print gameConfigure.gameData

def printTurtleStep(turtle, step, isSlant = False):
    index=2
    for x in range(step):
        modulo = index % 2
        turtle.pencolor((1*modulo,1*(modulo+1)%2,0))
        index = modulo + 1
        distanse = 10
        if isSlant:
            distanse = math.sqrt(2) * 10
        turtle.forward(distanse)

for step,direction in gameConfigure.gameData:
    step = int(step)
    if direction == "S":
        turtle.setheading(270)
        printTurtleStep(turtle,step, False)
    elif direction == "NE":
        turtle.setheading(45)
        printTurtleStep(turtle,step,True)
    elif direction == "E":
        turtle.setheading(0)
        printTurtleStep(turtle,step, False)
    elif direction == "NW":
        turtle.setheading(135)
        printTurtleStep(turtle,step,True)
    elif direction == "W":
        turtle.setheading(180)
        printTurtleStep(turtle,step, False)
    elif direction == "SE":
        turtle.setheading(315)
        printTurtleStep(turtle,step,True)
    elif direction == "SW":
        turtle.setheading(225)
        printTurtleStep(turtle,step,True)
    else:
        turtle.setheading(90)
        printTurtleStep(turtle,step, False)

input("Press Enter to continue...")
