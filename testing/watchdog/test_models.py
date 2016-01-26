
import pytest

from didadata.tests.factories.metrics import MetricFactory, RecordFactory
from testing.factories.watchdog import WatchdogFactory


@pytest.mark.django_db
class TestWatchdogModel:

    def test_repr(self):
        obj = WatchdogFactory.create()

        assert str(obj) == '{0} - {1}'.format(obj.observer, obj.metric)

    def test_property_last_value_none(self):
        obj = WatchdogFactory.create()

        assert obj.last_value is None

    def test_property_last_value(self):
        metric = MetricFactory.create()
        RecordFactory.create(value=3, metric=metric)
        RecordFactory.create(value=5, metric=metric)
        obj = WatchdogFactory.create(metric=metric)

        assert obj.last_value == 5

    def test_property_last_time_none(self):
        obj = WatchdogFactory.create()

        assert obj.last_time is None

    def test_property_last_time(self):
        metric = MetricFactory.create()
        RecordFactory.create(value=3, metric=metric)
        record = RecordFactory.create(value=5, metric=metric)
        obj = WatchdogFactory.create(metric=metric)

        assert obj.last_time == record.timestamp
