'''
Created on 18 Dec 2017

@author: tothi
'''
from Domain.Passengers import Passengers
from Utils.Sort_Search_Backtracking import isSorted, isSearched, mybacktracking
from Utils.Functions import firstnameletter_comp, lastname_comp, concatenation_comp, find_by_first_letters, find_by_string, find_by_name, formPassengerswithDifferentLastNames, formPLanesWithSameDestinationbutDifferentAirline, returnValue
class Controller:
    '''
    This class controles all the operations
    '''
    def __init__(self, planerepo,passengerrepo):
        '''
        We initialise the repositories
        '''
        self.__passengerrepo = passengerrepo
        self.__planerepo = planerepo
    def addPassengerinPlane(self,fname,lname,pnr,number,company):
        '''
        We add a passenger in a plane
        '''
        p = Passengers(fname,lname,pnr)
        l1 = self.__passengerrepo.lenPassengers()
        self.__passengerrepo.addPassenger(p)
        l2 = self.__passengerrepo.lenPassengers()
        if l1 == l2:
            return None
        for i in range(self.__planerepo.lenPlanes()):
            if self.__planerepo[i].getNumber() == number and self.__planerepo[i].getAirlineCompany() == company:
                l = self.__planerepo[i].getPassengers()
                l.append(p)
                self.__planerepo[i].setPassengers(l)
                return None
    def deletePassengerinPlane(self,pnr,number,company):
        '''
        We delete a passenger in a plane
        '''
        for i in range(self.__planerepo.lenPlanes()):
                if self.__planerepo[i].getNumber() == number and self.__planerepo[i].getAirlineCompany() == company:
                    l = self.__planerepo[i].getPassengers()
                    for i in range(len(l)):
                        if l[i].getpassportNr() == pnr:
                            del l[i]
                            return None
    def sortbyLastName(self):
        '''
        We sort the passenger by their last name
        '''
        for i in range(len(self.__planerepo)):
            isSorted(self.__planerepo[i].getPassengers(), lastname_comp,0)
    def sortbyletter(self,l):
        '''
        We sort the planes by a given letter
        '''
        isSorted(self.__planerepo,firstnameletter_comp,l)
    def sortbyconcatenation(self):
        '''
        We sort by concatenating the number of passengers with the number of the plane
        '''
        isSorted(self.__planerepo, concatenation_comp,0)
    def form1(self,k):
        '''
        We form groups of k passengers from the same plane but with different last names (k is a
value given by the user) 
        '''
        for elem in self.__planerepo:
            for i in mybacktracking(elem.getPassengers(), k, formPassengerswithDifferentLastNames):
                print(returnValue(i, elem.getPassengers()))
    def form2(self,k):
        '''
        Form groups of k planes with the same destination but belonging to different airline
companies (k is a value given by the user)
        '''
        for i in mybacktracking(self.__planerepo, k, formPLanesWithSameDestinationbutDifferentAirline):
            print(returnValue(i, self.__planerepo))
    def find_by_nr(self):
        '''
        We find the planes containing all the passengers with the same 3 letters from the passport number
        '''
        return isSearched(self.__planerepo,find_by_first_letters , 0)
    def find_by_str(self,index,s):
        try:
            return isSearched(self.__planerepo[index] ,find_by_string, [s])
        except IndexError:
            print('Inexistent plane')
    def find_by_name(self,f,l):
        return isSearched(self.__planerepo,find_by_name, [f,l])
    def addPlane(self,p):
        '''
        We add a plane
        '''
        self.__planerepo.addPlane(p)
    def deletePlane(self,index):
        '''
        We delete a plane
        '''
        self.__planerepo.deletePlane(index)
    def listPlane(self):
        '''
        We list the planes
        '''
        return self.__planerepo
    def listRepo(self):
        '''
        We list the repository
        '''
        self.__planerepo.getPlanesforTest().printRepo()
    def sortwithletter(self,l):
        '''
        We sort the planes by a given letter
        '''
        self.__planerepo = isSorted(self.__planerepo.getrepo(),firstnameletter_comp,l)
    def sortwithconcatenation(self):
        '''
        We sort by concatenating the number of passengers with the number of the plane
        '''
        self.__planerepo = isSorted(self.__planerepo.getrepo(), concatenation_comp,0)
        
    def getPlanes(self):
        '''
        We get the planes
        '''
        return self.__planerepo.getrepo()
    def getPlanesforTest(self):
        '''
        We get the planes for testing ! this function is for testing only
        '''
        return self.__planerepo
    def getPassengers(self):
        '''
        We get the passengers
        '''
        return self.__planerepo.getrepo()
        