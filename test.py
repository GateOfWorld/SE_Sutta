class SuttaDeck:
    def __init__(self)->None:
        """섯다 전용 덱을 생성합니다. 각 카드는 튜플로 제공되며, 튜플 내 인덱스 0번은 월, 1번은 특수카드 여부입니다. 즉, (1,a)는 1월 특수카드, 1광입니다."""
        self.deck=[]
        for i in range(1,11):
            self.deck.append((i,'a'))
            self.deck.append((i,'b'))
        self.suffle()

    def pop_deck(self, card_num:int=1):
        """덱에서 카드를 뽑습니다. 기본적으로 1장 뽑을때는 기본 카드 형태인 튜플로 제공되나, 복수의 카드를 뽑을 때에는 각 튜플의 리스트 형태로 나갑니다."""
        if card_num==1:
            card_res:tuple = self.deck.pop()
        else :
            card_res:list = []
            for _ in range(card_num):
                card_res.append(self.deck.pop())
        return card_res
    
    def return_deck(self, card:list|tuple)->bool:
        """시용자의 카드를 덱으로 반납합니다. 튜플이나 리스트 둘 다 지원합니다."""
        if str(type(card))=="<class 'list'>":
            self.deck.__iadd__(card)
            return True
        elif str(type(card))=="<class 'tuple'>":
            self.deck.append(card)
            return True
        else : 
            return False
        
    def suffle(self):
        import random
        random.shuffle(self.deck)
    
class SuttaPlayer:
    def __init__(self, userdata:str="") -> None:
        """플레이어 데이터를 불러오거나 새로 생성합니다. userdata에 데이터 값이 있으면 데이터베이스에서 값을 불러들여옵니다.
        시작 금액은 10만원이며, 구성요소는 플레이어의 손패, 보유금, 승수, 패수, 생존여부(게임진행가능여부)입니다."""
        if userdata!="":
            pass            ##불러오기
        else:
            self.data:str = ""
            self.hand:list = []
            self.money:int = 100000
            self.wp:int = 0
            self.lp:int = 0
            self.alive = True
            
    def get_card(self, card):
        """덱에서 가져온 카드를 손패에 추가합니다. 튜플이나 튜플의 리스트를 지원합니다."""
        if str(type(card))=="<class 'list'>":
            self.hand.__iadd__(card)
            return True
        elif str(type(card))=="<class 'tuple'>":
            self.hand.append(card)
            return True
        return False
    
    
    def win(self, gain_money:int)->None:
        """플레이어가 승리시, 판돈을 회수함과 동시에 승점을 추가합니다."""
        self.wp+=1
        self.money+=gain_money
        return
    
    def lose(self):
        """플레이어가 패배시, 패점을 추가합니다."""
        self.lp+=1
        return
    
    def lowpanjeong(self)->int:
        """갑오 이하의 승리 우선순위를 결정합니다."""
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
    
    def panjeong(self)->int:
        """플레이어에 손패에 맞는 승리 우선순위를 결정합니다. 특수족보인 땡잡이나 암행어사, 재경기는 나중에 처리합니다.
        광땡 및 암행어사 : 0~3, 장땡 : 4, 9땡 ~ 1땡 : 7~15, 땡잡이 6
        멍텅구리구사 : 5, 구사 : 16
        알리 ~ 세륙 : 17 ~ 22
        갑오 ~ 망통 : 23 ~ 32
        """
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
            else : return self.lowpanjeong()
        elif self.hand[0][0]==self.hand[1][0]:
            if self.hand[0][0]==10 : return 4
            else : return 16-self.hand[0][0]
        else : return self.lowpanjeong()
    
    def bet_player(self, bet_money:int):
        """지정된 베팅금액을 판돈에 보탭니다. 보유금 부족시, 보유 가능한 금액을 다 냅니다."""
        if self.alive :
            if self.money<bet_money:
                mtmp = self.money
                self.money=0
                return mtmp
            else :
                self.money -= bet_money
                return bet_money
        else :
            return 0
        
    def return_card(self):
        res:list = []
        for h in range(len(self.hand)):
            res.append(self.hand[h])
        self.hand = []
        return res
            
    
