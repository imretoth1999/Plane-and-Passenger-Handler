'''
Created on 18 Dec 2017

@author: tothi
'''
from unittest import TestCase, main
from Domain.Passengers import Passengers
class TestPassenger(TestCase):

    def testGetersAndSeters(self):
        p = Passengers('Ion','Pop',33)
        self.assertEqual(p.getFirstName(), 'Ion')
        self.assertEqual(p.getLastName(),'Pop')
        self.assertEqual(p.getpassportNr(), 33)
        p.setFirstName('Ioana')
        p.setLastName('Popescu')
        p.setpassportNr('100423')
        self.assertEqual(p.getFirstName(), 'Ioana')
        self.assertEqual(p.getLastName(), 'Popescu')
        self.assertEqual(p.getpassportNr(), '100423')


if __name__ == "__main__":
    main()