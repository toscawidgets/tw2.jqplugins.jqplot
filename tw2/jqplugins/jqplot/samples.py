"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import tw2.core as twc
from tw2.core.resources import encoder

from widgets import JQPlotWidget, PollingJQPlotWidget
from base import dateAxisRenderer_js

from random import random
from random import randint
from math import sin, cos

from time import time

def find_bounds(data):
    minx = min( [min( [point[0] for point in series] ) for series in data])
    maxx = max( [max( [point[0] for point in series] ) for series in data])
    miny = min( [min( [point[1] for point in series] ) for series in data])
    maxy = max( [max( [point[1] for point in series] ) for series in data])
    miny -= 0.1
    maxy += 0.1
    return minx, maxx, miny, maxy

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

class DemoPollingJQPlotWidget(PollingJQPlotWidget):
    def prepare(self):
        self.resources.append(dateAxisRenderer_js)
        super(DemoPollingJQPlotWidget, self).prepare()

    url = '/jqplot_datasource/'
    url_kwargs = {}
    interval = 2000

    data = data
    options = {
        'legend' : { 'show' : True },
        'title' : '(Polling) Sine of the times (tw2)',
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

    @classmethod
    def request(cls, req):
        import webob
        data = make_data()
        minx, maxx, miny, maxy = find_bounds(data)
        options = {
            'axes' : {
                'xaxis' : { 'min' : minx, 'max' : maxx },
                'yaxis' : { 'min' : miny, 'max' : maxy },
            }
        }
        json = encoder.encode(dict(data=data, options=options))
        return webob.Response(json, content_type="application/json")


# Register the widget's controller
import tw2.core as twc
mw = twc.core.request_local()['middleware']
mw.controllers.register(DemoPollingJQPlotWidget, 'jqplot_datasource')


