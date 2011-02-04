/* Some workhorse functions for tw2.jquery.plugins.jqplot */

function doJQPlotWidget(sel, data, options){
        $.jqplot.config.enablePlugins = true;
        $.jqplot(sel, data, options);
}

// closure
function make_jqplot_async_callback(pl) {
        return function (json) {
                for ( _i = 0; _i < json.data.length; _i++ ) {
                        pl.series[_i].data = json.data[_i] ;
                }
                for (ax in json.options.axes) {
                        pl.axes[ax]._ticks = []
                        if ( 'axes' in json.options &&
                                ax in json.options.axes &&
                                'min' in json.options.axes[ax] ) {
                                pl.axes[ax].min = json.options['axes'][ax].min;
                                pl.axes[ax].max = json.options['axes'][ax].max;
                        }
                        pl.axes[ax].numberTicks = null
                        pl.axes[ax].tickInterval = null
                        pl.axes[ax]._tickInterval = null
                }
                pl.redraw();
        };
}

function doPollingJQPlotWidget(sel, data, options, url, url_kwargs, interval){
        $.jqplot.config.enablePlugins = true;

        // Setup our initial plot
        var the_plot_thickens = $.jqplot(sel, data, options);

        var callback = make_jqplot_async_callback(the_plot_thickens);

        // Finally make the JSON call
        $.getJSON(url, url_kwargs, callback);

        // And if we want to keep polling, do it
        if ( interval > 0 ) {
                setInterval( function() {
                        $.getJSON(url, url_kwargs, callback);
                }, interval );
        }

}

