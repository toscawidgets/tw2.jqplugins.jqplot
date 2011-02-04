<%namespace name="tw" module="tw2.core.mako_util"/>
<div>
<div ${tw.attrs(attrs=w.attrs)}></div>
<script type="text/javascript">
    $(document).ready(
      function(){
        doPollingJQPlotWidget(
          // selector
          '${w.selector}',
          // data
          ${w._data},
          // options
          ${w._options},
          // url
          '${w.url}',
          // url_kwargs
          ${w.url_kwargs},
          // interval
          ${str(w.interval)}
        );
      }
    );
</script>
</div>
