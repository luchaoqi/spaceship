import curses
import collections


class game:
    """[game initialization module for drawing canvas / basic game logistic information]
    """
    def __init__(self, nlines, ncols, begin_y, begin_x):
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
            win = curses.newwin(
                self.nlines, self.ncols + 40, self.begin_y,
                self.begin_x)  # + 40: space for printing the score
            win.keypad(True)
            win.nodelay(True)
            win.refresh()
            # win.timeout(1000)
            return win
        except:
            print(
                'Screen initialization failed, please adjust the size of canvas or the size of terminal and try again.'
            )
            return
            # raise

    def game_init(self):
        # basic information initialization: score, position of ship, obstacles
        score = 0
        ship = [
            self.begin_y + self.nlines - 1, self.begin_x + self.ncols // 2
        ]  # last line, mid of cols
        obstacles = collections.deque()
        return score, ship, obstacles
