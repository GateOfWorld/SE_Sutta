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
        if self.hand[0]==(3,'a') and self.hand[1]==(8,'a') :
            return 0    ##38광땡
        elif self.hand[0]==(1,'a') and self.hand[1]==(8,'a') :
            return 2    ##18광땡
        elif self.hand[0]==(1,'a') and self.hand[1]==(3,'a') :
            return 3    ##13광땡
        elif self.hand[0]==(4,'a') and self.hand[1]==(7,'a') :
            return 1    ##47암행어사
        elif self.hand[0][0]==self.hand[1][0] : 
            res = 20-self.hand[0][0]
            if res==10: return 8
            else : return res
        elif tmp.count(4)==tmp.count(9)==1 :
            if self.hand[0][1]==self.hand[1][1]=='a':
                return 9        #멍텅구리구사   :9땡이하재경기
            else :return 20     #구사           :알리이하재경기
        elif self.hand[0]==(3,'a') and self.hand[1]==(7,'a'):
            return 10
        elif self.hand[0][0]==1 and self.hand[1][0]==2:
            return 21           #알리 21
        elif self.hand[0][0]==1 and self.hand[1][0]==4:
            return 22
        elif self.hand[0][0]==1 and self.hand[1][0]==9:
            return 23
        elif self.hand[0][0]==1 and self.hand[1][0]==10:
            return 24
        elif self.hand[0][0]==4 and self.hand[1][0]==10:
            return 25
        elif self.hand[0][0]==4 and self.hand[1][0]==6:
            return 26
        else : return 39-((self.hand[0][0]+self.hand[1][0])%10)