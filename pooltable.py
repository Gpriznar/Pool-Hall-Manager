### JSON and Files ###

import json

file_object = open("tables.txt", "w")

pool_tables = []

import time
import datetime
from datetime import date
from pool import title_menu
localtime = time.asctime( time.localtime(time.time()) )

title_menu()

### Class ###

class PoolTable:
  def __init__(self,table_no):
    self.table_no = table_no
    self.is_available = "Available"
    self.start_time = 0
    self.end_time = 0
    self.total_time = 0
    self.display_start_time = time.time()
    self.display_end_time = time.time()
    self.cost = 0

  def __repr__(self):
      return(f"{self.table_no} is {self.is_available}")

  def check_out(self):
          now = datetime.datetime.now()
          self.is_available = ("** Occupied **")
          self.start_time = now.strftime("%H:%M:%S")
          self.display_start_time = time.time()


  def check_in(self):
          now = datetime.datetime.now()
          self.is_available = ("Available")
          self.end_time = now.strftime("%H:%M:%S")
          self.display_end_time = time.time()
          number_total_time = (self.display_end_time - self.display_start_time)/60
          self.total_time = round(number_total_time)
          self.cost = round(number_total_time * .50)
          with open("tables.txt","a") as file_object:
              file_object.write(f"""
              ***********************************
              Table: {self.table_no}
              Start Time: {self.start_time}
              End Time: {self.end_time}
              Minutes in use: {self.total_time}
              Cost ${self.cost}
              ***********************************
              """)

### Functions ###

def return_table():
    pool_table_menu()
    user_input = int(input("""
    Which table would you like to return: """))
    table_choice = user_input - 1
    pool_table = pool_tables[table_choice]
    pool_table.check_in()


def pool_table_menu():
      for pool_table in pool_tables:
          print(f"""
          ┬──┬﻿ Table: {pool_table}
          """)

for index in range(1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

### Conditionals ###

user_input = ""

while user_input != 0:
    pool_table_menu()
    user_input = int(input("""
        Select a table number, press 99 to return a table, or press 0 to quit application: """))
    if user_input in range(1,13):
        table_choice = user_input - 1
        pool_table = pool_tables[table_choice]
        pool_table.check_out()
    elif user_input == 99:
        return_table()
    if user_input == 0:
        print("""

                   _____  ____   ____  _____  ___ __     __ _____
                  / ____|/ __ \ / __ \|  __ \|  _ \ \   / /  ____|
                 | |  __| |  | | |  | | |  | | |_) \ \_/ /| |__
                 | | |_ | |  | | |  | | |  | |  _ < \   / |  __|
                 | |__| | |__| | |__| | |__| | |_) | | |  | |____
                  \_____|\____/ \____/|_____/|____/  |_|  |______|

        """)
        break
