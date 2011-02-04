
import tw2.core as twc
import tw2.jquery.base as twjq_c
import defaults

jqplot_css = twjq_c.jQueryPluginCSSLink(
    name=defaults._jqplot_name_,
    version = defaults._jqplot_version_,
    modname = 'tw2.jqplugins.jqplot',
    subdir = '',
)
jqplot_js = twjq_c.jQueryPluginJSLink(
    name=defaults._jqplot_name_,
    version=defaults._jqplot_version_,
    variant='min',
    modname='tw2.jqplugins.jqplot',
    subdir = '',
)
jqplot_utils_js = twc.JSLink(
    modname='tw2.jqplugins.jqplot',
    filename='static/js/jqplot-utils.js',
)


class JQPlotPluginJSLink(twjq_c.jQueryPluginJSLink):
    jqplugin = twc.Param('(string) Name of the jqplot plugin')
    name=defaults._jqplot_name_
    version=defaults._jqplot_version_
    variant='min'
    modname='tw2.jqplugins.jqplot'
    basename='jqplot.%(jqplugin)s'
    subdir = 'plugins'

    @property
    def substitutions(self):
        subs = super(JQPlotPluginJSLink, self).substitutions
        subs.update(dict(jqplugin=self.jqplugin))
        return subs

__all__ = ['jqplot_js', 'jqplot_css', 'jqplot_utils_js']

jqplugins = [
    'barRenderer',
    'BezierCurveRenderer',
    'blockRenderer',
    'bubbleRenderer',
    'canvasAxisLabelRenderer',
    'canvasAxisTickRenderer',
    'categoryAxisRenderer',
    'ciParser',
    'cursor',
    'dateAxisRenderer',
    'donutRenderer',
    'dragable',
    'enhancedLegendRenderer',
    'funnelRenderer',
    'highlighter',
    'json2',
    'logAxisRenderer',
    'mekkoAxisRenderer',
    'mekkoRenderer',
    'meterGaugeRenderer',
    'ohlcRenderer',
    'pieRenderer',
    'pointLabels',
    'trendline',
]

jqplugins_links = dict(
    [("%s_js" % jqp, JQPlotPluginJSLink(jqplugin=jqp)) for jqp in jqplugins])

locals().update(**jqplugins_links)
__all__.extend(jqplugins_links.keys())
