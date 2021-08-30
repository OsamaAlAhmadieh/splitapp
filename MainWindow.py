from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLineEdit, QWidget
from PyQt5.QtWidgets import QGridLayout
import sys
import group

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        
        self.setFixedSize(QSize(600, 600))

        self.addGroupButton = QPushButton('Add Group')
        self.addGroupButton.clicked.connect(self.add_group)

        self.layout.addWidget(self.addGroupButton, 0, 0)

        self.setLayout(self.layout)


        # Backend Related Stuff
        self.numberOfGroups = 0
        self.AllGroups = []
        

    def add_group(self):
        self.name = QLineEdit()
        self.addGroupAddButton = QPushButton('Add')

        self.groupNameWindow = QWidget()
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.name, 0, 0)
        self.gridLayout.addWidget(self.addGroupAddButton, 1, 0)

        self.groupNameWindow.setWindowTitle('Create new group')
        self.groupNameWindow.setFixedSize(QSize(200, 100))

        self.groupNameWindow.setLayout(self.gridLayout)
        self.groupNameWindow.show()

        self.addGroupAddButton.clicked.connect(self.added_group_name)

        
    def added_group_name(self):

        var = self.name.text()
        grp = group.Group(var)
        self.name.clear()
        self.groupNameWindow.close()

        self.numberOfGroups += 1
        self.AllGroups.append(grp)

        self.newGroupButton = QPushButton(var)
        self.layout.addWidget(self.newGroupButton, self.numberOfGroups, 0)

        self.newGroupButton.clicked.connect(self.add_group_members)
        
        
    def add_group_members(self):
        selected_group = self.newGroupButton.text()
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


    def get_current_group(self, selected_group):
        for elt in self.AllGroups:
            if elt.name == selected_group:
                return elt


app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()


