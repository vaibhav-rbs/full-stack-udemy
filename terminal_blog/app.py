import menu
from database import Database


Database.initialize()

menu = menu.Menu()
menu.run_menu()

