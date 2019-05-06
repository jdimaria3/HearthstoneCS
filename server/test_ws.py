import unittest
import requests
import json

class TestWebservice(unittest.TestCase):
	
	SITE_URL = 'http://student04.cse.nd.edu:51051'
	CARDS_URL = SITE_URL + '/cards/'
	MINIONS_URL = SITE_URL + '/minions/'
	MINIONSA_URL = MINIONS_URL + 'attack/'
	MINIONSH_URL = MINIONS_URL + 'health/'
	SPELLS_URL = SITE_URL + '/spells/'
	COST_URL = CARDS_URL + 'cost/'
	NAME_URL = CARDS_URL + 'name/'
	CLASS_URL = CARDS_URL + 'class/'
	RARITY_URL = CARDS_URL + 'rarity/'
	
	#resets dictionary of cards
	def reset_data(self):
		r = requests.delete(self.CARDS_URL)
	
	#tests that a response is a json
	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False
	
	#tests that card database loads correctly		
	def test_get_cards(self):
		self.reset_data()
		r = requests.get(self.CARDS_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		
	#tests that a completely new card can be added without being given dbfID
	def test_post_cards(self):
		self.reset_data()
		
		c = {"type":"MINION", "name":"Joey", "cost":4, "rarity":"LEGENDARY",
			 "class":"HUNTER", "attack":4, "health":4, "url":"link.png"}
		j = json.dumps(c)
		r = requests.post(self.CARDS_URL, j)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		
		r = requests.get(self.CARDS_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		
	#tests that entire dictionary can be deleted
	def test_delete_cards(self):
		self.reset_data()
		
		r = requests.delete(self.CARDS_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
	
	#tests that a card can be retrieved by ID	
	def test_get_card_id(self):
		self.reset_data()
		
		id = '559'
		r = requests.get(self.CARDS_URL + id)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['card']['name'], 'Leeroy Jenkins')
		
	#tests that a card can be put in by ID
	def test_put_card_id(self):
		self.reset_data()
		
		id = '-4'
		c = {"type":"MINION", "name":"Joey", "cost":4, "rarity":"LEGENDARY",
			 "class":"HUNTER", "attack":4, "health":4, "url":"link.png"}
		j = json.dumps(c)
		r = requests.put(self.CARDS_URL + id, j)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		
	#tests that a card can be deleted by ID
	def test_delete_card_id(self):
		self.reset_data()
		
		id = '-4'
		r = requests.delete(self.CARDS_URL + id)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')		 
		
	#tests that minions can be isolated	
	def test_get_minions(self):
		self.reset_data()
		
		r = requests.get(self.MINIONS_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['minions'][0]['type'], 'MINION')
		
	#tests that minions with an attack range can be isolated
	def test_get_minions_attack(self):
		self.reset_data()
		
		range = '1025'
		r = requests.get(self.MINIONSA_URL + range)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['minions'][0]['attack'] >= 10, True)

	#tests that minions with a health range can be isolated
	def test_get_minions_health(self):
		self.reset_data()
		
		range = '1025'
		r = requests.get(self.MINIONSH_URL + range)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['minions'][0]['health'] >= 10, True)
		
	#tests that spells can be isolated
	def test_get_spells(self):
		self.reset_data()
		
		r = requests.get(self.SPELLS_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['spells'][0]['type'], 'SPELL')
		
	#tests that cards with a cost range can be isolated
	def test_get_cards_cost(self):
		self.reset_data()
		
		range = '1025'
		r = requests.get(self.COST_URL + range)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['cards'][0]['cost'] >= 10, True)

	#tests that cards containing a certain string in its name can be isolated
	def test_get_cards_name(self):
		self.reset_data()
		
		searchn = 'leeroy'
		r = requests.get(self.NAME_URL + searchn)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual('leeroy' in resp['cards'][0]['name'].lower(), True)
		
	#tests that cards in a certain class can be isolated
	def test_get_cards_class(self):
		self.reset_data()
		
		searchc = 'mage'
		r = requests.get(self.CLASS_URL + searchc)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['cards'][0]['class'], 'MAGE')

	#tests that cards with a rarity range can be isolated
	def test_get_cards_rarity(self):
		self.reset_data()
		
		searchr = 'legendary'
		r = requests.get(self.RARITY_URL + searchr)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['cards'][0]['rarity'], 'LEGENDARY')

if __name__ == "__main__":
	unittest.main()
	
