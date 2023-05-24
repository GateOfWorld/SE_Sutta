import random

class SuttaDeck:
    def __init__(self)->None:
        self.deck=[]
        for i in range(1,11):
            self.deck.append((i,'a'))
            self.deck.append((i,'b'))
        random.shuffle(self.deck)


    def pop_deck(self, card_num:int=1):
        if card_num==1:
            card_res = self.deck.pop()
        else :
            card_res:list = []
            for i in range(card_num):
                card_res.append(self.deck.pop())
        return card_res
    
    def return_deck(self, card)->bool:
        if type(card)=="<class 'list'>":
            self.deck.__iadd__(card)
            return True
        elif type(card)=="<class 'tuple'>":
            self.deck.append(card)
            return True
        else : 
            return False
    
class SuttaPlayer:
    def __init__(self, userdata:str="") -> None:
        if userdata!="":
            pass
        else:
            self.hand:list = []
            self.money:int = 100000
            self.wp:int = 0
            self.lp:int = 0
        return
    
    def win(self, gain_money:int)->None:
        self.wp+=1
        self.money+=gain_money
        return
    
    def lose(self):
        self.lp-=1
        return
    
    def panjeong(self)->int:
        def lowpanjeong(self)->int:
            if self.hand[0][0]==1 and self.hand[1][0]==2:
                return 17           
            elif self.hand[0][0]==1 and self.hand[1][0]==4:
                return 18
            elif self.hand[0][0]==1 and self.hand[1][0]==9:
                return 19
            elif self.hand[0][0]==1 and self.hand[1][0]==10:
                return 20
            elif self.hand[0][0]==4 and self.hand[1][0]==10:
                return 21
            elif self.hand[0][0]==4 and self.hand[1][0]==6:
                return 22
            else : return 32-((self.hand[0][0]+self.hand[1][0])%10)
        #--------------------------------------
        if self.hand[0][0]==4 and self.hand[1][0]==9:
            if self.hand[0][1]==self.hand[1][1]=='a' :
                return 5
            else : 
                return 16 
        elif self.hand[0][1]==self.hand[1][1]=='a' :
            if self.hand[0][0]==3 and self.hand[1][0]==8:
                return 0#38
            elif self.hand[0][0]==1 and self.hand[1][0]==8:
                return 2#18
            elif self.hand[0][0]==1 and self.hand[1][0]==3:
                return 3#13
            elif self.hand[0][0]==4 and self.hand[1][0]==7:
                return 1#47암행, 1끗취급
            elif self.hand[0][0]==3 and self.hand[1][0]==7:
                return 6#37땡잡이, 망통취급
            else : return lowpanjeong()
        elif self.hand[0][0]==self.hand[1][0]:
            if self.hand[0][0]==10 : return 4
            else : return 16-self.hand[0][0]
        else : return lowpanjeong()
    
    def bet_player(self, bet_money:int):
        if self.money<bet_money:
            mtmp = self.money
            self.money=0
            return mtmp
        else :
            self.money -= bet_money
            return bet_money
    
        