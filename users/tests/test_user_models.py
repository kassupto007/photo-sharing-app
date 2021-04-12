import pytest

from users.models import Profile


@pytest.mark.django_db
def test_create_user():
    Profile.objects.create_user(username='test', password='testPassword8')
    assert Profile.objects.count() == 1
