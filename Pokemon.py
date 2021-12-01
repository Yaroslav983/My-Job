import requests





class BasePockemon:
    hyperlinkblocked = input()
    def __init__(self, hyperlinkblocked):
        result = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(hyperlinkblocked)).json()
        self.name = result["name"]
        self.ID = result["id"]
    def InfoSmall(self):
        print(self.name)
        print(self.ID)

class Pockemon(BasePockemon):

    weight: object

    def __init__(self, hyperlinkblocked):
        BasePockemon.__init__(self, hyperlinkblocked)
        result = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(hyperlinkblocked)).json()
        self.weight = result["weight"]
        self.height = result["height"]
    def Info(self):
        print(self.name)
        print(self.ID)
        print(self.weight)
        print(self.height)
class Stats(Pockemon):
    def __init__(self, hyperlinkblocked):
        Pockemon.__init__(self, hyperlinkblocked)
        result = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(hyperlinkblocked)).json()
        self.hp = result['hp']
        self.attack = result['attack']
        self.defence = result['defence']
        self.special_attack = result['special_attack']
        self.special_defence = result['special_defence']
        self.speed = result[speed]
    def GetStats(self):
        print(hp)
        print(attack)
        print(defence)
        print(special_attack)
        print(special_defence)
        print(speed)

def EverythingIsHere(hyperlink, IRealyNeedThat):
    if (IReallyNeedThat = "False"):
         me = BasePokemon(hyperlink)
         print(me.InfoSmall)
    else:
        me = Stats()
        print(me.GetStats())
        print(me.Info())
