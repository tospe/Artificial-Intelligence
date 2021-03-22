# reactiveAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

from game import Directions
from game import Agent
from game import Actions
import util
import time
import search
import numpy as np
from numpy import genfromtxt

class NaiveAgent(Agent):
    "An agent that goes West until it can't."
    def __init__(self):
        self.lap = 0
        self.orientation = 2 

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        sense = state.getPacmanSensor()
        i1 = sense[0]
        i2 = sense[1]
        i3 = sense[2] 
        i4 = sense[3]
        i5 = sense[4] 
        i6 = sense[5]
        i7 = sense[6] 
        i8 = sense[7]

        x1 = i2 or i3
        x2 = i4 or i5
        x3 = i6 or i7
        x4 = i8 or i1

        #Resolves the one line problem
        # if i1 and i2 and i3 and i5 and i6 and i7 and not i8:
        #     return Directions.WEST
        # elif i1 and i2 and i3 and i5 and i6 and i7 and i8:
        #     return Directions.STOP
        

        #Resolves if the map looks like a funnel 
        # if i7 and i5 and not i6 and self.lap != 2:
        #     print "down"
        #     self.orientation = 1  # Orientation down
        #     self.lap += 1
        # if i7 and i5 and not i6 and self.lap == 2 and self.orientation == 1 or x4 and x2 and not i6 and self.orientation == 1:
        #     return Directions.SOUTH

        # if i1 and i3 and not i2 and self.lap != 2:
        #     print "up"
        #     self.orientation = 0  # Orientation ip
        #     self.lap += 1
        # if i1 and i3 and not i2 and self.lap == 2 and self.orientation == 0 or x4 and x2 and not i2 and self.orientation == 0:
        #     return Directions.NORTH

        #Follow every boundarie
        if x4 and not x1:
            return Directions.NORTH
        elif x3 and not x4:
            return Directions.WEST
        elif x2 and not x3:
            return Directions.SOUTH
        elif x1 and not x2:
            return Directions.EAST
        else:
            return Directions.NORTH
        
        # if x1 and x2 and x3 and x4 and not i8:
        #     return Directions.WEST

        



class PSAgent(Agent):
    "An agent that follows the boundary using production system."

    def getAction(self, state):
        ''' Your code goes here! '''
        return Directions.NORTH

class ECAgent(Agent):
    "An agent that follows the boundary using error-correction."

    def __init__(self):
        self.north = Perceptron("../north.csv", 0.1, 2)
        self.north.train()

        self.west = Perceptron("../west.csv", 0.1, 2)
        self.west.train()

        self.south = Perceptron("../south.csv", 0.1, 2)
        self.south.train()

        self.east = Perceptron("../east.csv", 0.1, 2)
        self.east.train()

        self.cycle = 0


    def getAction(self, state):

        # inputs = state.getPacmanSensor()

        # isN = self.north.predict(inputs)
        # isW = self.west.predict(inputs)
        # isS = self.south.predict(inputs)
        # isE = self.east.predict(inputs)

        if isN and not isW and not isS and not isE:
            return Directions.NORTH
        elif not isN and isW and not isS and not isE:
            return Directions.WEST
        elif not isN and not isW and isS and not isE:
            return Directions.SOUTH
        elif not isN and not isW and not isS and isE:
            return Directions.EAST

        # moreThanOne = 1 if isN + isW + isS + isE > 1 else 0

        # if moreThanOne:
        #     if self.cycle == 0:
        #         self.cycle = 1
        #         return Directions.NORTH
        #     elif self.cycle == 1:
        #         self.cycle = 2
        #         return Directions.EAST
        #     elif self.cycle == 2:
        #         self.cycle = 3
        #         return Directions.SOUTH
        #     elif self.cycle == 3:
        #         self.cycle = 0
        #         return Directions.WEST


        return Directions.NORTH
            



class Perceptron:

    def __init__(self, file, learningRate, learningEpochs):
        self.learningEpochs = learningEpochs
        self.file = file
        self.learningRate = learningRate
        self.threshold = 1
        self.weights = np.random.uniform(low=-1, high=1, size=8)
        self.train()

    def train(self):
        my_data = genfromtxt(self.file, delimiter=',')
        for i in range(self.learningEpochs):
            for e in my_data:
                    inputs = e[:-1]
                    d = e[-1]
                    f = self.predict(inputs)
                    old = self.weights
                    self.weights = self.weights + \
                        self.learningRate * (d - f) * inputs
                    error = np.mean(old != self.weights)
            print "Generation -->" + str(i)

    def predict(self, inputs):
        activation = 0.0
        for i in range(len(inputs)):
            activation += inputs[i] * self.weights[i]

        return 1.0 if activation >= self.threshold else 0.0
