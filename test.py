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
            pass            ##불러오기
            self.data:str = ""
            self.hand:list = []
            self.money:int = 100000
            self.wp:int = 0
            self.lp:int = 0
        else:
            self.data:str = ""
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
    
class Game:
    def __init__(self,player:int, userdata:list):
        self.player = []
        self.deck = SuttaDeck()
        self.playable = []
        for i in range(player):
            self.player.append(SuttaPlayer(userdata[i]))        

    def Do_Sutta_Game(self, start_money:int=100):
        pass

    def top_grade(self):
        rank = []
        for i in range(len(self.player)):
            self.player[i].sort()
            rank[i] = { 'p_no':i, 'grade':self.player[i].grade(), 'win':False}
        rank.sort(lambda x:x[i]["grade"])
        if rank[0]['grade']==1 and rank[1]['grade']>3:
            rank[0]['grade']==38
        elif rank[0]['grade']==10 and rank[1]['grade']>19 : 
            rank[0]['grade']==39
        rank.sort(lambda x:x[i]["grade"])
        return rank

if __name__=="__main__":
    g = Game(5,['','','','',''])