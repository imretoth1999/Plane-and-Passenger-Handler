'''
Created on 18 Dec 2017

@author: tothi
'''
from unittest import TestCase, main
from Repository.PlaneRepo import PlaneRepo
from Domain.Planes import Planes
from Domain.Passengers import Passengers
class PlaneRepoTest(TestCase):


    def testadd(self):
        p = PlaneRepo()
        p1 = Passengers('Ion','Popescu',1)
        p2 = Passengers('Ioana','Popescu',2)
        p3 = Planes('Nume','A101','Wizair',60,'Cairo',[p1,p2])
        p.addPlane(p3)
        self.assertEqual(p.lenPlanes(), 1)
    def testDelete(self):
        p = PlaneRepo()
        p1 = Passengers('Ion','Popescu',1)
        p2 = Passengers('Ioana','Popescu',2)
        p3 = Planes('Nume','A101','Wizair',60,'Cairo',[p1,p2])
        p.addPlane(p3)
        p.deleteLastPlane()
        self.assertEqual(p.lenPlanes(), 0)
    def testUpdate(self):
        p = PlaneRepo()
        p1 = Passengers('Ion','Popescu',1)
        p2 = Passengers('Ioana','Popescu',2)
        p3 = Planes('Nume','A101','Wizair',60,'Cairo',[p1,p2])
        p.addPlane(p3)
        p.updateName('Nume1', 0)
        p.updateNumber('A103', 0)
        p.updateCompany('Wizz', 0)
        p.updateSeats(100, 0)
        p.updateDestination('Lima', 0)
        self.assertEqual(p[0].getName(), 'Nume1')
        self.assertEqual(p[0].getNumber(), 'A103')
        self.assertEqual(p[0].getAirlineCompany(),'Wizz')
        self.assertEqual(p[0].getNumberOfSeats(),100)
        self.assertEqual(p[0].getDestination(),'Lima')
    


if __name__ == "__main__":
    main()