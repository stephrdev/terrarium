$(document).ready(function() {
	var graph = undefined;

	$('.graph').each(function() {
		graph = $.graph($(this), {metrics: ($(this).data('graph') || '').split(',')});
	});

	$.get('/api/metrics/', function(data) {
		$.each(data.results, function(i, metric) {
			$('.sensors').append($('<label>').append($('<input>').attr({
				type: 'checkbox', value: metric.name, checked: 'checked'
			})).append(metric.name));
		});

		window.refresh_graph = function() {
			graph.refresh($('.sensors input:checked').map(function() { return this.value; }).toArray());
		}

		$('.sensors input').click(refresh_graph);

		setInterval(window.refresh_graph, 5 * 60 * 1000);
	});
});
