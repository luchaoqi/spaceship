import curses
import collections
import time
import random
import argparse


class game:
    def __init__(self,nlines,ncols,begin_y,begin_x):
        self.nlines = nlines
        self.ncols = ncols
        self.begin_y = begin_y
        self.begin_x = begin_x

    def draw_window(self):
        # draw window
        try:
            curses.initscr()
            curses.curs_set(0)
            curses.initscr()
            curses.noecho()
            curses.curs_set(False)
            win = curses.newwin(self.nlines,self.ncols + 40,self.begin_y,self.begin_x) # + 40: space for printing the score
            win.keypad(True)
            win.nodelay(1)
            win.refresh()
            return win
        except:
            print('Screen initialization failed, please adjust the size of canvas or the size of terminal and try again.')
            return
            # raise

    def game_init(self):
        # basic information initialization: score, position of ship, obstacles
        score = 0
        ship = [self.begin_y+self.nlines-1,self.ncols//2] # last line, mid of cols
        obstacles = collections.deque()
        return score,ship,obstacles


def main(nlines=10,ncols=30,begin_y=0,begin_x=0,difficulty=1):  # sourcery no-metrics
    try:
        tmp = game(nlines,ncols,begin_y,begin_x)
        win = tmp.draw_window()
        score,ship,obstacles = tmp.game_init()
        win.addstr(ship[0],ship[1], '*')
    except:
        return
        
    # game running
    difficulty_levels = [[20,0.5],[10,0.3],[5,0.2]] # number of obstables per line, obstable speed
    obstacle_n,obstacle_speed = difficulty_levels[difficulty]

    while True:
        win.clear()

        # press ESC to end the game
        key = win.getch()
        if key == 27:
            break

        # create random obstacles
        if len(obstacles) == nlines:
            obstacles.pop()
            score += 1
        col_idx = random.sample(range(begin_x,begin_x + ncols),k = random.randint(0,ncols//obstacle_n)) # col index of obstacle
        obstacles.appendleft(col_idx)

        # draw obstacles
        for line_idx in range(len(obstacles)):
            for col_idx in obstacles[line_idx]:
                win.addstr(begin_y+line_idx,col_idx,'-')

        # move the ship
        ship[1] = ship[1] + (key==curses.KEY_RIGHT) - (key==curses.KEY_LEFT)
        # margin case when ship is out of display
        if ship[1] > begin_x + ncols - 1:
            ship[1] = begin_x + ncols - 1
        if ship[0] < begin_x:
            ship[0] = begin_x
        
        # draw ship
        win.addstr(ship[0],ship[1], '*')
        win.refresh()

        # ship hits the obstacle
        if (len(obstacles) == nlines and ship[1] in obstacles[-2]) or (len(obstacles)==nlines-1 and ship[1] in obstacles[-1]):
            # change the obstacle shape to 'x'
            win.addstr(begin_y + nlines - 2, ship[1], 'x')
            win.addstr(ship[0],begin_y + ncols + 5, 'Score: '+ str(score))
            win.refresh()
            time.sleep(1)
            break

        # show current score
        win.addstr(ship[0],begin_y + ncols + 5, 'Score: '+ str(score))
        win.refresh()
        time.sleep(obstacle_speed)

    curses.endwin()
    print('Final score: ' + str(score))

if __name__ == '__main__':
    """[Play the spaceship dodging game in terminal]
    Args:
        nlines (int, optional): [height of canvas]. Defaults to 10.
        ncols (int, optional): [width of canvas]. Defaults to 30.
        difficulty (int, optional): [difficulty level]. Choices = [0,1,2]. Defaults to 1 .
    """

    parser = argparse.ArgumentParser(description="Play the spaceship dodging game in terminal")
    parser.add_argument("--canvas_height", nargs='?', default=10, type=int, help="height of canvas")
    parser.add_argument("--canvas_width", nargs='?', default=30, type=int,help="width of canvas")
    parser.add_argument("--diff_level", nargs='?', default=1, type=int, choices=[0,1,2], help="difficulty level")

    args = parser.parse_args()
    main(nlines=args.canvas_height,ncols=args.canvas_width,difficulty=args.diff_level)


