class card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

        if suit == "diamond" or suit == "heart":
            self.color = "red"
        else: 
            self.color = "black"

class Doc(object):
    def __init__(self):
        self.deck = [] 
        suit_list= ["spade", 'heart',"diamond","club"]
        for suit in suit_list:
            for x in range(1,14):
                if x == 1:
                    self.deck.append(card(suit, "A"))
                elif x == 11:
                    self.deck.append(card(suit, "J"))
                elif x == 12:
                    self.deck.append(card(suit, "Q"))
                elif x == 13:
                    self.deck.append(card(suit, "K"))
                else: 
                    self.deck.append(card(suit, x))
deck1 = Doc()
print deck1
for card in deck1.deck:
    print " This is the " + str(card.value) + " of " + card.suit
        

    