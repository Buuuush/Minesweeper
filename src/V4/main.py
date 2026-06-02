import tkinter as tk
from tkinter import ttk
import random
from tkinter import *
from playsound3 import playsound
import threading
import os, signal, re
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
    "gray_blank":  r"img\\gray\\gray_blank.png",
    "gray_ababab":  r"img\\gray\\gray_ababab.png"
}

numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight'}

dead = False

sound = {
    "left_clic": r"sfx\\lc.wav",
    "right_clic": r"sfx\\rc.wav",
    "bgm": r"sfx\\bgm.wav"
}

# ------ Elements first window ------
main_root = tk.Tk()
main_root.title("Menu")


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
    command=lambda: (generate_full_grid(difficulty.get(), dead)),
).grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)

# -------- Functions --------

def normalize(img_path, size=40):
    img = PhotoImage(file=img_path)
    return img.zoom(size, size).subsample(img.width(), img.height())

imgs = {key: normalize(path) for key, path in icones.items()}

def e(name):
    playsound(name)

def play_wav(f):
    threading.Thread(target=e, args=(f,)).start()
play_wav(sound.get("bgm"))

def kill_music():
    pids = re.findall(r"python\.exe\s+(\d+)", os.popen('tasklist').read())
    for i in range(len(pids)):
        os.kill(int(pids[i]), signal.SIGTERM)

# Load images
img_gray = imgs["gray"]
img_mine = imgs["mine_safe"]
img_mine_boom = imgs["mine_boom"]
flag_img = imgs["flag"]
img_gray_blank = imgs["gray_blank"]
img_one = imgs["one"]
img_two = imgs["two"]
img_three = imgs["three"]
img_four = imgs["four"]
img_five = imgs["five"]
img_six= imgs["six"]
img_seven = imgs["seven"]
img_eight = imgs["eight"]
img_gray_ababab = imgs["gray_ababab"]

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