class Game:
    def __init__(self,player:int, userdata:list):
        self.player = []
        self.deck = SuttaDeck()
        self.pandon:int = 0
        for i in range(player):
            self.player.append(SuttaPlayer(userdata[i]))        

    def Full_Game(self):
        starter = 0
        while (self.Non_Money()) :
            res = self.Match_Game(starter=starter)
            starter=res[0]
            #경기결과 SQL 저장
            print("승자 : %d번\t상금 : %d원"%(starter, self.pandon))            
            for p in self.player:
                p:SuttaPlayer
                print("%d\t%d\t%d\t"%(p.wp, p.lp, p.money),p.hand)
                if self.player.index(p)==starter: p.win(self.pandon)
                else : p.lose()
            
            self.pandon=0
    
    def Match_Game(self, start_money:int=0, starter:int=0):
        for p in self.player:
            self.deck.return_deck(p.return_card())
        self.deck.suffle()
        self.pandon = start_money
        if self.pandon==0:
            for i in range(starter, starter+len(self.player)):
                s=i
                if s>=len(self.player): s-=len(self.player)
                self.player[s].alive=True
                self.pandon+=self.player[s].bet_player(1000)
            self.dispense_card()
            self.bet_all()
            self.dispense_card()
            self.bet_all()
            graderes = self.gradeList()
            if (graderes[0][1]==5) or (graderes[0][1]==16) :
                return self.Match_Game(start_money=self.pandon, starter=graderes[0][0])
            if graderes[0][1]==graderes[1][1] :
                for gr in graderes:
                    if gr==graderes[0] : 
                        continue
                    if gr[1]!=graderes[0][1] : 
                        p:SuttaPlayer= self.player[gr[0]]
                        p.alive=False
                return self.Match_Game(start_money=self.pandon, starter=graderes[0][0])
            return graderes[0]
        else :
            self.dispense_card(starter=starter,count=2)
            self.bet_all()
            graderes = self.gradeList()
            if (graderes[0][1]==5) or (graderes[0][1]==16) :
                return self.Match_Game(start_money=self.pandon, starter=graderes[0][0])
            if graderes[0][1]==graderes[1][1] :
                for gr in graderes:
                    if gr==graderes[0] : 
                        continue
                    if gr[1]!=graderes[0][1] : 
                        p:SuttaPlayer= self.player[gr[0]]
                        p.alive=False
                return self.Match_Game(start_money=self.pandon, starter=graderes[0][0])
            return graderes[0]
        
    def bet_all(self, starter:int=0):
        pass

    def restarter(self)->int:
        for p in self.player:
            p:SuttaPlayer
            if p.alive :
                return self.player.index(p)
            else : continue
        return 0
    
    def dispense_card(self, starter:int =0, count:int =1):
        """지정된 매수의 카드를 생존한 각 플레이어에게 지급합니다. 생존한 유저에게만 지급하며, 죽은 유저(다이 선언한 유저)에게는 지급하지 않습니다."""
        for i in range(starter, len(self.player)+starter):
            s = i
            if s>=len(self.player): s-=len(self.player)
            p:SuttaPlayer = self.player[s]
            if p.alive:
                p.get_card(self.deck.pop_deck(count))
    
    def gradeList(self):
        """각 플레이어에게서 얻은 승리 우선순위를 정렬 후 반환합니다. """
        res = []
        for i in range(len(self.player)):
            p:SuttaPlayer=self.player[i]
            if p.alive:
                res.append([i, p.panjeong()])
            else: continue
        res.sort(key=(lambda x:x[1]))
        while (res[0][1]==1 and res[1][1]>4)or(res[0][1]==6 and res[1][1]>16):
            p = self.player[res[0][0]]
            res[0][1]=p.lowpanjeong()
            res.sort(key=(lambda x:x[1]))          
        return res
    
    def Non_Money(self):
        for p in self.player:
            p:SuttaPlayer
            if p.money==0:
                return False
        return True
            
if __name__=="__main__":
    g:Game = Game(5,['','','','',''])
    g.Full_Game()