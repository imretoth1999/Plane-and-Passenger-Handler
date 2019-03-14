'''
Created on 18 Dec 2017

@author: tothi
'''
def concatenation_comp(a,b,l):
            p1 = len(a.getPassengers())
            p2 = len(b.getPassengers())
            s1 = str(p1) + a.getNumber()
            s2 = str(p2) + b.getNumber()
            if s1 > s2:
                return False
            return True
def lastname_comp(a,b,l):
            if a.getLastName() > b.getLastName():
                return False
            return True
def firstnameletter_comp(a,b,l):
            if a.numberofPassengerswithagivenletter(l) > b.numberofPassengerswithagivenletter(l):
                return False
            return True
def find_by_first_letters(a,param):
    l = a.getPassengers()
    identify = l[0].getpassportNr()[0:3]
    for i in range(1,len(l)):
        if  l[i].getpassportNr()[0:3] is not identify:
            return False
    return True
def find_by_string(a,param):
    for i in range(len(a)):
        if a[i].getFirstName() in param[0] or a[i].getLastName() in param[0]:
            return True
    return False
def find_by_name(a,param):
    l = a.getPassengers()
    for i in range(len(l)):
        if l[i].getFirstName() == param[0] and l[i].getLastName() == param[1]:
            return True
    return False
def  formPassengerswithDifferentLastNames(sol,l):
    for i in range(len(sol)-1):
        if l[sol[i]].getLastName()==l[sol[len(sol)-1]].getLastName():
            return False
    return True
def formPLanesWithSameDestinationbutDifferentAirline(sol,l):
    for i in range(len(sol)-1):
        if (not l[sol[i]].getDestination() == l[sol[len(sol)-1]].getDestination()) or (l[sol[i]].getAirlineCompany() == l[sol[len(sol)-1]].getAirlineCompany()):
            return False
    return True
def returnValue(sol,repo):
    newList=[]
    for el in sol:
        newList.append(repo[el].getName())
    return newList