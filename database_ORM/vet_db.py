import sqlite3, colours
from random import randint

class DatabaseController:

  def __init__(self, path="vet.db"):

    self.__db_path = path
    self.__db = sqlite3.connect(self.__db_path)

  @property
  def db(self):
    return self.__db

  def init_db(self):
    """
    Initialises the database with empty tables
    """

    # First, confirm that the user really does intend to wipe and re-initialise the database
    confirmation_code = str(randint(1000,9999))
    print(f"{colours.RED}WARNING!{colours.END}")
    print(f"This action will erase all data in the database {self.__db_path}!\n")
    
    if input(f"Enter the number {colours.LIGHT_CYAN + confirmation_code + colours.END} to confirm that you wish to proceed, or anything else to quit:\n> ") != confirmation_code:
      return

    # Drop tables and recreate them
    print("\nDeleting tables...",end="")
    print("Done!")
    
    # Create new tables
    print("Creating tables...", end="")
    print("Done!")
    
    # Display 'done' message
    print()
    input("Press any key to continue...")

  def add_test_data(self):
    """
    Inserts a known set of representative test data to the database's tables for the purpose of development and testing.
    """

    pass
  
dbc = DatabaseController()
dbc.init_db()
