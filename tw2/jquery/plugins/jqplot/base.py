
import tw2.jquery.base as twjq_c
import defaults

jqplot_css = twjq_c.jQueryPluginCSSLink(
    name=defaults._jqplot_name_,
    version = defaults._jqplot_version_,
    modname = 'tw2.jquery.plugins.jqplot',
    subdir = '',
)

jqplot_js = twjq_c.jQueryPluginJSLink(
    name=defaults._jqplot_name_,
    version=defaults._jqplot_version_,
    variant='min',
    modname='tw2.jquery.plugins.jqplot',
    subdir = '',
)

__all__ = ['jqplot_js', 'jqplot_css']
