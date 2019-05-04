from PyQt5.QtWidgets import QApplication, QLabel


def show_app():
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    app.exec_()
