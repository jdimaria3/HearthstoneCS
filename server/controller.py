import cherrypy
import re, json

from flask_restful import reqparse, abort, Api, Resource




class OptionsController(Resource):
     def __init__(self):
        print("starting Options Controller")

     def OPTIONS(self, *args, **kargs):
         return ""


class CardsController(Resource):
    def __init__(self, cdb=None):
        self.cdb = cdb

    def get(self):
        output=dict()
        dbfIdList=self.cdb.get_cards()
        dictList=list()
        output["result"]= "success"
        for dbfId in dbfIdList:
             dictList.append(self.cdb.get_card(dbfId))

        output["cards"]=dictList
        return output

    def post(self):
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
        return output

    def DELETE(self):
        self.cdb.movies=dict()
        output={'result': 'success'}
        return output
        

class CardsKeyController(Resource):
    def __init__(self, cdb=None):
        self.cdb = cdb

    def get(self, dbfId):
        output=dict()
        output["card"]=self.cdb.get_card(int(dbfId))
        output["result"]="success"
        return output

    def put(self, dbfId):
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
        return output

    def delete(self, dbfId):
        output=self.cdb.delete_card(int(dbfId))
        return output

class MinionsController(Resource):
    def __init__(self, cdb=None):
        self.cdb= cdb
 
    def get(self):
        output=dict()
        output["result"]= "success"
        output["minions"]=self.cdb.get_minions()
        return output

class MinionsAttackController(Resource):
    def __init__(self, cdb=None):
        self.cdb= cdb 

    def get(self,RANGE):
         output=dict()
         output["result"]= "success"
         low=str(RANGE[0]) + str(RANGE[1])
         high=str(RANGE[2]) + str(RANGE[3])
         output["minions"]=self.cdb.get_minions_attackRange(int(low),int(high))
         return output        

class MinionsHealthController(Resource):
     def __init__(self, cdb=None):
         self.cdb= cdb
 
     def get(self,RANGE):
         output=dict()
         output["result"]= "success"
         low=str(RANGE[0]) + str(RANGE[1])
         high=str(RANGE[2]) + str(RANGE[3])
         output["minions"]=self.cdb.get_minions_healthRange(int(low),int(high))
         return output

class SpellsController(Resource):
    def __init__(self, cdb=None):
        self.cdb = cdb

    def get(self):
        output=dict()
        output["result"]= "success"
        output["spells"]=self.cdb.get_spells()
        return output

class CostController(Resource):
      def __init__(self, cdb=None):
          self.cdb= cdb
 
      def get(self,RANGE):
          output=dict()
          output["result"]= "success"
          low=str(RANGE[0]) + str(RANGE[1])
          high=str(RANGE[2]) + str(RANGE[3])
          output["cards"]=self.cdb.get_cards_costRange(int(low),int(high))
          return output
class NameController(Resource):
    def __init__(self, cdb=None):
           self.cdb= cdb
 
    def get(self,NAME):
        output=dict()
        output["result"]= "success"
        output["cards"]=self.cdb.get_cards_name(NAME)
        return output

class ClassController(Resource):
     def __init__(self, cdb=None):
            self.cdb= cdb
 
     def get(self,CLASS):
         output=dict()
         output["result"]= "success"
         output["cards"]=self.cdb.get_cards_class(CLASS)
         return output

class RarityController(Resource):
     def __init__(self, cdb=None):
            self.cdb= cdb
 
     def get(self, RARITY):
         output=dict()
         output["result"]= "success"
         output["cards"]=self.cdb.get_cards_rarity(RARITY)
         return output
