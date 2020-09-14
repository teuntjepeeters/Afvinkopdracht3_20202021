class auto:

    __max_snelheid = 100
    __aantal = 0

    def __init__(self, v):
        self.__snelheid = v
        auto.__aantal += 1
        self.__snelheid = 0
        print(auto.__aantal)
        
##    def setSnelheid(self, v):
##        if v>0 and v<200:
##            self.__snelheid = v
##        else:
##            print("Onmogelijk")
##
##    def getSnelheid(self):
##        return self.__snelheid
##
