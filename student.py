class student(object):

    # Data/Attribute
    def __init__(self, n, a, r):
        self.name = n
        self.age = a
        self.regid = r
        self.marks = {}
        self.avg = 0
        self.rank = 0

        self.initmarks()


    # Associated functions
    def printinfo(self):
        print('NAME: ', self.name)
        print('AGE: ', self.age)
        print('REG ID:', self.regid)
        print('-----------------------------------')
        print('MATHS    : ', self.marks['math'])
        print('PHYSICS  : ', self.marks['phy'])
        print('CHEMISTRY: ', self.marks['chem'])
        print('BIOLOGY  : ', self.marks['bio'])
        print('-----------------------------------')
        print('AVERAGE  : ', self.avg)
        print('RANK     : ', self.rank)
        print('\n\n')

    def initmarks(self):
        for subject in ['phy','chem','math', 'bio']:
            self.marks.setdefault(subject, 0)

    def setmarks(self, sub, marks):
        if(sub in ['phy','chem','math', 'bio'] and str(marks).isdigit()):
            self.marks[sub] = marks
            
        else:
            print('Incorrect subject code')

    def calcaverage(self):
        self.avg = sum(self.marks.values())/len(self.marks.values())

            
    def getaverage(self):
        self.calcaverage()
        return self.avg

    def setrank(self, rank):
        if(str(rank).isdigit()):
            self.rank = rank


###################################################################################

if __name__ == '__main__':

    s1 = student('Vijay', 14, 'HPE007')
    s1.printinfo()
    s1.setmarks('phy', 100)
    s1.setmarks('chem', 100)
    s1.setmarks('math', '%^')
    s1.setmarks('biology', 100)
    s1.printinfo()
    

    s2 = student('Hemanth', 14, 'HPE006')
    s2.printinfo()

    s1.setmarks('math', 88)
    s1.setmarks('bio', 100)
    s1.printinfo()

    s1avg = s1.getaverage()
    if(s1avg > 50):
        s1.setrank(1)

    s1.printinfo()
