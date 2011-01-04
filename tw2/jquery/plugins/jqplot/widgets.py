


from tw2.core.resources import encoder
import tw2.core as twc

import tw2.jquery
import tw2.jquery.base as tw2_jq_c_b
import tw2.jquery.plugins.ui.base as tw2_jq_ui

import formencode.validators as fv
import base

_pager_defaults = {'enableSearch': True, 'enableClear': True, 'gridModel': True}

import formencode as fe
import formencode.validators as fv

class JQPlotWidget(tw2_jq_ui.JQueryUIWidget):
    resources = [
        tw2.jquery.jquery_js,
        tw2_jq_ui.jquery_ui_js, tw2_jq_ui.jquery_ui_css,
        base.jqplot_js, base.jqplot_css,
    ]
    template = "tw2.jquery.plugins.jqplot.templates.jqplot"
  
    data = twc.Param("A list of list of tuples to plot.", default=[])
    options = twc.Param("Configuration options to pass to jqplot", default={})

    def prepare(self):
        super(JQPlotWidget, self).prepare()
        self._data = encoder.encode(self.data)
        self._options = encoder.encode(self.options)
