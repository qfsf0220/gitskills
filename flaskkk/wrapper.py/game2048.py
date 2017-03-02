# import curses
from random import randrange ,choice
from collections  import defaultdict

actions=["Up","Left","Right","Restart","Exit"]

letter_codes=[ord(ch) for ch in 'WASDRQwasdrq']

print letter_codes

def main(stdscr):
    def init():
        return "game"
    def not_game():
        respons=defaultdict(lambda :state)
        respons=['Restart'],respons['Exit']='init','Exit'
        return respons[actions]

    def game():
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #if 成功移动了一步:
            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'
        state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()