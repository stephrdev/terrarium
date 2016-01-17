import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda i: 'user-{0}'.format(i))
    email = factory.LazyAttribute(lambda o: '{0}@none.none'.format(o.username))
    first_name = factory.Sequence(lambda m: 'First {0}'.format(m))
    last_name = factory.Sequence(lambda n: 'Last {0}'.format(n))
    is_active = True
    is_staff = True

    class Meta:
        model = User

    @classmethod
    def _prepare(cls, create, **kwargs):
        raw_password = kwargs.pop('raw_password', 'secret')
        if 'password' not in kwargs:
            kwargs['password'] = make_password(raw_password)
        return super()._prepare(create, **kwargs)
