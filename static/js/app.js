$(document).ready(function() {
	$('.graph').each(function() {
		var button = $('<button>').text('Refresh');
		$(this).append(button);
		$.graph($(this), {
			metrics: ($(this).data('graph') || '').split(','),
			title: $(this).attr('title'),
			height: Math.min(Math.round($(this).width() * 10 / 16), 600),
			refresh_button: button,
			refresh_interval: 300
		});
	});

	window.refresh_graph = function() {
		graph.refresh($('.sensors input:checked').map(function() { return this.value; }).toArray());
	}

	$('.sensors button').click(function(e) {
		e.preventDefault();
		refresh_graph();
	});

	$.get('/api/metrics/', function(data) {
		$.each(data.results, function(i, metric) {
			$('.sensors').append($('<label>').append($('<input>').attr({
				type: 'checkbox', value: metric.name, checked: 'checked'
			})).append(' ' + metric.name));
		});
	});
});
