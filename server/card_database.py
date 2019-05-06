# Manuel Marroquin
# Hearthstone Card Database
# 11/23/17


class _card_database:
    def __init__(self):
        self.cards=dict()
        self.users=dict()


    def load_cards(self, card_file):
        myfile=open(card_file,"r")
        self.cards=dict()
        # TODO if spell

        # TODO if minion
        myfile.close()

    def  load_users(self,users_file):
        myfile=open(users_file, "r")
        self.users=dict()

    def get_card(self, dbfID):
        if dbfId in self.cards:
        else:
            return(None)

    def get_cards(self):
        mylist=list()
        for dbfID in self.cards:
            mylist.append(dbfId)
        return(mylist)

    def set_card(self, dbfId, mylist):
        if dbfId in self.cards:
            self.cards[dbfId]=mylist
        else:
            self.cards.update({dbfId,mylist})
     
    def delete_card(self, dbfId):
        if dbfId in self.cards:
            del self.cards[dbfId]

    def get_user(self, uid):
       if uid in self.users: 
           return(mylist)
       else:
           return(None)
    
    def set_user(self, uid, mylist):
        if uid in self.users:
            self.users[uid]=mylist
        else:
            self.users.update({uid,mylist})

    def delete_user(self, uid):
        if uid in self.users:
            del self.users[uid]

    def print_sorted_cards(self):
        for ID in sorted(self.cards):

    