def generate_full_grid(difficulty,death):
    main_root.withdraw()
    game_root = tk.Toplevel(main_root)
    game_root.title("Game")
    game_root.resizable(False,False)
    rows, cols, mines = diff_dic[difficulty]
    case_mined=nb_cases(rows,cols,mines)
    mine_remaining = mines
    death = death
    
    visited_cases=[]

    # Label above the grid with the grid manager
    label = ttk.Label(game_root, text=f"Remaining mines: {mine_remaining}", font=("Poppins",14, "bold"))
    label.grid(row=0, column=0, columnspan=cols, sticky="n", padx=5, pady=5)

    def empty_box(btn):
        x = btn.data["col"]
        y = btn.data["row"]
        if ((x,y) not in visited_cases):
            mine_field=[(),(),(),(),(),(),(),()]
            
            rb = buttons.get((y, x + 1)) # right box                     //     mine_field[0]
            lb = buttons.get((y, x - 1)) # left box                      //     mine_field[1]
            ub = buttons.get((y + 1, x)) # up box                        //     mine_field[2]
            db = buttons.get((y - 1, x)) # down box                      //     mine_field[3]
            drub = buttons.get((y + 1, x + 1)) # diag right up box       //     mine_field[4]
            dlub = buttons.get((y + 1, x - 1)) # diag left up box        //     mine_field[5]
            drdb = buttons.get((y - 1, x + 1)) # diag right down box     //     mine_field[6]
            dldb = buttons.get((y - 1, x - 1)) # diag left down box      //     mine_field[7]
            case_list = [rb, lb, ub, db, drub, dlub, drdb, dldb]
            mine=0

            if rb and rb.data["is_mined"]:
                mine+=1
            elif rb and rb.data["is_mined"]==False:
                if rb.data["number"]==False:
                    mine_field[0] = (y, x + 1, 0)

            if lb and lb.data["is_mined"]:
                mine+=1
            elif lb and lb.data["is_mined"]==False:
                if lb.data["number"]==False:
                    mine_field[1] = (y, x - 1, 0)

            if ub and ub.data["is_mined"]:
                mine+=1
            elif ub and ub.data["is_mined"]==False:
                if ub.data["number"]==False:
                    mine_field[2] = (y + 1, x, 0)

            if db and db.data["is_mined"]:
                mine+=1
            elif db and db.data["is_mined"]==False:
                if db.data["number"]==False:
                    mine_field[3] = (y - 1, x, 0)

            if drub and drub.data["is_mined"]:
                mine+=1
            elif drub and drub.data["is_mined"]==False:
                if drub.data["number"]==False:
                    mine_field[4] = (y + 1, x + 1, 0)

            if dlub and dlub.data["is_mined"]:
                mine+=1
            elif dlub and dlub.data["is_mined"]==False:
                if dlub.data["number"]==False:
                    mine_field[5] = (y + 1, x - 1, 0)

            if drdb and drdb.data["is_mined"]:
                mine+=1
            elif drdb and drdb.data["is_mined"]==False:
                if drdb.data["number"]==False:
                    mine_field[6] = (y - 1, x + 1, 0)

            if dldb and dldb.data["is_mined"]:
                mine+=1
            elif dldb and dldb.data["is_mined"]==False:
                if dldb.data["number"]==False:
                    mine_field[7] = (y - 1, x - 1, 0)

            visited_cases.append((x,y))

            if mine==0:
                btn.config(image=img_gray_ababab, background="#ABABAB")
                for i in range(len(mine_field)):
                    if mine_field[i]:
                        empty_box(case_list[i])
            else:
                btn.config(image=imgs[numbers[mine]],background="#ABABAB")
                btn.data["number"] = True

        else:
            pass


    def find_number(btn):
        x = btn.data["col"]
        y = btn.data["row"]
        rb = buttons.get((y, x + 1)) # right box
        lb = buttons.get((y, x - 1)) # left box
        ub = buttons.get((y + 1, x)) # up box
        db = buttons.get((y - 1, x)) # down box
        drub = buttons.get((y + 1, x + 1)) # diag right up box
        dlub = buttons.get((y + 1, x - 1)) # diag left up box
        drdb = buttons.get((y - 1, x + 1)) # diag right down box
        dldb = buttons.get((y - 1, x - 1)) # diag left down box
        mine=0

        if rb and rb.data["is_mined"] :
            mine+=1
        if lb and lb.data["is_mined"]:
            mine+=1
        if ub and ub.data["is_mined"]:
            mine+=1
        if db and db.data["is_mined"]:
            mine+=1
        if drub and drub.data["is_mined"]:
            mine+=1
        if dlub and dlub.data["is_mined"]:
            mine+=1
        if drdb and drdb.data["is_mined"]:
            mine+=1
        if dldb and dldb.data["is_mined"]:
            mine+=1

        if mine > 0:
            return numbers[mine]
        else:
            return mine

    def update_flag(e):
        nonlocal mine_remaining
        mine_remaining += e
        label.config(text=f"Remaining mines: {mine_remaining}")

    def right_clic(event):
        play_wav(sound.get("right_clic"))
        nonlocal death
        if death==False:
            if mine_remaining>0:
                # if not flag or gray or mine ( => mine boom or number)
                if ((event.widget.cget("image") != (str(event.widget.data["flag"]))) and
                        (event.widget.cget("image") != (str(event.widget.data["img_mine"]))) and
                        (event.widget.cget("image") != (str(event.widget.data["img_gray"])))):
                    
                    # Block flag on these pictures
                    if ((event.widget.cget("image") == (str(event.widget.data["one"]))) or
                            (event.widget.cget("image") == (str(event.widget.data["two"]))) or
                            (event.widget.cget("image") == (str(event.widget.data["three"]))) or
                            (event.widget.cget("image") == (str(event.widget.data["four"]))) or
                            (event.widget.cget("image") == (str(event.widget.data["five"]))) or
                            (event.widget.cget("image") == (str(event.widget.data["six"]))) or
                            (event.widget.cget("image") == (str(event.widget.data["seven"]))) or
                            (event.widget.cget("image") == (str(event.widget.data["eight"]))) or
                            (event.widget.cget("image") == (str(event.widget.data["img_gray_ababab"])))):

                        pass
                    else:
                        event.widget.config(image=event.widget.data["flag"],background='#ABABAB')
                        
                else:
                    if event.widget.cget("image") == str(event.widget.data["flag"]):
                        event.widget.config(image=event.widget.data["bg"],background='#ABABAB')
                        update_flag(+1)
                    else:
                        event.widget.config(image=event.widget.data["flag"],background='#ABABAB')
                        update_flag(-1)
            else:
                event.widget.config(background='#ABABAB')
        else:
            if event.widget.cget("image") != str(event.widget.data["img_mine_boom"]):
                event.widget.config(background='#797D79')
            else:
                event.widget.config(background='#797D79')

    def right_clic_release(event):
        if (event.widget.cget("image") == (str(event.widget.data["img_gray"])) or
            event.widget.cget("image") == (str(event.widget.data["img_mine"]))):
            event.widget.config(background='#454745')
        if event.widget.config("background")[4] == "#ABABAB":
            pass
        else:
            if (event.widget.data["is_mined"] == False and event.widget.data["number"] == False and
                    (event.widget.cget("image") != (str(event.widget.data["flag"])))):
                event.widget.config(background='#454745', image=img_gray)
            else:
                if event.widget.data["is_mined"] == True:
                    event.widget.config(background='#454745')
                else:
                    event.widget.config(background='#ABABAB')

    def left_clic(event):
        play_wav(sound.get("left_clic"))
        nonlocal death
        if death==False:
            if event.widget.cget("image") == str(event.widget.data["flag"]):
                event.widget.config(background="#ABABAB")
            else:
                if event.widget.data["is_mined"]:
                    event.widget.config(image=event.widget.data["img_mine_boom"])

                    # --------------------- ALL MINES EXPLODE -------------- #
                    for i in range(diff_dic[difficulty][1]):
                        for j in range(diff_dic[difficulty][0]):
                            future_bomb = buttons.get((i,j))
                            if future_bomb.data["is_mined"]:
                                future_bomb.config(image=future_bomb.data["img_mine_boom"], background="#454745")
                    death = True

                else:
                    coord=find_number(event.widget)
                    if coord != 0:
                        bg_number = imgs[coord]
                        event.widget.config(image=bg_number, background="#ABABAB")
                        event.widget.data["number"]=True
                    else:
                        bg_number=img_gray_ababab
                        event.widget.config(image=bg_number, background="#ABABAB")
                        empty_box(event.widget)
        else:
            if event.widget.cget("image") != str(event.widget.data["img_mine_boom"]):
                if event.widget.data["number"]:
                    event.widget.config(background="#797D79")

    def left_clic_release(event):
        nonlocal death
        if death==False:
            if event.widget.cget("image") == str(event.widget.data["gray_blank"]):
                event.widget.config(image=event.widget.data["bg"],background='#ABABAB')
            elif event.widget.cget("image") == str(event.widget.data["flag"]):
                event.widget.config(background='#ABABAB')
        else:
            if event.widget.data["number"] == True:
                event.widget.config(background='#ABABAB')

    def create_button(bg,r,c,is_mined):
        btn=tk.Button(
            grid_frame,
            background='#454745',
            image=bg,
            activebackground='#797D79'
        )
        btn.data = {
            "bg": bg,
            "gray_blank": img_gray_blank,
            "img_gray": img_gray,
            "flag": flag_img,
            "is_mined": is_mined,
            "img_mine": img_mine,
            "img_gray_ababab": img_gray_ababab,
            "img_mine_boom": img_mine_boom,
            "one": img_one,
            "two": img_two,
            "three": img_three,
            "four": img_four,
            "five": img_five,
            "six": img_six,
            "seven": img_seven,
            "eight": img_eight,
            "row": r,
            "col": c,
            "number": False,
            "diff": difficulty
        }
        btn.grid(row=r, column=c)
        btn.bind("<Button-3>", right_clic)
        btn.bind("<ButtonRelease-3>", right_clic_release)
        btn.bind("<Button-1>", left_clic)
        btn.bind("<ButtonRelease-1>", left_clic_release)
        return btn

    # Put buttons in a custom frame
    grid_frame = tk.Frame(game_root)
    grid_frame.grid(row=1, column=0)

    game_root.img_gray = img_gray
    game_root.img_mine = img_mine
    list_but=[]
    buttons = {}

    for r in range(rows):
        for c in range(cols):
            if (r, c) in case_mined:
                bg = img_mine
            else:
                bg = img_gray
            btn = create_button(bg,r,c,is_mined=(r, c) in case_mined)
            buttons[(r, c)] = btn
            list_but.append(btn)

    def on_close():
        game_root.destroy()
        main_root.deiconify()

    game_root.protocol("WM_DELETE_WINDOW", on_close)


main_root.mainloop()

kill_music()
