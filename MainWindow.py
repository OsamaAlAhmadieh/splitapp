from PyQt5.QtCore import QLine, QSize
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLineEdit, QWidget, QTableWidget, QHeaderView
from PyQt5.QtWidgets import QGridLayout
import sys
import group

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        
        self.setFixedSize(QSize(600, 600))

        self.addGroupButton = QPushButton('Add Group')
        self.addGroupButton.setShortcut(QKeySequence('ctrl+n'))
        self.addGroupButton.clicked.connect(self.create_add_group_window)

        self.displayAllGroupsButton = QPushButton('Display')
        self.displayAllGroupsButton.clicked.connect(self.display_groups_callback)

        self.layout.addWidget(self.addGroupButton, 0, 0)
        self.layout.addWidget(self.displayAllGroupsButton, 0, 1)

        self.setLayout(self.layout)

        # Backend related stuff
        self.total_groups = 0
        self.all_groups = []
        self.MAXGROUPS = 5 

    def create_add_group_window(self):
        self.name = QLineEdit()
        self.addGroupAddButton = QPushButton('Add')
        self.addGroupAddButton.setShortcut(QKeySequence('return'))

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
            grp1 = group.Group(var, [])
            self.name.clear()
            self.groupNameWindow.close()

            self.total_groups += 1 
            self.all_groups.append(grp1)

            self.grp1Button = QPushButton(var)
            self.layout.addWidget(self.grp1Button, self.total_groups, 0)

            #self.grp1Button.clicked.connect(lambda: self.create_add_members_window(grp1.name))
            self.grp1Button.clicked.connect(lambda: self.create_new_window_for_group(grp1.name))

            return
        
        if self.total_groups == 1:
            var = self.name.text()
            grp2 = group.Group(var, [])
            self.name.clear()
            self.groupNameWindow.close()

            self.total_groups += 1
            self.all_groups.append(grp2)

            self.grp2Button = QPushButton(var)
            self.layout.addWidget(self.grp2Button, self.total_groups, 0)

            self.grp2Button.clicked.connect(lambda: self.create_add_members_window(grp2.name))

            return

    def create_add_members_window(self, current_group_name):
        self.memberName = QLineEdit()
        self.addMemberAddButton = QPushButton('Add Member')
        self.addMemberAddButton.setShortcut(QKeySequence('return'))

        self.addMemberWindow = QWidget()
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.memberName, 0, 0)
        self.gridLayout.addWidget(self.addMemberAddButton, 1, 0)

        self.addMemberWindow.setWindowTitle('Add new Member')
        self.addMemberWindow.setFixedSize(QSize(300, 100))
        self.addMemberWindow.setLayout(self.gridLayout)

        self.addMemberWindow.show()

        self.addMemberAddButton.clicked.connect(lambda: self.added_member_name(current_group_name))


    def  added_member_name(self, current_group_name):
        var = self.memberName.text()
        self.memberName.clear()
        current_group, index = self.find_current_group(current_group_name)
        current_group.add_member(var)
        self.all_groups[index] = current_group

    def find_current_group(self, current_group_name):
        for elt in self.all_groups:
            if elt.name == current_group_name:
                return elt, self.all_groups.index(elt)

    def display_groups_callback(self):
        for elt in self.all_groups:
            print(elt.name)
            print(elt.members)


    def create_new_window_for_group(self, current_group_name):
        current_group = self.find_current_group(current_group_name)[0]
        #4 columns: name, paid, owes, and net. 
        self.group_view = QTableWidget(len(current_group.members), 4)
        #self.group_view.setFixedSize(QSize(600,300))
        header = self.group_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.group_view_window = QWidget()
        self.layout_group_view_window = QGridLayout()

        self.layout_group_view_window.addWidget(self.group_view, 0, 0)

        self.group_view_window.setLayout(self.layout_group_view_window)

        self.group_view_window.show()
        

        

    


app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()


