from functools import cmp_to_key
class Player:

    def __init__(self, name, score):

        # initialization of class member variable
        self.name = name
        self.score = score



    def __repr__(self):

        # representation string, specified by description
        return "%s %s"%(self.name, str(self.score) )


        
    def comparator(a, b):

        # Description demands that we sort Player with score and name's alphabet, on descending order
        if a.score > b.score:
            return -1

        elif a.score == b.score:

            if a.name < b.name:
                return -1
            elif a.name == b.name:
                return 0
            else:
                return 1
                
        else:
            return 1



n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)