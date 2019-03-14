'''
Created on 18 Dec 2017

@author: tothi
'''
from unittest import TestCase, main
from Repository.PassengersRepo import PassengersRepo
from Domain.Passengers import Passengers
class PassengerRepoTest(TestCase):

    
    def testadd(self):
        p = PassengersRepo()
        p.addPassenger(Passengers('Ion','Popescu',340))
        self.assertEqual(p.lenPassengers(), 1)
    def testDelete(self):
        p = PassengersRepo()
        p.addPassenger(Passengers('Ion','Popescu',340))
        p.deleteLastPassenger()
        self.assertEqual(p.lenPassengers(), 0)
    def testUpdate(self):
        p = PassengersRepo()
        p.addPassenger(Passengers('Ion','Popescu',340))
        p.addPassenger(Passengers('Ioana','Pop',10))
        p.updateFirstName('Andrei', 1)
        p.updateLastName('Ln', 1)
        p.updatePassportNumber(30, 0)
        self.assertEqual(p[0].getpassportNr(),30)
        self.assertEqual(p[1].getFirstName(),'Andrei')
        self.assertEqual(p[1].getLastName(), 'Ln')

if __name__ == "__main__":
    main()