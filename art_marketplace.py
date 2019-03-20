"""
Creating and managing an art marketplace
Exercise with object oriented programmation in Python3
"""
"""
Importing libraries
"""

from datetime import datetime

"""
Defining new classes
"""

class Art:

    #giving Art a constructor
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = str(year)
        self.owner = owner
    
    #giving Art a string representation
    def __str__(self):
        return "{artist}. \"{title}\". {year}, {medium}. {owner}, {location}.".format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner=self.owner.name, location=self.owner.location)

class Marketplace:

    #giving Marketplace a constructor
    def __init__(self):
        self.listings = [] #contains work of art to sell

    #defining a new method .add_listing(), which add his argument to the listing of arts to be sold
    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    #defining a new method .remove_listing(). It removes its argument from the listing of art to be sold
    def remove_listing(self, listing_sold):
        self.listings.remove(listing_sold)

    #defining a new method .show_listing(). It show every piece of art into the listing
    def show_listing(self):
        if len(self.listings) == 0:
            print("There are no listings.")
        else:
            print("Currently there are these listings available:")
            for listing in self.listings:
                print(listing)
        
    #defining a new .check_expired_listing method. It checks for expired listings and removes them from listings' list
    def check_expired_listing(self):
        for listing in self.listings:
            time_up = datetime.now() - listing.creation_time
            if time_up.days >= 31:
                self.listings.remove(listing)

class Client:

    #giving Client a constructor
    def __init__(self, name, location, is_museum, wallet=0):
        self.name = name
        self.is_museum = is_museum #bool type
        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"
        self.wallet = wallet
        self.wishlist = []
    
    #defining a new .whish() method which adds its argument to client's whishlist
    def wish(self, art):
        self.wishlist.append(art)

    #defining a new .show_wishlist() method which prints client's wishlist's items
    def show_wishlist(self):
        if len(self.wishlist) == 0:
            print("{}'s wishlist is empty".format(self.name))
        else:
            print("Showing {}'s wishlist:".format(self.name))
            for art in self.wishlist:
                print(art)
        

    #defining a new .sell_artwork() method. This:
    #1. checks if the seller actually possess what they are going to sell
    #2. creates a Listing object with its argument
    #3. adds that object to the marketplace
    #4. update client's wallet
    def sell_artwork(self, art, price, date_of_selling):
        if art.owner == self:
            new_listing = Listing(art, price, self, date_of_selling)
            veneer.add_listing(new_listing)
            self.wallet += price

    #defining a new .buy_art() method, which:
    #1.    checks whether the client doesn't own the art to be bought and
    #2.    checks whether exists an art's listing in marketplace's listings
    #2a-1. if true, proceeds with transaction
    #2a-2. if art were in client's wishlist, removes it
    def buy_art(self, art):
        #1
        if self != art.owner:
            #2
            for listing in veneer.listings:
                if art == listing.art:
                    art.owner = self
                    veneer.remove_listing(listing)
                    self.wallet -= listing.parsed_price
                    if art in self.wishlist:
                        self.wishlist.remove(art)
                    break

class Listing:

    #giving Listing a constructor
    def __init__(self, art, price, seller, creation_time):
        self.art = art
        self.price = str(price) + " $"
        self.parsed_price = price
        self.seller = seller
        self.creation_time = creation_time #a datetime obj

    #giving List a string representation
    def __str__(self):
        return "{art}, {price}.".format(art=self.art.title, price=self.price)

"""
Testing the code
"""

#instantiating a new Marketplace object
veneer = Marketplace()

#testing .show_listing()
veneer.show_listing()

#instantiating 2 Client objects
edytta = Client("Edytta Halpirt", None, False)
moma = Client("The MOMA", "New York", True, 100000000)

#instanciating a work of art as Art object
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

#testing Art's string representation
print(girl_with_mandolin)

#testing .wish() and .show_wishlist methods
moma.wish(girl_with_mandolin)
moma.show_wishlist()

#testing .sell_artwork() method
edytta.sell_artwork(girl_with_mandolin, 6000000, datetime(2019, 3, 20))
veneer.show_listing()
print(edytta.wallet)

#testing .buy_artwork() method
moma.buy_art(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listing()
print(moma.wallet, moma.wishlist)

#testing .check_expired_listing() method
expired_listing = Listing(girl_with_mandolin, 5, moma, datetime(2019, 2, 14))
veneer.add_listing(expired_listing)
veneer.show_listing()
print("Looking for expired listing...")
veneer.check_expired_listing()
veneer.show_listing()
