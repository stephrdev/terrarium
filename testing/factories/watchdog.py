import factory
from didadata.tests.factories.metrics import MetricFactory
from howl.models import Observer
from howl.operators import get_operator_types

from terrarium.watchdog.models import Watchdog


class ObserverFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda i: 'observer {0}'.format(i))
    operator = get_operator_types()[0][0]
    value = 50
    waiting_period = 0

    class Meta:
        model = Observer


class WatchdogFactory(factory.DjangoModelFactory):
    observer = factory.SubFactory(ObserverFactory)
    metric = factory.SubFactory(MetricFactory)

    class Meta:
        model = Watchdog
