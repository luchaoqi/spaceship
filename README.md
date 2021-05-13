Python-based spaceship dodging game in terminal using curses (windows-curses), no pygame required.

> Windows version of Python doesn't come with built-in module `curses`, but you can work around by using `windows-curses`

### Linux

```bash
# unit test for windows
conda env create -f environment.yml -n spaceship # env name
conda activate spaceship
# run the program
python test.py --canvas_height 30 --canvas_width 30 --diff_level 2
```

demo

<iframe width="857" height="565" src="https://www.youtube.com/embed/x4g7NjKTjqw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Windows

```bash
# unit test for windows
conda env create -f environment_win.yml -n spaceship # env name
conda activate spaceship
# run the program
python test.py --canvas_height 30 --canvas_width 30 --diff_level 2
```

demo

![](https://i.loli.net/2021/05/14/i3oxKlQY9mcg74s.gif)

