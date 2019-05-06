#pseudocode for the javascript implementation of our searches

#init stuff - variables
var type
var class
var rarity

#sets type variable based on type radio button group
def getType() {
	if allB == 1
		type = "ALL" #just not set variable?
	else if spellsB == 1
		type = "SPELL"
	else if minionB == 1
		type = "MINION"
}

#sets class variable based on class radio button group
def getClass() {
	if druidB == 1
		class = "DRUID"
	else if hunterB == 1
		class = "HUNTER"
	else if mageB == 1
		class = "MAGE"
	else if palB == 1
		class = "PALADIN"
	else if priestB == 1
		class = "PRIEST"
	else if rogueB == 1
		class = "ROGUE"
	else if shamB == 1
		class = "SHAMAN"
	else if warlB == 1
		class = "WARLOCK"
	else if warrB == 1
		class = "WARRIOR"
	else if allB == 1
		class = "NEUTRAL" #all
}

#sets rarity variable based on rarity radio button group
def getRarity() {
	if freeB == 1
		rarity = "FREE" #basic?
	else if commB == 1
		rarity = "COMMON"
	else if rareB == 1
		rarity = "RARE"
	else if epicB == 1
		rarity == "EPIC"
	else if legendB == 1
		rarity == "LEGENDARY"
	else if allB == 1
		rarity = "ALL" #just not set variable?
}

#compares two dictionaries and returns dict with shared items
def compareDicts(dict1, dict2) {
	newDict = {}
	for key in dict1:
		if key in dict2:
			newDict[key] = dict1[key]
	return newDict
}

#performs filter operation; passes all dicts through comparison function
def filter() {
	typeDict = {}   #get_Type function in CDB
	classDict = {}  #get_Class function in CDB
	rarityDict = {} #get_Rarity function in CDB
	costDict = {}	#get_Cost function in CDB
	attackDict = {}	#get_Attack function in CDB
	healthDict = {} #get_Health function in CDB
	
	if type == "SPELL" or type == "ALL":
		netDict = compareDicts(compareDicts(typeDict, classDict), 
								compareDicts(rarityDict, costDict))
	else if type == "MINION":
		netDict = compareDicts(compareDicts(typeDict, classDict),
							compareDicts(compareDicts(rarityDict, costDict)
										compareDicts(attackDict, healthDict)))
}
