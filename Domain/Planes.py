'''
Created on 12 Dec 2017

@author: tothi
'''

class Planes:
    '''
    Planes are identified by name, number, airline company,number of seats, destination, list of passengers
    '''


    def __init__(self, name,number,company,seats,destination,passengers):
        '''
        We initialise the plane
        '''
        self.__name = name
        self.__number = number
        self.__airlineCompany = company
        self.__numberOfSeats = seats
        self.__destination = destination
        self.__passengers = passengers
    def getName(self):
        '''
        We get the name of the plane
        '''
        return self.__name
    def getNumber(self):
        '''
        We get the number of the plane
        '''
        return self.__number
    def getAirlineCompany(self):
        '''
        We get the airline company
        '''
        return self.__airlineCompany
    def getNumberOfSeats(self):
        '''
        We get the number of seats
        '''
        return self.__numberOfSeats
    def getDestination(self):
        '''
        We get the destination
        '''
        return self.__destination
    def getPassengers(self):
        '''
        We get the passengers
        '''
        return self.__passengers
    def setName(self,name):
        '''
        we set the name
        '''
        self.__name = name
    def setNumber(self,nr):
        '''
        We set the number
        '''
        self.__number = nr
    def setAirlineCompany(self,company):
        '''
        We set the Airline company
        '''
        self.__airlineCompany = company
    def setNumberOfSeats(self,seats):
        '''
        We set the number of seats
        '''
        self.__numberOfSeats = seats
    def setDestination(self,d):
        '''
        We set the destination
        '''
        self.__destination = d
    def setPassengers(self,p):
        '''
        We set the passengers
        '''
        self.__passengers = p
    def numberofPassengerswithagivenletter(self,l):
        '''
        We get the number of passengers with a given letter
        '''
        k = 0
        for elem in self.__passengers:
            if elem.getFirstName()[0] == l:
                k+=1
        return k
    def __str__(self):
        return self.__name + ', ' + self.__number + ', ' + self.__airlineCompany + ', ' + str(self.__numberOfSeats) + ', ' + self.__destination + ', ' + str(self.__passengers)
    def __repr__(self):
        return str(self)
    def __len__(self):
        i = 0
        for elem in self.__passengers:
            i+=1
        return i
    def __getitem__(self,index):
        return self.__passengers[index]