from PyQt5.QtCore import QLine, QSize
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
        self.addGroupButton.clicked.connect(self.create_add_group_window)

        self.layout.addWidget(self.addGroupButton, 0, 0)

        self.setLayout(self.layout)

        # Backend related stuff
        self.total_groups = 0
        self.all_groups = []
        self.MAXGROUPS = 5 

    def create_add_group_window(self):
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

        self.addGroupAddButton.clicked.connect(self.add_group_name)
        

    def add_group_name(self):
        
        if self.total_groups == 0:
            var = self.name.text()
            grp1 = group.Group(var)
            self.name.clear()
            self.groupNameWindow.close()

            self.total_groups += 1 
            self.all_groups.append(grp1)

            self.grp1Button = QPushButton(var)
            self.layout.addWidget(self.grp1Button, self.total_groups, 0)

            self.grp1Button.clicked.connect(lambda: self.create_add_members_window(grp1.name))

            return
        
        if self.total_groups == 1:
            var = self.name.text()
            grp2 = group.Group(var)
            self.name.clear()
            self.groupNameWindow.close()

            self.total_groups += 1
            self.all_groups.append(grp2)

            self.grp2Button = QPushButton(var)
            self.layout.addWidget(self.grp2Button, self.total_groups, 0)

            self.grp2Button.clicked.connect(lambda: self.create_add_members_window(grp2.name))

            return

    def create_add_members_window(self, extra_arg):

        print(extra_arg)

        self.memberName = QLineEdit()
        self.addMemberAddButton = QPushButton('Add Member')

        self.addMemberWindow = QWidget()
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.memberName, 0, 0)
        self.gridLayout.addWidget(self.addMemberAddButton, 1, 0)

        self.addMemberWindow.setWindowTitle('Add new Member')
        self.addMemberWindow.setFixedSize(QSize(300, 100))
        self.addMemberWindow.setLayout(self.gridLayout)

        self.addMemberWindow.show()

        self.addMemberAddButton.clicked.conenct(self.added_gr)


app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()


