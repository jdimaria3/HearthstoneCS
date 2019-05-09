import flask
from flask_restful import Api, Resource
from flask_cors import CORS

from _card_database import _card_database
from controller import *

cdb=_card_database()
cdb.load_cards('./cards.json', './images.json')



app = flask.Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*/*/*": {"origins": "*"}})

api.add_resource(CardsController, '/cards/', resource_class_kwargs={'cdb': cdb})
api.add_resource(CardsKeyController, '/cards/<string:dbfId>/', resource_class_kwargs={'cdb': cdb})
api.add_resource(CostController, '/cards/cost/<string:RANGE>', resource_class_kwargs={'cdb': cdb})

api.add_resource(NameController, '/cards/name/<string:NAME>', resource_class_kwargs={'cdb': cdb})
api.add_resource(ClassController, '/cards/class/<string:CLASS>/', resource_class_kwargs={'cdb': cdb})
api.add_resource(RarityController, '/cards/rarity/<string:RARITY>/', resource_class_kwargs={'cdb': cdb})


api.add_resource(MinionsController, '/minions/', resource_class_kwargs={'cdb': cdb})
api.add_resource(MinionsAttackController, '/minions/attack/<string:RANGE>/', resource_class_kwargs={'cdb': cdb})
api.add_resource(MinionsHealthController, '/minions/health/<string:RANGE>/', resource_class_kwargs={'cdb': cdb})

api.add_resource(SpellsController, '/spells/', resource_class_kwargs={'cdb': cdb})



if __name__ == '__main__':

	app.run(debug=True, host = "127.0.0.1", port = 8080)