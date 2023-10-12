class Pagination:
    def __init__(self, _list, qt):
        self.qt = qt
        self._l = len(_list)
        self.book = {i: list_ for i, list_ in zip(
            range(1, self._l // qt + 1 + bool(self._l % qt)),
            [_list[i:i + self.qt] for i in range(0, self._l, self.qt)]
        )}
        self.now = 1

    def prev_page(self):
        self.now = self.now - 1 if self.now - 1 > 0 else 1
        return self

    def next_page(self):
        self.now = self.now + 1 if self.now + 1 < max(self.book) else max(self.book)
        return self

    def first_page(self):
        self.now = 1
        return self

    def last_page(self):
        self.now = max(self.book)

    def go_to_page(self, num):
        if num >= max(self.book):
            self.now = max(self.book)
        elif num <= 1:
            self.now = 1
        else:
            self.now = num

    def get_visible_items(self):
        return self.book[self.now]

    @property
    def total_pages(self):
        return max(self.book)

    @property
    def current_page(self):
        return self.now


alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
pagination.next_page().next_page()
print(pagination.get_visible_items())
print(pagination.total_pages)
print(pagination.current_page)

