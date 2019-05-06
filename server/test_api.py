#Joey DiMaria
#Test Hearthstone Card Database

from _card_database import _card_database
import unittest

class TestCardDatabase(unittest.TestCase):

	cdb = _card_database()
	
	def reset_data(self):
		self.cdb.load_cards('./cards.json', './images.json')
	
	cdb.load_cards('./cards.json', './images.json')
	#cdb.print_sorted_cards()
	
	def test_get_card(self):
		#self.reset_data()
		card = self.cdb.get_card(559)
		print(card)
		self.assertEqual(card[1], 'Leeroy Jenkins')
		card = self.cdb.get_card(138)
		self.assertEqual(card[3], 'EPIC')
		
	def test_get_minions(self):
		list = self.cdb.get_minions()
		card1 = list[0]
		card2 = list[4]
		self.assertEqual(card1[0], 'MINION')
		self.assertEqual(card2[1], 'Rhonin')
		
	def test_get_spells(self):
		list = self.cdb.get_spells()
		card1 = list[0]
		card2 = list[5]
		self.assertEqual(card1[1], 'Flame Lance')
		self.assertEqual(card2[0], 'SPELL')
		
	def test_get_cards_name(self):
		list = self.cdb.get_cards_name('GIANT')
		card1 = list[0]
		card2 = list[1]
		self.assertEqual('Giant' in card1[1], True)
		self.assertEqual('Giant' in card2[1], True)
		
	def test_get_cards_rarity(self):
		list = self.cdb.get_cards_rarity('EPIC')
		card1 = list[0]
		self.assertEqual(card1[3], 'EPIC')
		self.assertEqual('RARE' in list, False)
		
	def test_get_cards_class(self):
		list = self.cdb.get_cards_class('MAGE')
		card1 = list[0]
		card2 = list[20]
		self.assertEqual(card1[4], 'MAGE')
		self.assertEqual(card2[4], 'MAGE')
		
	def test_get_cards_costRange(self):
		list = self.cdb.get_cards_costRange(11, 30)
		card1 = list[2]
		self.assertEqual(card1[2] > 10, True)
		list = self.cdb.get_cards_costRange(-5, -1)
		self.assertEqual(list, [])
		
	def test_get_minions_healthRange(self):
		list = self.cdb.get_minions_healthRange(1, 4)
		card1 = list[0]
		card2 = list[10]
		self.assertEqual(card1[6] >= 1 and card1[6] <= 4, True)
		self.assertEqual(card2[6] > 4 or card2[6] < 1, False)
		
	def test_get_minions_attackRange(self):
		list = self.cdb.get_minions_attackRange(5, 8)
		card1 = list[0]
		self.assertEqual(card1[5] >= 5 and card1[5] <= 8, True)
		list2 = self.cdb.get_minions_attackRange(50, 100)
		self.assertEqual(list2, [])
		
	def test_set_card(self):
		card = ['TEST']
		self.cdb.set_card(-1234, card)
		card = self.cdb.get_card(-1234)
		self.assertEqual(card[0], 'TEST')
		
	def test_delete_card(self):
		card = ['TEST']
		self.cdb.set_card(-1234, card)
		self.cdb.delete_card(-1234)
		card = self.cdb.get_card(-1234)
		self.assertEqual(card, None)

if __name__ == "__main__":
	unittest.main()
