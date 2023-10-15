# -*- coding: utf-8 -*-
"""MLOM_Lab10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16IfHCqmng_1wOKoc1ImpBN_jN7SjQzHx
"""

from pulp import *
import matplotlib.pyplot as plt
import numpy as np

pip install pulp

#creating an LP problem named "Simple LP Problem" to maximize a objection function
prob = LpProblem("Simple LP Problem",LpMaximize)

#define two decision variable
x = LpVariable("x",0) #to get negative numbers
y = LpVariable("y",0)

#adding an objective function to your Pulp Linear programming(LP) problem
prob += 3*x + 2*y

#define the constraints
prob += 2*x + y <= 18.0
prob += 2*x + 3*y <= 42.0
prob += 3*x + y <= 24.0

#invoke the LP solver to find the optimal for your decision variable "x" and "y"
prob.solve()

x.varValue

y.varValue

value(prob.objective)