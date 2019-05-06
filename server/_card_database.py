# Manuel Marroquin
# Hearthstone Card Database
# 11/23/17

import json

# the default img if no link available for card
defaultImg="http://media-hearth.cursecdn.com/attachments/0/612/blizzcon-mystery-minion-template.png"

class _card_database:
    def __init__(self):
        self.cards=dict()
    
    # Loads the cards dict dbfid key list of attributes as value
    def load_cards(self, card_file, img_file):
        json_data=open(card_file)
        cards= json.load(json_data)
        for card in cards:
            if "dbfId" in card and "rarity" in card:
                imgLink=self.get_img_link(card["dbfId"], "./images.json")
                # If spell then no health and attack attributes
                if card["type"]=="SPELL":
                    self.cards[int(card["dbfId"])]= [card["type"],card["name"],
                               card["cost"], card["rarity"], card["cardClass"],
                               imgLink]
                # if minion then add health and attack attribute
                elif card["type"]=="MINION":
                    self.cards[int(card["dbfId"])]= [card["type"],card["name"],
                               card["cost"], card["rarity"], card["cardClass"],
                               card["attack"],card["health"],
                               imgLink]                   
        json_data.close()

    # Function that gets img link of given card ID if it exist in given file
    def get_img_link(self,dbfId,img_file):
        json_data=open(img_file)
        links=json.load(json_data)
        for link in links:
            if(link["dbfId"]==dbfId):
                json_data.close()
                return (link["url"])
        json_data.close()
        return(" ")

    def get_cards(self):
        IDList=list()
        for dbfId in self.cards:
            IDList.append(int(dbfId))
        return IDList

    # Returns List of attributes for card dbfId if it exist
    def get_card(self, dbfId):
        output=dict()
        if dbfId in self.cards:

            if self.cards[dbfId][0]=="SPELL":
                output["dbfId"]=int(dbfId)
                output["type"]=self.cards[dbfId][0]
                output["name"]=self.cards[dbfId][1]
                output["cost"]=self.cards[dbfId][2]
                output["rarity"]=self.cards[dbfId][3]
                output["class"]=self.cards[dbfId][4]
                output["url"]=self.cards[dbfId][5]
            else:
                output["dbfId"]=int(dbfId)
                output["type"]=self.cards[dbfId][0]
                output["name"]=self.cards[dbfId][1]
                output["cost"]=self.cards[dbfId][2]
                output["rarity"]=self.cards[dbfId][3]
                output["class"]=self.cards[dbfId][4]
                output["attack"]=self.cards[dbfId][5]
                output["health"]=self.cards[dbfId][6]
                output["url"]=self.cards[dbfId][7]                   
            return(output)
        else:
            return(None)

    # Return all cards that are minions
    def get_minions(self):
        myList=list()
        for dbfId in self.cards:
           if(self.cards[dbfId][0]=="MINION"):
               myList.append(self.get_card(dbfId))
        return myList

    # Return all cards that are spells
    def get_spells(self):
        myList=list()
        for dbfId in self.cards:
            if(self.cards[dbfId][0]=="SPELL"):
                myList.append(self.get_card(dbfId))
        return myList

    # Get cards by name
    def get_cards_name(self, NAME):
        myList=list()
        for dbfId in self.cards:
            if ( NAME.lower() in self.cards[dbfId][1].lower()):
                myList.append(self.get_card(dbfId))
        return myList

    # Returns cards of given rarity
    def get_cards_rarity(self, RARITY):
        myList=list()
        for dbfId in self.cards:
            if (self.cards[dbfId][3].lower() == RARITY.lower()):
                myList.append(self.get_card(dbfId))
        return myList

    # Returns cards of given class
    def get_cards_class(self, CLASS):
        myList=list()
        for dbfId in self.cards:
            if (self.cards[dbfId][4].lower() == CLASS.lower()):
                myList.append(self.get_card(dbfId))
        return myList

    # Return cards that are in a given range
    def get_cards_costRange(self,low, high):
        myList=list()
        for dbfId in self.cards:
            if (self.cards[dbfId][2] >= low and self.cards[dbfId][2] <= high):
                myList.append(self.get_card(dbfId))
        return myList
    # Return minions with health withing a given range
    def get_minions_healthRange(self, low, high):
        myList=list()
        for dbfId in self.cards:
            # if minion
            if self.cards[dbfId][0]=="MINION":
                if(self.cards[dbfId][6]>=low and self.cards[dbfId][6]<=high):
                    myList.append(self.get_card(dbfId))
        return myList
    # Return minions withing a given attack range.
    def get_minions_attackRange(self, low, high):
        myList=list()
        for dbfId in self.cards:
            # if minion
            if self.cards[dbfId][0]=="MINION":
                if(self.cards[dbfId][5]>=low and self.cards[dbfId][5]<=high):
                    myList.append(self.get_card(dbfId))
        return myList
            
    # Prints Cards sorted by dfId
    def print_sorted_cards(self):
        for dbfId in self.cards:
            print(dbfId, self.cards(dbfId))

    # Creates/updates a card given dbfId and a list
    def set_card(self, dbfId, mylist):
        if dbfId in self.cards:
            self.cards[dbfId]=mylist
        else:
            self.cards.update({dbfId:mylist})

    # Deletes card given dbfId
    def delete_card(self, dbfId):
        if dbfId in self.cards:
            del self.cards[dbfId]
            return({"result":"success"})
        return({"result": "error"})
        

#if __name__ == "__main__":   
    #newDatabase= _card_database()
    #newDatabase.load_cards("./cards.json", "./images.json")
    #newDatabase.print_sorted_cards()
    #print(newDatabase.get_spells())
    #print(newDatabase.get_minions())
    #print(newDatabase.get_card(559))
    #print(newDatabase.get_cards_costRange(11,30))
    #print(newDatabase.get_minions_attackRange(9,10))
    #print(newDatabase.get_cards_name("GIANT"))
    #print(newDatabase.get_cards_rarity("FREE"))
    #print(newDatabase.get_cards_class("SHAMAN"))
