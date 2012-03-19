tw2.jqplugins.jqplot
=========================

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _jqPlot: http://www.jqplot.com/

tw2.jqplugins.jqplot is a `toscawidgets2 (tw2)`_ wrapper for `jqPlot`_.

Live Demo
---------
Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.jqplugins.jqplot>`_.

Links
-----
Get the `source from github <http://github.com/toscawidgets/tw2.jqplugins.jqplot>`_.

`PyPI page <http://pypi.python.org/pypi/tw2.jqplugins.jqplot>`_
and `bugs <http://github.com/toscawidgets/tw2.jqplugins.jqplot/issues/>`_

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

`jqPlot`_ is a plotting and charting plugin for the jQuery Javascript
framework. `jqPlot`_ produces beautiful line, bar and pie charts.

This module, tw2.jqplugins.jqplot, provides `toscawidgets2 (tw2)`_ access
to `jqPlot`_ widgets.

Sampling tw2.jqplugins.jqplot in the WidgetBrowser
--------------------------------------------------

The best way to scope out ``tw2.jqplugins.jqplot`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.jqplugins.jqplot/tw2/jqplugins/jqplot/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.jqplugins.jqplot.git
    $ cd tw2.jqplugins.jqplot
    $ mkvirtualenv tw2.jqplugins.jqplot
    (tw2.jqplugins.jqplot) $ pip install tw2.devtools
    (tw2.jqplugins.jqplot) $ python setup.py develop
    (tw2.jqplugins.jqplot) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
