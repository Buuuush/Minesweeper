import tkinter as tk
from tkinter import ttk
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *

# ------ Variables ------
diff_dic = {
    "Easy": [9, 9, 10],
    "Medium": [16, 16, 40],
    "Hard": [16, 30, 99]
}

icones={
    "mine_safe": r"img\\mine\\mine_safe.png",
    "mine_boom": r"img\\mine\\mine_boom.png",
    "flag": r"img\\flag\\flag.png",
    "one": r"img\\numbers\\one.png",
    "two": r"img\\numbers\\two.png",
    "three": r"img\\numbers\\three.png",
    "four": r"img\\numbers\\four.png",
    "five": r"img\\numbers\\five.png",
    "six": r"img\\numbers\\six.png",
    "seven": r"img\\numbers\\seven.png",
    "eight": r"img\\numbers\\eight.png",
    "gray": r"img\\gray\\gray.png",
    "gray_blank":  r"img\\gray\\gray_blank.png"
}

# ------ Elements first window ------
main_root = tk.Tk()
main_root.title("test")

tk.Label(
    main_root,
    text="Difficulty:",
).grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)

difficulty = ttk.Combobox(
    main_root,
    values=["Easy", "Medium", "Hard"],
    state="readonly",
)
difficulty.grid(row=2, column=2, padx=5, pady=5)
difficulty.current(0)

tk.Button(
    main_root,
    text="Start the game:",
    command=lambda: generate_full_grid(difficulty.get()),
).grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)

# -------- Functions --------

def normalize(img_path, size=40):
    img = PhotoImage(file=img_path)
    return img.zoom(size, size).subsample(img.width(), img.height())

imgs = {key: normalize(path) for key, path in icones.items()}
    
def nb_cases(x, y, r_mine):
    mined = []
    all_cases = []

    for i in range(x):
        for j in range(y):
            all_cases.append((i, j))

    while r_mine > 0:
        choix = random.choice(all_cases)

        if choix not in mined:
            mined.append(choix)
            r_mine -= 1

    return mined

def find_numbers():
    pass

def generate_full_grid(difficulty):
    main_root.withdraw()
    game_root = tk.Toplevel(main_root)
    game_root.title("Game")
    rows, cols, mines = diff_dic[difficulty]
    case_mined=nb_cases(rows,cols,mines)
    mine_remaining = mines

    # Label above the grid with the grid manager
    label = ttk.Label(game_root, text=f"Remaining mines: {mine_remaining}", font=("Poppins",14, "bold"))
    label.grid(row=0, column=0, columnspan=cols, sticky="n", padx=5, pady=5)

    def update_flag(e):
        nonlocal mine_remaining
        mine_remaining += e
        label.config(text=f"Remaining mines: {mine_remaining}")

    def right_clic(event):
        if mine_remaining>0:
            if event.widget.cget("image") == str(event.widget.flag):
                event.widget.config(image=event.widget.bg,background='#797D79')
                update_flag(+1)
            elif event.widget.cget("image") == str(imgs["mine_boom"]):
                event.widget.config(background='#797D79')
            else:
                event.widget.config(image=event.widget.flag,background='#797D79')
                update_flag(-1)
        else:
            if event.widget.cget("image") == str(event.widget.flag):
                event.widget.config(image=event.widget.bg,background='#797D79')
                update_flag(+1)
            elif event.widget.cget("image") == str(imgs["mine_boom"]):
                event.widget.config(background='#797D79')
            else:
                event.widget.config(background='#797D79')

    def right_clic_release(event):
        event.widget.config(background='#454745')

    def left_clic(event):
        if event.widget.cget("image") == str(event.widget.flag):
            event.widget.config(background='#797D79')
        else:
            if event.widget.is_mined:
                event.widget.config(image=imgs["mine_boom"])

    def left_clic_release(event):
        if event.widget.cget("image") == str(event.widget.gray_blank):
            event.widget.config(image=event.widget.bg,background='#454745')
        elif event.widget.cget("image") == str(event.widget.flag):
            event.widget.config(background='#454745')

    def create_button(bg,grid_frame,flag,gray_blank,r,c,is_mined):
        btn=tk.Button(
            grid_frame,
            background='#454745',
            image=bg,
            activebackground='#797D79'
        )
        btn.grid(row=r, column=c)
        btn.bg = bg
        btn.gray_blank = gray_blank
        btn.flag = flag
        btn.is_mined = is_mined
        btn.bind("<Button-3>", right_clic)
        btn.bind("<ButtonRelease-3>", right_clic_release)
        btn.bind("<Button-1>", left_clic)
        btn.bind("<ButtonRelease-1>", left_clic_release)
        return btn

    # Put buttons in a custom frame
    grid_frame = tk.Frame(game_root)
    grid_frame.grid(row=1, column=0)

    # Load images
    img_gray = imgs["gray"]
    img_mine = imgs["mine_safe"]
    img_mine_boom = imgs["mine_boom"]
    flag_img = imgs["flag"]
    gray_blank = imgs["gray_blank"]

    game_root.img_gray = img_gray
    game_root.img_mine = img_mine
    list_but=[]
    for r in range(rows):
        for c in range(cols):
            if (r, c) in case_mined:
                bg = img_mine
            else:
                bg = img_gray
            btn = create_button(bg,grid_frame,flag_img,gray_blank,r,c,is_mined=(r, c) in case_mined)
            list_but.append(btn)

    def on_close():
        game_root.destroy()
        main_root.deiconify()

    game_root.protocol("WM_DELETE_WINDOW", on_close)


main_root.mainloop()


