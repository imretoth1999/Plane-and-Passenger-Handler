'''
Created on 12 Dec 2017

@author: tothi
'''
class PassengersRepo:
    '''
    This is the repository of passengers
    '''


    def __init__(self):
        self.__repo = []
    def addPassenger(self,p):
        for i in range(len(self.__repo)):
            if self.__repo[i].getpassportNr() == p.getpassportNr():
                print('The passenger already exists')
                return None
        self.__repo.append(p)

    def findbyFirstName(self,n):
        l = []
        for elem in self.__repo:
            if elem.getFirstName() == n:
                l.append(elem)
        return l
    def findbyLastName(self,n):
        l = []
        for elem in self.__repo:
            if elem.getLastName() == n:
                l.append(elem)
        return l
    def findbypassportNumber(self,pnr):
        l = []
        for elem in self.__repo:
            if elem.getpassportNr() == pnr:
                l.append(elem)
        return l
    def clearPassengers(self):
        self.__repo.clear()
    def deleteLastPassenger(self):
        self.__repo.pop()
    def deletePassenger(self,index):
        try:
            del self.__repo[index]
        except IndexError:
            print('There was an error while removing the passenger')
    def updateFirstName(self,n,index):
        self.__repo[index].setFirstName(n)
    def updateLastName(self,l,index):
        self.__repo[index].setLastName(l)
    def updatePassportNumber(self,pnr,index):
        self.__repo[index].setpassportNr(pnr)
    def __getitem__(self,index):
        return self.__repo[index]    
    def lenPassengers(self):
        return len(self.__repo)
    def __str__(self):
        '''
        We print the repo
        '''
        s = ''
        for elem in self.__repo:
            s += str(elem) + '\n'
        return s
    def __repr__(self):
        return str(self)   