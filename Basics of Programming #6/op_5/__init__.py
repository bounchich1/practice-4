"""
Program provides functionality to work with
different gaps
"""


class Interval:

    def __init__(self, start, end):

        self.start = start

        self.end = end

    def contains(self, point):

        if self.start == float('-inf') and self.end == float('inf'):
            return True

        if self.start == float('-inf'):
            return point < self.end
        if self.end == float('inf'):
            return point > self.start
        return self.start < point < self.end

    def __str__(self):

        if self.end == float('inf') and self.start == float('-inf'):
            return "(-∞, +∞)"
        if self.start == float('-inf'):
            return f"(-∞, {self.end})"
        if self.end == float('inf'):
            return f"({self.start}, +∞)"
        return f"({self.start}, {self.end})"


class Gap(Interval):

    def contains(self, point):
        return self.start <= point <= self.end

    def __str__(self):
        return f"[{self.start}, {self.end}]"


class RightGap(Interval):

    def contains(self, point):
        return self.start < point <= self.end

    def __str__(self):
        return f"({self.start}, {self.end}]"


class LeftGap(Interval):

    def contains(self, point):
        return self.start <= point < self.end

    def __str__(self):
        return f"[{self.start}, {self.end})"


class GapContainer:

    def __init__(self):
        self.intervals = []

    def add_interval(self, interval) -> None:

        self.intervals.append(interval)

    def remove_interval(self, interval) -> None:

        self.intervals.remove(interval)

    def __contains__(self, interval) -> bool:

        return interval in self.intervals

    def __len__(self) -> int:
        count = 0
        for _ in self.intervals:
            count += 1
        return count

    def print(self) -> str:

        output = ''
        count = 0
        for interval in self.intervals:
            count += 1
            if count == 1:
                output = f'{output}{str(interval)}'
            else:
                output = f'{output}, {str(interval)}'
        output = f'[{output}]'
        return output




