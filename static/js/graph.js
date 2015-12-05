(function($) {
	$.graph = function(element, options) {
		var module = {
			element: element,
			graph_element: $('<div>').addClass('plot'),
			legend_element: $('<div>').addClass('legend'),
			graph_object: undefined,
			options: $.extend({
				metrics: undefined,
			}, options),

			init: function() {
				module.element.append(module.graph_element);
				module.element.append(module.legend_element);

				module.graph_object = {
					data: undefined,
					legend: undefined,
					legend_target: module.legend_element.get(0),
					full_width: true,
					height: 600,
					interpolate: 'basic',
					target: module.graph_element.get(0),
					x_accessor: 'timestamp',
					y_accessor: 'value',
					x_extended_ticks: true,
					y_extended_ticks: true,
					yax_count: 20,
					area: false,
					missing_is_hidden: true,
					min_y_from_data: true,
					max_y_from_data: true,
				}
			},

			refresh: function(metrics) {
				module.options.metrics = metrics;

				endpoint = '/api/records/';
				if (metrics !== undefined) {
					endpoint += '?metric=' + metrics.join(',');
				};

				d3.json(endpoint, function(response) {
					var groups = d3.nest().key(function(record) {
						return  record.metric;
					}).map(response.results, d3.map);

					groups.forEach(function(key, values) {
						groups.set(key, MG.convert.date(
							values,
							'timestamp',
							'%Y-%m-%dT%H:%M:%S.%L%LZ'
						));
					});

					module.plot(groups.keys(), groups.values());
				});
			},

			plot: function(legend, data) {
				module.graph_object.legend = legend ;
				module.graph_object.data = data;

				MG.data_graphic(module.graph_object);
			}
		};

		module.init();
		module.refresh(module.options.metrics);

		return {
			refresh: module.refresh,
		};
	};
})(jQuery);
