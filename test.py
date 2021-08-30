from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize
import sys

# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Split App')

#         button = QPushButton('Press Me')

#         button.setFixedSize(QSize(100,100))

#         self.setCentralWidget(button)

#         self.setFixedSize(QSize(400,400))


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec()

#############################################################################

# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Split App')

#         self.setFixedSize(QSize(400,400))

#         button = QPushButton('Press Me')
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         button.clicked.connect(self.the_button_was_toggled)

#         self.setCentralWidget(button)

#     def the_button_was_clicked(self):
#         print('Yes Yes')


#     def the_button_was_toggled(self, checked):
#         self.button_checked = checked

#         print(self.button_checked)

# app = QApplication(sys.argv)

# window = MainWindow()

# window.show()


# app.exec()

############################################################################

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Split App 2')
        self.setFixedSize(QSize(400,400))

        self.button = QPushButton('click me')
        self.button.clicked.connect(self.callback)

        self.setCentralWidget(self.button)

    def callback(self):
        self.button.setText('already clicked')
        self.button.setCheckable(False)

        self.setWindowTitle('we changed the title')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()