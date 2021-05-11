import curses
import collections
import time
import random

# setup the window

curses.initscr()
nlines,ncols,begin_y,begin_x = 10,30,0,0
win = curses.newwin(nlines,ncols,begin_y,begin_x) 
curses.noecho()
curses.curs_set(False)
win.keypad(True)
# win.scroll(1)
# win.scrollok(1)
# win.border(0)
# win.nodelay(1)



# spaceship and obstacle init
ship = [nlines-1,ncols//2] # last line, mid of cols
obstacles = collections.deque()



# game logic

score = 0
c = 1
while True:
  win.clear()
  win.addch(ship[0],ship[1], '*')

  if len(obstacles) == nlines:
    obstacles.pop()
    score += 1

  ncol = random.sample(range(begin_x,begin_x + ncols),k = random.randint(0,(ncols-begin_x)//4)) # col index of obstacle
  obstacles.appendleft(ncol)
  

  # draw obstacles
  for nline in range(len(obstacles)):
    for ncol in obstacles[nline]:
      win.insstr(nline,ncol,'-')
    win.refresh()



  # event = win.getch()
  # key = event
  # if key == curses.KEY_LEFT:
    
  # if key == curses.KEY_RIGHT:

  
  # # margin
  # if x > ncols:
  #   x = ncols


  
  # ship = 
  
  # if ship in obstacles[-1]:
  #   break

  # if key in [curses.KEY_LEFT, curses.KEY_RIGHT]:






  time.sleep(0.5)
  c += 1
  if c == 20:
    break
  




curses.endwin()
print('Final score: ' + str(score))