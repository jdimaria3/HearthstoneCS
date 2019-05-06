Manuel Marroquin
Joey DiMaria
11/27/17
API Description
Hearthstone 

	Currently our card database API has a self.cards variable, which when loaded
becomes a dict with a unique IDs of a playing card as the key and the list elements of 
the cards such as type, name, cost, health, attack, class, etc. being the value.

	To use this API one must first instanstiate the database by calling a new 
instance of the class, and then call the load_cards function by passing it a file
that contains the image links and card info in json format. Once the database is
populated a number of functions can be called from this API.

	One can print all of the cards in order by calling the print_sorted_cards
function. Or add/delete a new card given an ID and attributes for the given card.
If the user has a unique card dbfId, they can get that card and all of its info
by calling the get_card function. Additionally, this database has functions to
return a list of the cards that are minions, spells, or are between a certain range for
their cost, attack, and health. Additionaly, one can search up cards by class, rarity,
and even name. The get_cards_name function takes in a string and returns a list
of cards whos name matches a part of the string given.

	These functions will facilitate the filtering and searching of the card database
for the following parts of the project, especially for the web server that we intend
to make. 

