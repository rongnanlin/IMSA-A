
# function library to by-pass instance functions

class MyLibrary:
    def toHash(self, aList):
        #print aList
        #print "YO"
        return aList[1]+aList[8]

    def overlap(self, a1, a2, b1, b2):
        result = False
        if  (a1<=b2 and b2<=a2) or (a1<=b1 and b1<=a2):
            result = True
        return result

    def calculate_overlap(self, a1, a2, b1, b2):
        if self.overlap(a1,a2,b1,b2):
            if (a1 < b1 and a2 <= b2 ):
                return a2 - b1 +1
            elif (a1 < b1 and b2 <= a2):
                return b2 - b1 +1
            elif (b1 <= a1 and a2 <= b2):
                return a2 - a1 +1
            elif (b1 <= a1 and b2 <= a2):
                return b2 - a1 +1
        else:
            return 0