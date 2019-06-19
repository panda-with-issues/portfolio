"""
Exercise in object oriented programming with Python3
Managing a Business of Restaurants
"""

"""
Defining custom Menu class
"""

class Menu:
  
  #defining a constructor
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items #dict type obj with dish:price mapping
    self.start_time = start_time
    self.end_time = end_time
    
  #defining a string rappresentation of class instances
  def __repr__(self):
    return "{name} menu, available from {start_time} to {end_time}.".format(name=self.name, start_time=self.start_time, end_time=self.end_time)
  
  """
  defining new Menu methods
  """ 
  
  #defining a calculate_bill() method to return the total price of purchased item
  def calculate_bill(self, purchased_items):
    bill = 0
    for i in purchased_items: #list type obj
      bill += self.items.get(i, 0)
    return bill

"""
Defining new custom class Franchise
"""

class Franchise:
  
  #defining a constructor
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus #list type obj containing available menus in franchise
    self.income_of_the_day = 0 #needed for get_income() method
    
  #giving Franchise a string representation
  def __repr__(self):
    return "Restaurant in {}".format(self.address)
  
  """
  Defining new Franchise methods
  """
  
  #defining .available_menus() to return which menu is available at any given time
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    if len(available_menus) != 0:
      print('At {} these menus are available:'.format(time))
      for menu in available_menus:
        print(menu)
    else:
      print("We're sorry, but any menu is available at {}.".format(time))
      
  #defining get_paid() method which store every bill made
  def get_paid(self, menu, purchased_items):
    self.income_of_the_day += menu.calculate_bill(purchased_items)
    return self.income_of_the_day
  
  #defining get_income() which returns a franchise's total income of the day
  def get_income(self):
    return print("The total income of today for {franchise} is {income} $.".format(franchise=self, income=self.income_of_the_day))
  
"""
Defining a new Business class
"""

class Business:
  
  #giving Business a contructor
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises #a list type obj
    
  #making Business iterable in franchises
  def __iter__(self):
    return iter(self.franchises)
    
  """
  Defining new Business methods
  """
  
  #defining a .total_income() method which returns the sum of every franchise's daily income in the business
  def total_income(self):
    total_income = 0
    for franchise in self:
      total_income += franchise.income_of_the_day
    return print("Today the {name} earned {total_income} $.".format(name=self.name, total_income=total_income))
  
  #defining .new_day() method which reset all franchises' incomes to 0 
  def new_day(self):
    for franchise in self:
      franchise.income_of_the_day = 0
    return franchise.income_of_the_day

"""
Testing the code
"""

#instanciating 5 Menu objects
brunch = Menu(#
  "Brunch",
  {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},
  11,
  16)

early_bird = Menu(#
  "Early-bird Dinners", 
  {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00},
  15,
  18)

dinner = Menu(#
  "Dinner",
  {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00},
  17,
  23)

kids = Menu(#
  "Kids Menu",
  {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00},
  11,
  21)

arepas = Menu(#
  "Take a' Arepa",
  {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50},
10,
20)

#testing Menu's string represantation
print(arepas)

#testing .calculate_bill() method
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#instanciating 3 Franchise objects
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas])

#testing Franchise's string representation
print(flagship_store)

#testing .available_menus() method
flagship_store.available_menus(12)
new_installment.available_menus(17)
flagship_store.available_menus(3)

#testing get_paid() and get_income() method
flagship_store.get_paid(brunch, ['pancakes', 'home fries', 'coffee'])
flagship_store.get_paid(early_bird, ['salumeria plate', 'mushroom ravioli (vegan)'])

new_installment.get_paid(kids, ['chicken nuggets', 'apple juice'])

flagship_store.get_income()
new_installment.get_income()
arepas_place.get_income()

#instanciating 2 Business object
old_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
new_business = Business("Take a' Arepa", [arepas_place])

#testing .total_income method
old_business.total_income()
new_business.total_income()

#testing new_day() method
old_business.new_day()
old_business.total_income()
