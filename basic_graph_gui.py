import sys

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QFont, QIcon

#Set the Name of the Window
plt.figure(num="Coronavirus Graph")


#Adjust the position of the plot canvas, labels and title
plt.subplots_adjust(left=0.15, bottom=0.30, right=0.90, top=0.925, wspace=0.20, hspace=0.20)

#Read the data file
data = pd.read_csv("coronavirus.csv")

#x-axis and y-axis variables. data.nameOfTheColumn for the column variables
x = data.Country
y = data.Confirmed


#Rotate name of countries (on x-axis) by 90 degrees to look neat so they don't overlap
plt.xticks(rotation=90)

#Plot the x-axis and y-axis
plt.bar(x, y)


#Label the x-axis and y-axis
plt.xlabel('Countries')
plt.ylabel('Confirmed')

#Title the Graph
plt.title('Number of People Confirmed with Coronavirus in Countries')


#Display the graph using a GUI
plt.show()

