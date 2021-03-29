


import pytest
def substitute_func(title, body):
    return None


@pytest.fixture()
def gh_patched(monkeypatch):
    import views
    monkeypatch.setattr(views, 'Entry', substitute_func)


def test_some_view_post_returns_redirect(mocker, gh_patched):
    from views import some_view, HTTPFound
    req = mocker.MagicMock()
    req.method = 'POST'
    req.POST = {'title': 'some title', 'body': 'some body text'}
    req.dbsession.add = lambda arg: None
    assert isinstance(some_view(req), HTTPFound)

def test_some_view_get_req_returns_dict(mocker):
    from views import some_view
    req = mocker.MagicMock()
    req.method = 'GET'
    assert some_view(req) == {}



    
def test_method_calls(mocker, gh_patched):
    from views import some_view, HTTPFound, Entry
    
    req = mocker.MagicMock()
    req.method = 'POST'
    req.POST = {'title': 'some title', 'body': 'some body text'}
    
    mocker.spy(HTTPFound, '__init__')
    mocker.spy(Entry, '__init__')
    
    req.dbsession.add = lambda arg: None
    some_view(req)
    assert HTTPFound.__init__.call_count == 1
    assert Entry.__init__.call_count == 0

def test_values_are_dropped_if_already_seen(mocker):
    from views import Numbers
    nums = Numbers([1,2,1,2,1,2])
    mocker.spy(nums, '_drop_val')
    nums.make_unique()
    assert nums._drop_val.call_count == 4