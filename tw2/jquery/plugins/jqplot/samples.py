"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import tw2.core as twc

from widgets import JQPlotWidget
from base import dateAxisRenderer_js

from random import random
from random import randint
from math import sin, cos

from time import time

def make_data():
    """ Sin of the times! """
    now = int(time())
    n = 20.0
    tsteps = 100
    tspan = range(now-tsteps, now)
    series1 = [[i*1000,sin(i/n)] for i in tspan]
    series2 = [[i*1000,abs(sin(i/n))**((i%(2*n))/n)] for i in tspan]
    series3 = [[i*1000,cos(i/(n+1))*1.5] for i in tspan]
    series4 = [[series2[i][0], series2[i][1] * series3[i][1]]
               for i in range(len(series3))]
    data = [series1, series2, series3,series4]
    return data

data = make_data()

class DemoJQPlotWidget(JQPlotWidget):
    def prepare(self):
        self.resources.append(dateAxisRenderer_js)
        super(DemoJQPlotWidget, self).prepare()

    data = data
    options = {
        'legend' : { 'show' : True },
        'title' : 'Sine of the times (tw2)',
        'series' : [ {'showMarker' : False} for d in data ],
        'axes' : {
            'xaxis' : {
                'renderer' : twc.JSSymbol('$.jqplot.DateAxisRenderer'),
                'tickOptions' : {
                    'formatString' : '%T'
                },
            },
        },
    }
