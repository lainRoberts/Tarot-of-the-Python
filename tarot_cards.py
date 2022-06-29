import scrape_definitions

card_def = scrape_definitions.CardScrapper()

class MajorArcana:
    def __init__(self, name=" ", description=" "):
            self.name = name
            self.description = description                    
            self.description = card_def.card_get_meaning(name)
            

class TheFool(MajorArcana):
    def __init__(self, description = '  ', url = '', name = 'The Fool'):
        self.name = name
        self.description = description         


class TheMagician(MajorArcana):
    def __init__(self, description = '  ', url = '', name = 'The Magician'):
        self.name = name
        self.description = description


class TheHighPriestess(MajorArcana):
    def __init__(self, description = '  ', url = '', name = 'The High Priestess'):
        self.name = name
        self.description = description         



class TheEmperor(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Emperor'):
        self.name = name
        self.description = description         



class TheEmpress(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Empress'):
        self.name = name
        self.description = description         



class TheHierophant(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Hierophant'):
        self.name = name
        self.description = description         



class TheLovers(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Lovers'):
        self.name = name
        self.description = description         



class TheChariot(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Chariot'):
        self.name = name
        self.description = description         



class Balance(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Balance'):
        self.name = name
        self.description = description         



class TheHermit(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Hermit'):
        self.name = name
        self.description = description         



class TheWheelOfFortune(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Wheel of Fortune'):
        self.name = name
        self.description = description         



class Strength(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Strength'):
        self.name = name
        self.description = description         



class TheHangedMan(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Hanged Man'):
        self.name = name
        self.description = description         



class Death(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Death'):
        self.name = name
        self.description = description         
        self.description = description


class Temperance(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Temperance'):
        self.name = name
        self.description = description         



class TheDevil(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Devil'):
        self.name = name
        self.description = description         



class TheTower(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Tower'):
        self.name = name
        self.description = description         



class TheStar(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Star'):
        self.name = name
        self.description = description         



class TheMoon(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Moon'):
        self.name = name
        self.description = description         



class TheSun(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The Sun'):
        self.name = name
        self.description = description         



class Judgement(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Judgement'):
        self.name = name
        self.description = description         



class TheWorld(MajorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'The World'):
        self.name = name
        self.description = description         


class MinorArcana():
    def __init__(self, description= " ", name=" "):
            self.name = name
            self.description = description
           #card_def.card_get_meaning(self.name)                          
    

class Cup1(MinorArcana):
    def __init__(self, description = ' ', url = ' ', name = 'Ace of Cups'):
        super().__init__(description)
        self.name = name
        self.description = description



class Cup2(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Two of Cups'):
        self.name = name
        self.description = description

    
class Cup3(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Three of Cups'):
        self.name = name
        self.description = description



class Cup4(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Four of Cups'):
        self.name = name
        self.description = description

    
class Cup5(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Five of Cups'):
        self.name = name
        self.description = description



class Cup6(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Six of Cups'):
        self.name = name
        self.description = description

    
class Cup7(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Seven of Cups'):
        self.name = name
        self.description = description



class Cup8(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Eight of Cups'):
        self.name = name
        self.description = description

    
class Cup9(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Nine of Cups'):
        self.name = name
        self.description = description



class Cup10(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Ten of Cups'):
        self.name = name
        self.description = description

    
class CupPage(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Page of Cups'):
        self.name = name
        self.description = description



class CupKnight(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Knight of Cups'):
        self.name = name
        self.description = description

    
class CupQueen(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Queen of Cups'):
        self.name = name
        self.description = description



class CupKing(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'King of Cups'):
        self.name = name
        self.description = description

    


class Cup1(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Ace of Cups'):
        self.name = name
        self.description = description



class Cup2(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Two of Cups'):
        self.name = name
        self.description = description

    
class Cup3(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Three of Cups'):
        self.name = name
        self.description = description



class Cup4(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Four of Cups'):
        self.name = name
        self.description = description

    
class Cup5(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Five of Cups'):
        self.name = name
        self.description = description



class Cup6(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Six of Cups'):
        self.name = name
        self.description = description

    
class Cup7(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Seven of Cups'):
        self.name = name
        self.description = description



class Cup8(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Eight of Cups'):
        self.name = name
        self.description = description

    
class Cup9(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Nine of Cups'):
        self.name = name
        self.description = description



class Cup10(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Ten of Cups'):
        self.name = name
        self.description = description

    
class CupPage(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Page of Cups'):
        self.name = name
        self.description = description



class CupKnight(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Knight of Cups'):
        self.name = name
        self.description = description

    
class CupQueen(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Queen of Cups'):
        self.name = name
        self.description = description



class CupKing(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'King of Cups'):
        self.name = name
        self.description = description

    


class Coin1(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Ace of Coins'):
        self.name = name
        self.description = description



class Coin2(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Two of Coins'):
        self.name = name
        self.description = description

    
class Coin3(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Three of Coins'):
        self.name = name
        self.description = description



class Coin4(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Four of Coins'):
        self.name = name
        self.description = description

    
class Coin5(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Five of Coins'):
        self.name = name
        self.description = description



class Coin6(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Six of Coins'):
        self.name = name
        self.description = description

    
class Coin7(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Seven of Coins'):
        self.name = name
        self.description = description



class Coin8(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Eight of Coins'):
        self.name = name
        self.description = description

    
class Coin9(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Nine of Coins'):
        self.name = name
        self.description = description



class Coin10(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Ten of Coins'):
        self.name = name
        self.description = description

    
class CoinPage(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Page of Coins'):
        self.name = name
        self.description = description



class CoinKnight(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Knight of Coins'):
        self.name = name
        self.description = description

    
class CoinQueen(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Queen of Coins'):
        self.name = name
        self.description = description



class CoinKing(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'King of Coins'):
        self.name = name
        self.description = description

    


class Sword1(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Ace of Swords'):
        self.name = name
        self.description = description



class Sword2(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Two of Swords'):
        self.name = name
        self.description = description

    
class Sword3(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Three of Swords'):
        self.name = name
        self.description = description



class Sword4(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Four of Swords'):
        self.name = name
        self.description = description

    
class Sword5(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Five of Swords'):
        self.name = name
        self.description = description



class Sword6(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Six of Swords'):
        self.name = name
        self.description = description

    
class Sword7(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Seven of Swords'):
        self.name = name
        self.description = description



class Sword8(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Eight of Swords'):
        self.name = name
        self.description = description

    
class Sword9(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Nine of Swords'):
        self.name = name
        self.description = description



class Sword10(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Ten of Swords'):
        self.name = name
        self.description = description

    
class SwordPage(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Page of Swords'):
        self.name = name
        self.description = description



class SwordKnight(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Knight of Swords'):
        self.name = name
        self.description = description

    
class SwordQueen(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Queen of Swords'):
        self.name = name
        self.description = description



class SwordKing(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'King of Swords'):
        self.name = name
        self.description = description

    


class Wand1(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Ace of Wands'):
        self.name = name
        self.description = description



class Wand2(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Two of Wands'):
        self.name = name
        self.description = description

    
class Wand3(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Three of Wands'):
        self.name = name
        self.description = description



class Wand4(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Four of Wands'):
        self.name = name
        self.description = description

    
class Wand5(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Five of Wands'):
        self.name = name
        self.description = description



class Wand6(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Six of Wands'):
        self.name = name
        self.description = description

    
class Wand7(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Seven of Wands'):
        self.name = name
        self.description = description



class Wand8(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Eight of Wands'):
        self.name = name
        self.description = description

    
class Wand9(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Nine of Wands'):
        self.name = name
        self.description = description



class Wand10(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Ten of Wands'):
        self.name = name
        self.description = description

    
class WandPage(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Page of Wands'):
        self.name = name
        self.description = description



class WandKnight(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Knight of Wands'):
        self.name = name
        self.description = description

    
class WandQueen(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'Queen of Wands'):
        self.name = name
        self.description = description



class WandKing(MinorArcana):
    def __init__(self, description = '  ', url = ' ', name = 'King of Coins'):
        self.name = name
        self.description = description

    

