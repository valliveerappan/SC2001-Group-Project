#keeps track of how many comparisons made when sorting arr for analysing efficiency
class KeyComparisons:
    def __init__(self):
        self.key_comparisons = 0

    def less_than(self, a, b):
        self.key_comparisons += 1
        return a < b

    def less_than_or_equal(self, a, b):
        self.key_comparisons += 1
        return a <= b

    def reset(self):
        self.key_comparisons = 0

    def get(self):
        return self.key_comparisons
