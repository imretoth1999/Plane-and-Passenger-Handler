'''
Created on 18 Dec 2017

@author: tothi
'''
from Domain.Passengers import Passengers
from Domain.Planes import Planes
from UI.UserInput import user_input, string_input
import string
class PlanesMenu():
    def __init__(self,ctrl):
        self.__ctrl = ctrl
    @staticmethod
    def printMenu():
        '''
        We show the menu 
        '''
        print('Input -4 for deleting a plane')
        print('Input -3 for deleting a passenger from a plane')
        print('Input -2 for adding a new plane')
        print('Input -1 for adding a passenger to a plane')
        print("Input 0 for exiting the program")
        print('Input 1 for viewing the planes')
        print('Input 2 for sorting the passengers in a plane by the last name')
        print('Input 3 for sorting the planes by the passengers having a letter')
        print('Input 4 for sorting the planes by concatenating the number of passengers and plane name')
        print('Input 5 for finding all the planes with passengers with the same 3 letters')
        print('Input 6 for finding the passengers in a plane with the first name or the last name a given string')
        print('Input 7 for finding the planes where there is a given name')
        print('Input 8 for forming groups of k passengers from the same plane but with different last names')
        print('Input 9 for forming groups of k planes with the same destination but belonging to different airline companies')
        print(".....................................................")
    def menu(self):
        plane = Planes(string_input(),string_input(),string_input(),user_input(),string_input(),[])
        self.__ctrl.addPlane(plane)
        while True:
            PlanesMenu.printMenu()
            command = user_input()
            if command == -4:
                self.__ctrl.deletePlane(user_input())
            elif command == -3:
                self.__ctrl.deletePassengerinPlane(user_input(),string_input(),string_input())
            elif command == -2:
                plane = Planes(string_input(),string_input(),string_input(),user_input(),string_input(),[])
                self.__ctrl.addPlane(plane)
            elif command == -1:
                self.__ctrl.addPassengerinPlane(string_input(),string_input(),string_input(),string_input(),string_input())
            elif command == 0:
                exit()
            elif command == 1:
                print(self.__ctrl.listPlane())
            elif command == 2:
                self.__ctrl.sortbyLastName()
                print(self.__ctrl.listPlane())
            elif command == 3:
                self.__ctrl.sortbyletter(string_input())
            elif command == 4:
                self.__ctrl.sortbyconcatenation()
            elif command == 5:
                l = self.__ctrl.find_by_nr()
                print(l)
            elif command == 6:
                l = self.__ctrl.find_by_str(user_input(),string_input())
                print(l)
            elif command == 7:
                l = self.__ctrl.find_by_name(string_input(),string_input())
                print(l)
            elif command == 8:
                self.__ctrl.form1(user_input())
            elif command == 9:
                self.__ctrl.form2(user_input())
            else:
                print('Not a valid option')