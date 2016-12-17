import sys
sys.path.append('..')

import Avatar as a
from core import Environnement as e
import Wall as w


env = e.Environnement(8, 7)
avatar = a.Avatar(4,0,env)
env.ajouteAgent(avatar)
wall1 = w.Wall(3,3)
wall2 = w.Wall(4,3)
wall3 = w.Wall(5,3)
env.ajouteAgent(wall1)
env.ajouteAgent(wall2)
env.ajouteAgent(wall3)


avatar.calculeScore()
for line in env.score :
    print(line)