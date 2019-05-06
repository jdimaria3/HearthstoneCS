import cherrypy
from cont import *

from _card_database import _card_database


def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"


def start_service():
    
    cdb=_card_database()
    cdb.load_cards('./cards.json', './images.json')

    # Instantiate Controllers
    cardController = CardsController(cdb)
    cardKeyController= CardsKeyController(cdb)
    minionsController=MinionsController(cdb)
    minionsAttackController=MinionsAttackController(cdb)
    minionsHealthController=MinionsHealthController(cdb)
    spellsController=SpellsController(cdb)
    costController = CostController(cdb)
    nameController= NameController(cdb)
    classController= ClassController(cdb)
    rarityController= RarityController(cdb)    
    
    optionsController= OptionsController()
    dispatcher = cherrypy.dispatch.RoutesDispatcher()


##################################CONTROLLERS#####################################

    # For Cards
    dispatcher.connect('cards_get', '/cards/',
    controller=cardController,
    action = 'GET', conditions=dict(method=['GET']))

    dispatcher.connect('cards_getO', '/cards/',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))
 
    dispatcher.connect('cards_post', '/cards/',
    controller=cardController,
    action = 'POST', conditions=dict(method=['POST']))

    dispatcher.connect('cards_delete', '/cards/',
    controller=cardController,
    action = 'DELETE', conditions=dict(method=['DELETE']))

    # For Card dbfIds keys
    dispatcher.connect('cardsID_get', '/cards/:dbfId',
    controller=cardKeyController,
    action = 'GET', conditions=dict(method=['GET']))

    dispatcher.connect('cardsID_getO', '/cards/:dbfId',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))

    dispatcher.connect('cardsID_put', '/cards/:dbfId',
    controller=cardKeyController,
    action = 'PUT', conditions=dict(method=['PUT']))

    dispatcher.connect('cardsID_delete', '/cards/:dbfId',
    controller=cardKeyController,
    action = 'DELETE', conditions=dict(method=['DELETE']))

    # For Minions
    dispatcher.connect('minions_get', '/minions/',
    controller=minionsController,
    action = 'GET', conditions=dict(method=['GET']))

    dispatcher.connect('minions_getO', '/minions/',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))

    # For Minions Attack Keys
    dispatcher.connect('minionsAttack_get', '/minions/attack/:RANGE',
    controller=minionsAttackController,
    action = 'GET', conditions=dict(method=['GET']))

    dispatcher.connect('minionsAttack_getO', '/minions/attack/:RANGE',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))


    # For Minions Health Keys
  
    dispatcher.connect('minionsHealth_get', '/minions/health/:RANGE',
    controller=minionsHealthController,
    action = 'GET', conditions=dict(method=['GET']))

    dispatcher.connect('minionsHealth_getO', '/minions/health/:RANGE',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))

    # For spells 
    dispatcher.connect('spells_get', '/spells/',
    controller=spellsController,
    action = 'GET', conditions=dict(method=['GET']))

    dispatcher.connect('spells_getO', '/spells/',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))
 

    # For Cards cost range key
    dispatcher.connect('cost_get', '/cards/cost/:RANGE',
    controller=costController,
    action = 'GET', conditions=dict(method=['GET']))

    dispatcher.connect('cost_getO', '/cards/cost/:RANGE',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))


    # For Card Names 
    dispatcher.connect('name', '/cards/name/:NAME',
    controller=nameController,
    action = 'GET', conditions=dict(method=['GET']))
 
    dispatcher.connect('nameO', '/cards/name/:NAME',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))  


    # For class cards
    dispatcher.connect('class_get', '/cards/class/:CLASS',
    controller=classController,
    action = 'GET', conditions=dict(method=['GET']))

    dispatcher.connect('class_getO', '/cards/class/:CLASS',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))


    # For card rarities
    dispatcher.connect('rarity_get', '/cards/rarity/:RARITY',
    controller=rarityController,
    action = 'GET', conditions=dict(method=['GET']))

    dispatcher.connect('rarity_getO', '/cards/rarity/:RARITY',
    controller=optionsController,
    action = "OPTIONS", conditions=dict(method=['OPTIONS']))

    # Configuration for the server
    conf = {
	    'global' : {
	        'server.socket_host': '127.0.0.1',
                'server.socket_port': 8080,},
                '/' : {'request.dispatch': dispatcher,
                'tools.CORS.on': True}
	   }
    # starting the server
    cherrypy.config.update(conf) 
    app= cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)
    

if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
