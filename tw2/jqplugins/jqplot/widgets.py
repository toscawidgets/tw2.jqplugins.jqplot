


from tw2.core.resources import encoder
import tw2.core as twc

import tw2.jquery
import tw2.jqplugins.ui.base as tw2_jq_ui

import base

_pager_defaults = {'enableSearch': True, 'enableClear': True, 'gridModel': True}


class JQPlotWidget(tw2_jq_ui.JQueryUIWidget):
    width = twc.Param("Width of the chart.", default="550px")
    height = twc.Param("Height of the chart.", default="300px")
    style = twc.Variable(attribute=True)

    resources = [
        tw2.jquery.jquery_js,
        tw2_jq_ui.jquery_ui_js, tw2_jq_ui.jquery_ui_css,
        base.jqplot_js, base.jqplot_css, base.jqplot_utils_js,
    ]
    template = "tw2.jqplugins.jqplot.templates.jqplot"

    data = twc.Param("A list of list of tuples to plot.", default=[])
    options = twc.Param("Configuration options to pass to jqplot", default={})

    def prepare(self):
        self._data = encoder.encode(self.data)
        self._options = encoder.encode(self.options)
        self.style = "width:%s;height:%s;" % (self.width, self.height)
        super(JQPlotWidget, self).prepare()

class PollingJQPlotWidget(JQPlotWidget):
    template = "tw2.jqplugins.jqplot.templates.pollster"

    url = twc.Param("(string) A url to poll", default='')
    url_kwargs = twc.Param("(dict) A dict for a query str", default={})
    interval = twc.Param("(int) milliseconds between pulls", default=0)

    def prepare(self):
        self.url_kwargs = encoder.encode(self.url_kwargs)
        super(PollingJQPlotWidget, self).prepare()
