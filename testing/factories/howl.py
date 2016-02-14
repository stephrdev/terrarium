import factory
from howl.models import Observer
from howl.operators import get_operator_types


class ObserverFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda i: 'observer {0}'.format(i))
    operator = get_operator_types()[0][0]
    value = 50
    waiting_period = 5

    class Meta:
        model = Observer
