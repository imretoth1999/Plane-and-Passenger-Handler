'''
Created on 12 Dec 2017

@author: tothi
'''

class Passengers:
    '''
    Every passenger is identified by first name,last name and passport number
    '''
    def __init__(self, f,l, pnr):
        '''
        we initialise the class
        '''
        self.__firstName = f
        self.__lastName = l 
        self.__passportNr = pnr
    def getFirstName(self):
        '''
        We get the first name
        '''
        return self.__firstName
    def getLastName(self):
        '''
        We get the last name
        '''
        return self.__lastName
    def getpassportNr(self):
        '''
        We get the passport number
        '''
        return self.__passportNr
    def setFirstName(self,f):
        '''
        We set the first name
        '''
        self.__firstName = f
    def setLastName(self,l):
        '''
        We set the last name
        '''
        self.__lastName = l
    def setpassportNr(self,pnr):
        '''
        We set the passport number
        '''
        self.__passportNr = pnr
    def getName(self):
        return self.__firstName + ' ' + self.__lastName
    def __str__(self):
        return self.__firstName + ', '+ self.__lastName + ' - ' + str(self.__passportNr)