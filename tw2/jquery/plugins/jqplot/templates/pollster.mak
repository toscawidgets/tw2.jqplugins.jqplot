<%namespace name="tw" module="tw2.core.mako_util"/>
<div>
<div ${tw.attrs(attrs=w.attrs)}></div>
<script type="text/javascript">
$(document).ready(
    function(){
		$.jqplot.config.enablePlugins = true;

		// Setup our initial plot
		var the_plot_thickens = $.jqplot(
			'${w.selector}',
			${w._data},
			${w._options}
		);

		// Setup our callback function
		callback = function (json) {
		  pl = the_plot_thickens;
		  
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

		// Finally make the JSON call
		$.getJSON(
			'${w.url}',
			${w.url_kwargs},
			callback
		);

		// And if we want to keep polling, do it
		var interval = ${str(w.interval)};
		if ( interval > 0 ) {
			setInterval( function() {
				$.getJSON(
					'${w.url}',
					${w.url_kwargs},
					callback
				);}, interval );
		}
    }
);
</script>
</div>
