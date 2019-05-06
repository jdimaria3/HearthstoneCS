import cherrypy
import re, json

from _card_database import _card_database



class OptionsController(object):
     def __init__(self):
        print("starting Options Controller")

     def OPTIONS(self, *args, **kargs):
         return ""


class CardsController(object):
    def __init__(self, cdb=None):
        self.cdb = cdb

    def GET(self):
        output=dict()
        dbfIdList=self.cdb.get_cards()
        dictList=list()
        output["result"]= "success"
        for dbfId in dbfIdList:
             dictList.append(self.cdb.get_card(dbfId))

        output["cards"]=dictList
        return json.dumps(output)

    def POST(self):
        # Get json text
        the_body= cherrypy.request.body.read().decode()
        the_body= json.loads(the_body)
        # Determine new dbfId
        newID=max(self.cdb.cards.keys())
        newID=newID+1
        # Create a new list of attributes

        myList=list()
        # Determine how what type of card is being added.
        myList.append(the_body["type"])
        myList.append(the_body["name"])
        myList.append(the_body["cost"])
        myList.append(the_body["rarity"])
        myList.append(the_body["class"])
        if(the_body["type"]=="MINION"):
            myList.append(the_body["attack"])
            myList.append(the_body["health"])

        myList.append(the_body["url"])
        # Set the card given dbfId and list
        self.cdb.set_card(newID, myList)     
        output={'result':'success', "dbfId" : newID}
        return json.dumps(output)

    def DELETE(self):
        self.cdb.movies=dict()
        output={'result': 'success'}
        return json.dumps(output)
        

class CardsKeyController(object):
    def __init__(self, cdb=None):
        self.cdb = cdb

    def GET(self, dbfId):
        output=dict()
        output["card"]=self.cdb.get_card(int(dbfId))
        output["result"]="success"
        return json.dumps(output)

    def PUT(self, dbfId):
        # Get json text
        the_body= cherrypy.request.body.read().decode()
        the_body= json.loads(the_body)
        # Create a new list of attributes
        myList=list()
        # Determine how what type of card is being added.
        myList.append(the_body["type"])
        myList.append(the_body["name"])
        myList.append(the_body["cost"])
        myList.append(the_body["rarity"])
        myList.append(the_body["class"])
        if(the_body["type"]=="MINION"):
            myList.append(the_body["attack"])
            myList.append(the_body["health"])

        myList.append(the_body["url"])
        self.cdb.set_card(int(dbfId), myList)
        output={'result':'success'}
        return json.dumps(output)

    def DELETE(self, dbfId):
        output=self.cdb.delete_card(int(dbfId))
        return(json.dumps(output))

class MinionsController(object):
    def __init__(self, cdb=None):
        self.cdb= cdb
 
    def GET(self):
        output=dict()
        output["result"]= "success"
        output["minions"]=self.cdb.get_minions()
        return(json.dumps(output))

class MinionsAttackController(object):
    def __init__(self, cdb=None):
        self.cdb= cdb 

    def GET(self,RANGE):
         output=dict()
         output["result"]= "success"
         low=str(RANGE[0]) + str(RANGE[1])
         high=str(RANGE[2]) + str(RANGE[3])
         output["minions"]=self.cdb.get_minions_attackRange(int(low),int(high))
         return(json.dumps(output))        

class MinionsHealthController(object):
     def __init__(self, cdb=None):
         self.cdb= cdb
 
     def GET(self,RANGE):
         output=dict()
         output["result"]= "success"
         low=str(RANGE[0]) + str(RANGE[1])
         high=str(RANGE[2]) + str(RANGE[3])
         output["minions"]=self.cdb.get_minions_healthRange(int(low),int(high))
         return(json.dumps(output))

class SpellsController(object):
    def __init__(self, cdb=None):
        self.cdb = cdb

    def GET(self):
        output=dict()
        output["result"]= "success"
        output["spells"]=self.cdb.get_spells()
        return(json.dumps(output))

class CostController(object):
      def __init__(self, cdb=None):
          self.cdb= cdb
 
      def GET(self,RANGE):
          output=dict()
          output["result"]= "success"
          low=str(RANGE[0]) + str(RANGE[1])
          high=str(RANGE[2]) + str(RANGE[3])
          output["cards"]=self.cdb.get_cards_costRange(int(low),int(high))
          return(json.dumps(output))
class NameController(object):
    def __init__(self, cdb=None):
           self.cdb= cdb
 
    def GET(self,NAME):
        output=dict()
        output["result"]= "success"
        output["cards"]=self.cdb.get_cards_name(NAME)
        return(json.dumps(output))

class ClassController(object):
     def __init__(self, cdb=None):
            self.cdb= cdb
 
     def GET(self,CLASS):
         output=dict()
         output["result"]= "success"
         output["cards"]=self.cdb.get_cards_class(CLASS)
         return(json.dumps(output))

class RarityController(object):
     def __init__(self, cdb=None):
            self.cdb= cdb
 
     def GET(self, RARITY):
         output=dict()
         output["result"]= "success"
         output["cards"]=self.cdb.get_cards_rarity(RARITY)
         return(json.dumps(output))
