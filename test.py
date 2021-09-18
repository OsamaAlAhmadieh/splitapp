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











######################################################################3
    #Depricated functions

    def added_group_name(self):

        var = self.name.text()
        grp = group.Group(var)
        self.name.clear()
        self.groupNameWindow.close()

        self.numberOfGroups += 1
        self.AllGroups.append(grp)

        self.newGroupButton = QPushButton(var)
        self.AllGroupButtons.append(self.newGroupButton)
        
        self.layout.addWidget(self.newGroupButton, self.numberOfGroups, 0)

        self.newGroupButton.clicked.connect(self.add_group_members)

    def add_group_members(self):
        selected_group = self.get_current_group()
        print(selected_group)
        print(type(selected_group))
        self.memberName = QLineEdit()
        self.addMemberAddButton = QPushButton('Add member')

        self.addMemberWindow = QWidget()
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.memberName, 0, 0)
        self.gridLayout.addWidget(self.addMemberAddButton, 1, 0)

        self.addMemberWindow.setWindowTitle('Add new Member')
        self.addMemberWindow.setFixedSize(QSize(300, 100))
        self.addMemberWindow.setLayout(self.gridLayout)

        self.addMemberWindow.show()

        self.addMemberAddButton.clicked.connect(lambda: self.added_new_member(selected_group))
        

    def added_new_member(self, selected_group):
        member = self.memberName.text()
        self.memberName.clear()
        current_grp = self.get_current_group(selected_group)
        current_grp.add_member(member)
        print(current_grp)
