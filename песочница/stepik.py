class HighScoreTable:
    def __init__(self, qt):
        self.qt = qt
        self._table = []

    def update(self, num):
        self._table.append(num)

    @property
    def scores(self):
        self._table = sorted(self._table, reverse=True)[:self.qt]
        return self._table
    def reset(self):
        self._table.clear()