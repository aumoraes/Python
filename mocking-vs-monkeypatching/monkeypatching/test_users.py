import pytest


def substitute_func(username):
    print("aqui 1")
    return '[{"login": "aishapectyo"},{"login": "jradavenport"},{"login": "kridicule"}]'


@pytest.fixture()
def gh_patched(monkeypatch):
    import monkeypatching.users as users
    print("aqui 2")
    monkeypatch.setattr(users, 'get_user_followers', substitute_func)


def test_get_follower_names_returns_name_list(gh_patched):
    from monkeypatching.users import get_follower_names
    print("aqui 3")
    assert 'jradavenport' in get_follower_names('aumoraes')
