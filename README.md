
## Dependencies

```
pip install tk
```

## Functions

- `generate_full_grid()`
- `hide_grid()`
- `rightclic()`
- `leftclic()`
- `find_mine()`
- `win_game()`

## Explanations

`generate_full_grid()` asks for a level (easy, medium, hard) and then generates a grid.

Levels: easy (9x9 tiles) 10 mines, medium (16x16 tiles) 40 mines, hard (30x16 tiles) 99 mines. The grid contains numbered tiles, empty tiles and mined tiles.

`hide_grid()` hides all tiles by showing gray tiles.

`rightclic()` places a flag on the clicked tile; if a flag is already present it removes it and restores the gray tile.

`leftclic()` reveals the tile.

`find_mine()` displays all exploded mines and indicates a loss.

`win_game()` displays all non-exploded mines and indicates victory.

## External files

### Images

- `img\flag\flag.png` (54x54)
- `img\mine\mine_safe.png` (54x54)
- `img\mine\mine_boom.png` (54x54)
- `img\gray\gray.png` (54x54)
- `img\gray\gray_blank` (54x54)
- `img\gray\gray_ababab` (54x54)
- `img\Numbers\one - eight.jpg` (54x54)

### Scripts

- `src\main.py`

## Steps

1. Implement grid generation function (29/05): 12h — grid done; remaining: generate 1,2,3,4,5,6,7,8, mines, blanks.

   Unrevealed tiles must use the `gray.png` texture; revealed tiles must have the color `#797D79` with the corresponding image texture.

2. Finish grid generation (01/06): 10h (+ weekend) — done. Numbers were added along with all grids.

   When a tile is revealed, its background color becomes `#ABABAB`.

To do: If a blank tile is found, reveal the 8 neighboring tiles and fix bugs (right-click on a number places a flag and flags cannot be removed).

## Commands

```powershell
python -m venv .venv && .venv\Scripts\activate && pip install tk playsound3
```