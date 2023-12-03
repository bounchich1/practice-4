import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from functools import partial

from op_5 import Interval, Gap, RightGap, LeftGap


class InvalidGaps(Exception):
    pass


class IntervalApp(QWidget):
    def __init__(self):
        super().__init__()

        self.edit_start = None
        self.edit_end = None
        self.edit_point = None

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_start = QLabel("Start:")
        self.edit_start = QLineEdit()
        layout.addWidget(self.label_start)
        layout.addWidget(self.edit_start)

        self.label_end = QLabel("End:")
        self.edit_end = QLineEdit()
        layout.addWidget(self.label_end)
        layout.addWidget(self.edit_end)

        self.label_point = QLabel("Point to check:")
        self.edit_point = QLineEdit()
        layout.addWidget(self.label_point)
        layout.addWidget(self.edit_point)

        self.button_interval = QPushButton("Check Interval")
        self.button_interval.clicked.connect(partial(self.check_interval, Interval))
        layout.addWidget(self.button_interval)

        self.button_gap = QPushButton("Check Gap")
        self.button_gap.clicked.connect(partial(self.check_gap, Gap))
        layout.addWidget(self.button_gap)

        self.button_right_gap = QPushButton("Check Half Interval Right")
        self.button_right_gap.clicked.connect(partial(self.check_right_gap, RightGap))
        layout.addWidget(self.button_right_gap)

        self.button_left_gap = QPushButton("Check Half Interval Left")
        self.button_left_gap.clicked.connect(partial(self.check_left_gap, LeftGap))
        layout.addWidget(self.button_left_gap)

        self.button_infinite = QPushButton("Check Infinite Interval")
        self.button_infinite.clicked.connect(partial(self.check_infinite_interval))
        layout.addWidget(self.button_infinite)

        self.setLayout(layout)
        self.setWindowTitle("Interval Checker")

    def get_start_end(self):
        try:
            start = float(self.edit_start.text())
            end = float(self.edit_end.text())
            if start >= end:
                raise InvalidGaps
            return start, end
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values.")
            return None, None
        except InvalidGaps:
            QMessageBox.warning(self, "Illogical gaps", "Please enter valid numeric values.")
            return None, None

    def get_point(self):
        try:
            point = float(self.edit_point.text())
            return point
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid numeric point.")
            return

    def check_interval(self, interval_type):
        start, end = self.get_start_end()
        user_gap = Interval(start, end)
        if start is None or end is None:
            return

        point = self.get_point()

        interval = interval_type(start, end)
        if interval.contains(point):
            QMessageBox.information(self, "Result",
                                    f"The point {point} belongs to the {interval_type.__name__} {str(user_gap)}")
        else:
            QMessageBox.information(self, "Result",
                                    f"The point {point} does not belong to the {interval_type.__name__} {str(user_gap)}")

    def check_infinite_interval(self):
        start, end = self.get_start_end()
        user_gap = Interval(start, end)
        point = self.get_point()

        interval = Interval(start, end)
        if interval.contains(point):
            QMessageBox.information(self, "Result",
                                    f"The point {point} belongs to the Infinite Interval {str(user_gap)}")
        else:
            QMessageBox.information(self, "Result",
                                    f"The point {point} does not belong to the Infinite Interval {str(user_gap)}")

    def check_gap(self, interval_type):
        start, end = self.get_start_end()
        user_gap = Gap(start, end)
        if start is None or end is None:
            return
        point = self.get_point()

        interval = interval_type(start, end)
        if interval.contains(point):
            QMessageBox.information(self, "Result",
                                    f"The point {point} belongs to the {interval_type.__name__} {str(user_gap)}")
        else:
            QMessageBox.information(self, "Result",
                                    f"The point {point} does not belong to the {interval_type.__name__} {str(user_gap)}")

    def check_left_gap(self, interval_type):
        start, end = self.get_start_end()
        user_gap = LeftGap(start, end)
        if start is None or end is None:
            return
        point = self.get_point()

        interval = interval_type(start, end)
        if interval.contains(point):
            QMessageBox.information(self, "Result",
                                    f"The point {point} belongs to the {interval_type.__name__} {str(user_gap)}")
        else:
            QMessageBox.information(self, "Result",
                                    f"The point {point} does not belong to the {interval_type.__name__} {str(user_gap)}")

    def check_right_gap(self, interval_type):
        start, end = self.get_start_end()
        user_gap = RightGap(start, end)
        if start is None or end is None:
            return
        try:
            point = float(self.edit_point.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid numeric point.")
            return

        interval = interval_type(start, end)
        if interval.contains(point):
            QMessageBox.information(self, "Result",
                                    f"The point {point} belongs to the {interval_type.__name__} {str(user_gap)}")
        else:
            QMessageBox.information(self, "Result",
                                    f"The point {point} does not belong to the {interval_type.__name__} {str(user_gap)}")

def run_interval_app():
    app = QApplication(sys.argv)
    window = IntervalApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_interval_app()
