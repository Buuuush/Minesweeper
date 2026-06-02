
## Dependencies

```
pip install tk playsound3
```

## Functions

- `play_wav()`
- `kill_music()`
- `normalize()`
- `nb_cases()`
- `generate_full_grid()`
- `empty_box()`
- `check_win()`
- `find_number()`
- `update_flag()`
- `right_clic()`
- `right_clic_release()`
- `left_clic()`
- `left_clic_release()`
- `create_button()`
- `on_close()`

## Explanations

 `play_wav()` starts a thread to play a WAV file using `playsound`.

 `kill_music()` searches for Python process IDs (PIDs) and stops them all (because Idk how to stop them lol) ^^

 `normalize()` serves as an image cache.

 `nb_cases()` randomly generates the mine positions.

 `generate_full_grid()` asks for a level (easy, medium, hard) and then generates the grid.

 `empty_box()` when clicking an empty tile, checks the 8 neighboring tiles and reveals them; if another empty tile is found, it is revealed as well (flood-fill behavior).

 `check_win()` checks after each click whether all non-mine tiles have been revealed.

 `find_number()` when a number tile is revealed, computes the number of surrounding mines and returns that number to select the correct image.

 `update_flag()` simple function to update the count of flags/mines remaining.

 `right_clic()` places a flag on the clicked tile; if a flag is already present it removes it and restores the gray tile.

 `right_clic_release()` handles actions when the right mouse button is released.

 `left_clic()` reveals the clicked tile and checks if it is a mine. If it is, all mines are revealed and the player loses. It also calls `find_number()` to determine number images.

 `left_clic_release()` handles actions when the left mouse button is released.

 `create_button()` creates all buttons with extra attributes so they can be distinguished.

 `on_close()` closes the game window and returns to the dropdown menu.


## Datas levels

- `Easy` (9x9 tiles) - 10 mines
- `Medium` (16x16 tiles) - 40 mines
- `Hard` (30x16 tiles) - 99 mines.

## External files

### Images

- `img\flag\flag.png` (54x54)
- `img\mine\mine_safe.png` (54x54)
- `img\mine\mine_boom.png` (54x54)
- `img\gray\gray.png` (54x54)
- `img\gray\gray_blank` (54x54)
- `img\gray\gray_ababab` (54x54)
- `img\Numbers\one - eight.jpg` (54x54)

### SFX

- `sfx\bgm.wav`
- `sfx\lc.wav`
- `sfx\rc.wav`

### Scripts

- `src\main.py`

## Steps


1. Implement grid generation function (29/05): 12h — grid done; remaining: generate numbers 1,2,3,4,5,6,7,8, mines, blanks.

   Unrevealed tiles must use the `gray.png` texture; revealed tiles must have background color `#797D79` with the corresponding image texture.

2. Finish grid generation (01/06): 10h (+ weekend) — done. Numbers were added along with all grids.

   When a tile is revealed, its background color becomes `#ABABAB`.

3. If a blank tile is found, reveal the 8 neighboring tiles. Lose and win states were added. SFX were added to the game for a better experience.

## Commands

```powershell
python -m venv .venv && .venv\Scripts\activate && pip install tk playsound3
```