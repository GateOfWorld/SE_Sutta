class Deck :
    def __init__(self):
        self.deck=[]
        for i in range(1,14):
            self.deck.append((i,'spade'))
            self.deck.append((i,'heart'))
            self.deck.append((i,'diamond'))
            self.deck.append((i,'clover'))
        return
    
    def suffle(self, seed:any=None):
        """덱의 순서를 무작위로 섞습니다."""
        import random
        import time
        if seed==None: 
            random.seed(time.time())
        random.shuffle(self.deck)
        return

    def Pop(self, num=1):
        if num==1:
            card_res:tuple=self.deck.pop()
        else :
            card_res:list=[]
            for _ in range(num):
                card_res.append(self.deck.pop())
        return card_res
    
    def return_card(self, card):
        """시용자의 카드를 덱으로 반납합니다. 튜플이나 리스트 둘 다 지원합니다."""
        if str(type(card))=="<class 'list'>":
            self.deck.__iadd__(card)
            return True
        elif str(type(card))=="<class 'tuple'>":
            self.deck.append(card)
            return True
        else : 
            return False
    
class Player:
    def __init__(self):
        self.win, self.lose, self.played = 0
        return

    def win_rate(self)->float:
        return float(self.win/(self.win+self.lose))

    def lose_rate(self)->float:
        return float(self.lose/(self.win+self.lose))

    def win_game(self,value:int=1):
        self.win+=value
        return

    def lose_game(self,value:int=1):
        self.lose+=value
        return

class Game:
    def __init__(self, p:int=1):
        self.p = []
        for _ in range(p):
            self.p.append(Player())
        self.deck = Deck()
        self.runner:list
        for _ in range(4):


    def new_game(self, meter:int = 10):
        self.deck.suffle()
        back_card:list = self.deck.Pop(meter-1)

