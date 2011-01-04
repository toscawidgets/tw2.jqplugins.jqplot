<%namespace name="tw" module="tw2.core.mako_util"/>
<div>
<div ${tw.attrs(attrs=w.attrs)}></div>
<script type="text/javascript">
$(document).ready(
    function(){
		$.jqplot.config.enablePlugins = true;
		$.jqplot(
			'${w.selector}',
			${w._data},
			${w._options}
		);
    }
);
</script>
</div>
