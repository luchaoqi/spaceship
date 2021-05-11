import curses
import collections
import time
import random

# setup the window

curses.initscr()
nlines,ncols,begin_y,begin_x = 10,30,0,0
win = curses.newwin(nlines,ncols + 40,begin_y,begin_x) # + 40: space for printing the score
curses.noecho()
curses.curs_set(False)
win.keypad(True)
# win.scroll(1)
# win.scrollok(1)
# win.border(0)
win.nodelay(1)
# win.timeout(100)

# spaceship and obstacle init
ship = [begin_y+nlines-1,ncols//2] # last line, mid of cols
obstacles = collections.deque()

# game
score = 0
c = 1
while True:
  win.clear() # imp

  # create random obstacles
  if len(obstacles) == nlines:
    obstacles.pop()
    score += 1
  col_idx = random.sample(range(begin_x,begin_x + ncols),k = random.randint(0,ncols//5)) # col index of obstacle
  obstacles.appendleft(col_idx)

  # draw obstacles
  for line_idx in range(len(obstacles)):
    for col_idx in obstacles[line_idx]:
      win.addstr(begin_y+line_idx,col_idx,'-')
  
  # draw ship
  key = win.getch()
  if key == 27:
    break
  ship[1] = ship[1] + (key==curses.KEY_RIGHT) - (key==curses.KEY_LEFT)
  # margin: case when ship out of display
  if ship[1] > begin_x + ncols - 1:
    ship[1] = begin_x + ncols - 1
  if ship[0] < begin_x:
    ship[0] = begin_x
  win.addstr(ship[0],ship[1], '*')
  

  # game logic

  # ship will hit the obstacle in the next frame (second last line)
  if len(obstacles) >= nlines-1 and ship[1] in obstacles[-2]:
    # change the obstacle
    win.addstr(begin_y + nlines - 2, ship[1], 'x')
    win.addstr(ship[0],begin_y + ncols + 5, 'Score: '+ str(score))
    win.refresh()
    time.sleep(1)
    break

  # event = win.getch()
  # key = event
  # if key == curses.KEY_LEFT:
    
  # if key == curses.KEY_RIGHT:


  win.addstr(ship[0],begin_y + ncols + 5, 'Score: '+ str(score))
  win.refresh()
  time.sleep(0.3)
  # c += 1
  # if c == 20:
  #   break


curses.endwin()
print('Final score: ' + str(score))