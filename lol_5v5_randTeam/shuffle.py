# shuffle.py
import random as r
import User as u

LANE = ['탑', '정글', '미드', '원딜', '서폿']

class shuffle:
    def __init__(self, players: list) -> None:
        self.__players = players

    def output(self) -> str:
        result = ""
        r.shuffle(self.__players)
        for i in range(2):
            for j in range(5):
                out = r.choice(self.__players)
                result += str(i+1) + "팀 "+ LANE[j] + " " + out.getName() + "\n"
                self.__players.remove(out)
            if i == 0:
                result += "-----------------------\n"
        
        return result