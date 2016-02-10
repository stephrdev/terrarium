import pytest
from django.contrib import admin

from didadata.tests.factories.metrics import MetricFactory, RecordFactory
from terrarium.watchdog.admin import WatchdogAdmin
from terrarium.watchdog.models import Watchdog
from testing.factories.users import UserFactory
from testing.factories.watchdog import WatchdogFactory


@pytest.mark.django_db
class TestWatchdogAdmin:
    def setup(self):
        self.modeladmin = WatchdogAdmin(Watchdog, admin.site)

    def test_get_last_value(self, rf):
        metric = MetricFactory.create()
        RecordFactory.create(value=5, metric=metric)
        obj = WatchdogFactory.create(metric=metric)

        user = UserFactory.create()
        request = rf.get('/')
        request.user = user

        assert self.modeladmin.get_last_value(obj=obj) == 5

    def test_get_last_timestamp(self, rf):
        metric = MetricFactory.create()
        record = RecordFactory.create(value=5, metric=metric)
        obj = WatchdogFactory.create(metric=metric)

        user = UserFactory.create()
        request = rf.get('/')
        request.user = user

        assert self.modeladmin.get_last_timestamp(obj=obj) == record.timestamp
