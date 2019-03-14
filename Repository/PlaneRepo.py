'''
Created on 12 Dec 2017

@author: tothi
'''

class PlaneRepo:
    '''
    This is the repository of the Passengers class
    '''
    def __init__(self):
        self.__repo = []
    def addPlane(self,p):
        '''
        We add a new plane
        Restriction: We don't add the plane if it already exists  
        '''
        for elem in self.__repo:
            if elem.getNumber() == p.getNumber():
                print('There plane already exists ')
        self.__repo.append(p)
    def findbyname(self,n):
        '''
        We find a plane by the name
        '''
        l = []
        for elem in self.__repo:
            if elem.getName() == n:
                l.append(elem)
        return l
    def findbynumber(self,n):
        '''
        We find a plane by the number
        '''
        l = []
        for elem in self.__repo:
            if elem.getNumber() == n:
                l.append(elem)
        return l
    '''
    def findNr(self, n, source, start):
        if len(source) <= start:
            return -1
        elif n == self.__repo[start].getNumber():
            return start
        else:
            return findNr(n, source, start + 1)
    '''
    def clearPlanes(self):
        '''
        We clear the planes
        '''
        self.__repo.clear()
    def deleteLastPlane(self):
        '''
        We delete the last plane
        '''
        self.__repo.pop()
    def deletePlane(self,index):
        '''
        We delete a plane
        '''
        try:
            del self.__repo[index]
        except IndexError:
            print('There was an error while removing the plane')
    def updateName(self,n,index):
        '''
        We update the name
        '''
        self.__repo[index].setName(n)
    def updateNumber(self,nr,index):
        '''
        We update the number
        '''
        self.__repo[index].setNumber(nr)
    def updateCompany(self,c,index):
        '''
        We update the company
        '''
        self.__repo[index].setAirlineCompany(c)
    def updateSeats(self,nr,index):
        '''
        We update the seats
        '''
        self.__repo[index].setNumberOfSeats(nr)
    def updateDestination(self,d,index):
        '''
        We update the destination
        '''
        self.__repo[index].setDestination(d)
    def updatePassengersFirstName(self,n,index):
        '''
        We update the passengers first name
        '''
        self.__repo[index].setFirstName(n)
    def updatePassengersLastName(self,n,index):
        '''
        We update the passengers last name
        '''
        self.__repo[index].setLastName(n)
    def updatePassengersPassportId(self,n,index):
        '''
        We update passengers passport id
        '''
        self.__repo[index].setpassportNr(n)
    def __getitem__(self,index):
        return self.__repo[index]
    def __setitem(self,index,thing):
        self.__repo[index] = thing
        return self.__repo[index]
    def getrepo(self):
        '''
        We get the repo
        '''
        return self.__repo
    def lenPlanes(self):
        '''
        We get the len of the plane
        '''
        return len(self.__repo)
    def __len__(self):
        return len(self.__repo)
    def __repr__(self):
        return str(self)
    def __str__(self):
        '''
        We print the repo
        '''
        s = ''
        for elem in self.__repo:
            s += str(elem) + '\n'
        return s