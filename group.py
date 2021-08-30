class Group():

    def __init__(self, groupName, members=[]):
        self.name = groupName
        self.members = members
        self.totalMembers = len(members)

    def __str__(self):
        count = 0
        individual_members = ''
        for name in self.members:
            if count == self.totalMembers - 1 and count != 0:
                individual_members = individual_members + 'and ' + name + '.'
            else:
                individual_members = individual_members + name + ', '
                count += 1
            
        return 'The group called ' + self.name + ' has the following members: ' + individual_members

    def add_member(self, memberName):
        assert(isinstance(memberName,str))
        self.members.append(memberName)
        self.totalMembers += 1

group1 = Group('myGroup',['osama','karoly'])

if __name__ == '__main__':

    group1.add_member('Waleedbayk')
    print(group1.totalMembers)
    print(group1.members)
    print(group1)