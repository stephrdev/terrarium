(function($) {
	$.graph = function(element, options) {
		var module = {
			element: element,
			graph_element: $('<div>').addClass('plot'),
			legend_element: $('<div>').addClass('legend'),
			graph_object: undefined,
			options: $.extend({
				title: 'Graph',
				metrics: undefined,
				height: element.height(),
				refresh_interval: undefined,
				refresh_button: undefined
			}, options),

			init: function() {
				module.element.append(module.graph_element);
				module.element.append(module.legend_element);

				module.graph_object = {
					title: module.options.title,
					data: undefined,
					legend: undefined,
					legend_target: module.legend_element.get(0),
					full_width: true,
					height: module.options.height,
					interpolate: 'basic',
					target: module.graph_element.get(0),
					x_accessor: 'timestamp',
					y_accessor: 'value',
					x_extended_ticks: true,
					y_extended_ticks: true,
					yax_count: module.options.height * 0.03,
					area: false,
					missing_is_hidden: true,
					min_y_from_data: true,
					max_y_from_data: true,
					utc_time: false,
				};

				if (module.options.refresh_interval !== undefined) {
					setInterval(function() {
						module.refresh(module.options.metrics);
					}, module.options.refresh_interval * 1000);
				};

				if (module.options.refresh_button !== undefined) {
					module.options.refresh_button.click(function(e) {
						e.preventDefault();
						module.refresh(module.options.metrics);
					});
				};
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
						}).map(response.results, d3.map),
						formatter = d3.time.format.utc('%Y-%m-%dT%H:%M:%S.%L%LZ')
					;

					groups.forEach(function(key, values) {
						groups.set(key, values.map(function(record) {
							record.timestamp = formatter.parse(record.timestamp);
							return record;
						}));
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
