def some_view(request):
    if request.method == "GET":
        return {}
    if request.method == "POST":
        new_entry = Entry(
            title = request.POST['title'],
            body = request.POST['body']
        )
        request.dbsession.add(new_entry)
        return HTTPFound(request.route_url('entry_list'))


class Entry():
    def __init__(self, title, body):
        print("HI Entry")
        pass

class HTTPFound():
    def __init__(self, route_url):
        print("HI HTTPFound")
        pass

class Numbers(object):
    def __init__(self, iterable):
        self._container = iterable

    def make_unique(self):
        i = 0
        visited = []
        while i < len(self._container):
            if self._container[i] in visited:
                self._drop_val(i)
                #i = 0
                continue
            visited.append(self._container[i])
            i += 1

    def _drop_val(self, idx):
        self._container.pop(idx)