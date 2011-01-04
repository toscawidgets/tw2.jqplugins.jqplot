"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""
from widgets import JQPlotWidget
from random import random
from random import randint
from math import sin

n = 20

class DemoJQPlotWidget(JQPlotWidget):
    options = {
        'title' : 'just a test title'
    }
    data = [
        [[i, random()*i/float(n)] for i in range(n)],
        [[i, random()*sin(3.14*(i/float(n)))] for i in range(n)],
        [[i, random()/(i+1)] for i in range(n)],
        [[i, random()*i + i] for i in range(n)],
    ]

