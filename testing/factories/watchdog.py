import factory

from terrarium.watchdog.models import Watchdog
from testing.factories.didadata import MetricFactory
from testing.factories.howl import ObserverFactory


class WatchdogFactory(factory.DjangoModelFactory):
    observer = factory.SubFactory(ObserverFactory)
    metric = factory.SubFactory(MetricFactory)

    class Meta:
        model = Watchdog
