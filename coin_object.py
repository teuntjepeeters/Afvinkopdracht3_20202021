import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup

    def __str__(self):
        return "je side up is:", self.sideup

if __name__ == "__main__":
    c = Coin()
    

    
