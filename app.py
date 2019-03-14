'''
Created on 18 Dec 2017

@author: tothi
'''
from Repository.PassengersRepo import PassengersRepo
from Repository.PlaneRepo import PlaneRepo
from Controller.Controller import Controller
from UI.Menu import PlanesMenu
def start():
    repo1 = PassengersRepo()
    repo2 = PlaneRepo()
    ctrl = Controller(repo2,repo1)
    ui = PlanesMenu(ctrl)
    ui.menu()
start()