import random
import time
import argparse
import curses
from start import game


def main(nlines=10,
         ncols=30,
         begin_y=0,
         begin_x=0,
         difficulty=2):  # sourcery no-metrics
    difficulty_levels = [[20, 0.5], [15, 0.3], [
        5, 0.2
    ]]  # number of obstables per line, move speed of obstacles and spaceship
    obstacle_n, speed = difficulty_levels[difficulty]

    try:
        tmp = game(nlines, ncols, begin_y, begin_x)
        win = tmp.draw_window()
        score, ship, obstacles = tmp.game_init()
        win.addstr(ship[0], ship[1], '*')
    except:
        return

    # game running
    while True:
        # press ESC to end the game
        key = win.getch()
        curses.flushinp()
        if key == 27:
            break

        # create random obstacles
        if len(obstacles) == nlines:
            obstacles.pop()
            score += 1
        col_idx = random.sample(
            range(begin_x, begin_x + ncols),
            k=random.randint(0, ncols // obstacle_n))  # col index of obstacle
        obstacles.appendleft(col_idx)

        # show obstacles
        for line_idx in range(len(obstacles)):
            for col_idx in obstacles[line_idx]:
                win.addstr(begin_y + line_idx, col_idx, '-')

        # move the ship
        ship[1] = ship[1] + (key == curses.KEY_RIGHT) - (key
                                                         == curses.KEY_LEFT)
        # margin case when ship is out of display
        if ship[1] > begin_x + ncols - 1:
            ship[1] = begin_x + ncols - 1
        if ship[1] < begin_x:
            ship[1] = begin_x
        # show ship
        win.addstr(ship[0], ship[1], '*')

        # ship hits the obstacle
        if (len(obstacles) == nlines and ship[1] in obstacles[-2]) or (
                len(obstacles) == nlines - 1 and ship[1] in obstacles[-1]):
            # change the obstacle shape to 'x'
            win.addstr(begin_y + nlines - 2, ship[1], 'x')
            win.addstr(ship[0], begin_y + ncols + 5, 'Score: ' + str(score))
            win.refresh()
            time.sleep(1)
            break

        # show current score
        win.addstr(ship[0], begin_y + ncols + 5, 'Score: ' + str(score))
        win.refresh()
        win.clear()
        time.sleep(speed)

    curses.endwin()
    print('Final score: ' + str(score))


if __name__ == '__main__':
    """[Play the spaceship dodging game in terminal]
    Args:
        nlines (int, optional): [height of canvas]. Defaults to 10.
        ncols (int, optional): [width of canvas]. Defaults to 30.
        begin_y (int, optional): [position of upper margin of canvas]. Defaults to 0.
        begin_x (int, optional): [position of left margin of canvas]. Defaults to 0.
        difficulty (int, optional): [difficulty level: control the number of obstacles/move speed]. Choices = [0,1,2]. Defaults to 2 .
    """

    parser = argparse.ArgumentParser(
        description="Play the spaceship dodging game in terminal")
    parser.add_argument("--canvas_height",
                        nargs='?',
                        default=10,
                        type=int,
                        help="height of canvas")
    parser.add_argument("--canvas_width",
                        nargs='?',
                        default=30,
                        type=int,
                        help="width of canvas")
    parser.add_argument("--begin_y",
                        nargs='?',
                        default=0,
                        type=int,
                        help="position of upper margin of canvas")
    parser.add_argument("--begin_x",
                        nargs='?',
                        default=0,
                        type=int,
                        help="position of left margin of canvas")
    parser.add_argument(
        "--diff_level",
        nargs='?',
        default=1,
        type=int,
        choices=[0, 1, 2],
        help=
        "difficulty level: control the number of obstacles/move speed. Choices = [0,1,2]. Defaults to 2"
    )
    args = parser.parse_args()

    main(nlines=args.canvas_height,
         ncols=args.canvas_width,
         difficulty=args.diff_level)
