from random import choice
import matplotlib.pyplot as plt
class RandomWalk:

    def __init__(self,max_point=1000):
       self.max_point=max_point
       self.x, self.y=[0],[0]

    def fill_walk(self):
        while len(self.x)< self.max_point:
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_far=x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_far=y_direction * y_distance

            x_track=self.x[-1] + x_far
            y_track = self.y[-1] + y_far
            self.x.append(x_track)
            self.y.append(y_track)
while True:
    new_motion=input("Do you want to make another motion (Y/N)? ").upper()

    walk=RandomWalk(50000)
    walk.fill_walk()
    plt.suptitle("Brownian Motion Simulation")
    plt.scatter(walk.x,walk.y,c='red',edgecolors='none',cmap=plt.cm.colors,s=1)
    plt.scatter(walk.x[-1],walk.y[-1],c='blue',edgecolors='none')
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    if new_motion == 'N':
        break
    else: continue
