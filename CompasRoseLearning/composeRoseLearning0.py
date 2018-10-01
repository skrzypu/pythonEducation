#!/usr/bin/env python

from os import listdir
from os.path import isfile, join
import csv
import turtle
import math

class GameConfigure:
    def __init__(self, pathToGameData):
        self.pathToGameData = pathToGameData
        self.gameData = []

    def loadRandomData(self):
        onlyfiles = [f for f in listdir(self.pathToGameData) if isfile(join(self.pathToGameData, f))]
        gameFile = self.pathToGameData + "/square.txt"
        f = open(gameFile, 'rb')
        reader = csv.reader(f)
        row_count = sum(1 for row in gameFile)

        for row in reader:
            for data in row:
                self.gameData.append(data.split(";"))
            break
        f.close()

gameConfigure = GameConfigure("game_data")
gameConfigure.loadRandomData()
turtleWindow = turtle.Screen()
turtle = turtle.Turtle()
turtle.left(90)
print gameConfigure.gameData

def printTurtleStep(turtle, step):
    index=2
    for x in range(10):
        modulo = index % 2
        turtle.pencolor((1*modulo,1*(modulo+1)%2,0))
        index = modulo + 1
        turtle.forward(step)

for step,direction in gameConfigure.gameData:
    step = int(step)
    if direction == "S":
        turtle.left(180)
        printTurtleStep(turtle,step)
        turtle.right(180)
    elif direction == "NE":
        turtle.right(45)
        printTurtleStep(turtle,math.sqrt(2)*step)
        turtle.left(45)
    elif direction == "E":
        turtle.right(90)
        printTurtleStep(turtle,step)
        turtle.left(90)
    elif direction == "NW":
        turtle.left(45)
        printTurtleStep(turtle,math.sqrt(2)*step)
        turtle.right(45)
    elif direction == "W":
        turtle.left(90)
        printTurtleStep(turtle,step)
        turtle.right(90)
    elif direction == "SE":
        turtle.right(135)
        printTurtleStep(turtle,math.sqrt(2)*step)
        turtle.left(135)
    elif direction == "SW":
        turtle.left(135)
        printTurtleStep(turtle,math.sqrt(2)*step)
        turtle.right(135)
    else:
        turtle.forward(step*10)

input("Press Enter to continue...")
