# You have 20 bottles of pills.19 bottles have 1.0 gram pills,but one has pilles of weight 1.1 grams.Given a scale that provides an exact measurement,how would you find the heavy bottle? You can only use the scale once.

#Solve:

# Take 1 pill from the #1 bottle, 2 from the #2 bottle,..., 20 from #20bottle.
# The total number of pills are (1+20)*20/2 = 210
# Check the total weights, to see how much heavier than 210 gram
# Suppose it is x gram heavier, then the heavy bottle is #(x/0.1)

def pill_bottle(bottles):
    pills = []
    for i, bottle in enumerate(bottles,1):
        pills += [bottle.pill()] * (i)
    print(pills)
    weight = sum(pills)
    weight = round(weight,1)
    print(weight)
    index = (weight - (1+i)*(i)/2) / 0.1 
    return int(index) 


class Bottle():
    def __init__(self, pill_weight=1):
        self.pill_weight = pill_weight
  
    def pill(self):
        return self.pill_weight

if __name__ == '__main__':
    bottles = [Bottle(), Bottle(), Bottle(), Bottle(), Bottle(1.1),
    Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
    Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
    Bottle(), Bottle(), Bottle(), Bottle(), Bottle()]
    print(pill_bottle(bottles))
    

 