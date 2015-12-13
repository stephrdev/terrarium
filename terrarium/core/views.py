from django.http import JsonResponse
from django.views.generic import TemplateView, View
from django.views.generic.list import MultipleObjectMixin

from didadata.models import Record


class HomeView(TemplateView):
    template_name = 'home.html'


class RecordsApiView(MultipleObjectMixin, View):
    model = Record
    paginate_by = 250

    def get_queryset(self):
        qset = super().get_queryset()
        if self.request.GET.get('metric', ''):
            qset = qset.filter(metric__name__in=self.request.GET['metric'].split(','))
        return qset

    def get(self, request, *args, **kwargs):
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            self.get_queryset(), self.paginate_by)
        return JsonResponse({'results': [
            {'metric': obj.metric.name, 'timestamp': obj.timestamp, 'value': obj.value}
            for obj in queryset
        ]})
