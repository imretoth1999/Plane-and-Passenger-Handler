'''
Created on 18 Dec 2017

@author: tothi
'''
from unittest import TestCase, main
from Domain.Planes import Planes
from Domain.Passengers import Passengers
class PlaneTest(TestCase):


    def testGettersSetters(self):
        p1 = Passengers('Ion','Popescu',1)
        p2 = Passengers('Ioana','Popescu',2)
        p = Planes('Nume','A101','Wizair',60,'Cairo',[p1,p2])
        self.assertEqual(p.getName(), 'Nume')
        self.assertEqual(p.getNumber(), 'A101')
        self.assertEqual(p.getAirlineCompany(), 'Wizair')
        self.assertEqual(p.getNumberOfSeats(), 60)
        self.assertEqual(p.getDestination(), 'Cairo')
        self.assertEqual(p.getPassengers(), [p1,p2])
        p.setName('Nume1')
        p.setNumber('A102')
        p.setAirlineCompany('Wizz')
        p.setNumberOfSeats(30)
        p.setDestination('Lima')
        p.setPassengers([p2,p1])
        self.assertEqual(p.getName(), 'Nume1')
        self.assertEqual(p.getNumber(), 'A102')
        self.assertEqual(p.getAirlineCompany(), 'Wizz')
        self.assertEqual(p.getNumberOfSeats(), 30)
        self.assertEqual(p.getDestination(), 'Lima')
        self.assertEqual(p.getPassengers(), [p2,p1])

if __name__ == "__main__":

    main()