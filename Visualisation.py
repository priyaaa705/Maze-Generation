# from tkinter import *
# import os

# rows, cols = (30, 30)
# goal_x, goal_y = (1, 1)

# run_search_algos = False
# run_mdp_algo = False
# SearchAlgoMaze = None

# AlgoRun = []
# SetDeterministic = True

# SetValueIteration = True
# SetPolicyIteration = True

# def set_values():
#     global rows, cols, goal_x, goal_y
#     rows, cols = ent_rows.get(), ent_cols.get()
#     goal_x, goal_y = ent_goalX.get(), ent_goalY.get()

#     global AlgoRun, SetDeterministic, SetPolicyIteration, SetValueIteration
#     AlgoRun = [CheckRunDFS.get(), CheckRunBFS.get(), CheckRunAStar.get()]
#     SetDeterministic = CheckDeterministic.get()
#     SetValueIteration = CheckValueIteration.get()
#     SetPolicyIteration = CheckPolicyIteration.get()

# def run_search_algo():
#     global run_search_algos
#     set_values()
#     run_search_algos = True
#     window.destroy()

# def run_search_mdp():
#     global run_mdp_algo
#     set_values()
#     run_mdp_algo = True
#     window.destroy()

# def check_changed():
#     global AlgoRun, SetDeterministic, SetPolicyIteration, SetValueIteration
#     AlgoRun =[CheckRunDFS.get(), CheckRunBFS.get(), CheckRunAStar.get()]
#     SetDeterministic = CheckDeterministic.get()
#     SetValueIteration = CheckValueIteration.get()
#     SetPolicyIteration = CheckPolicyIteration.get()

# # ---------------WINDOW----------------------
# window = Tk()
# window.title('ARTIFICIAL INTELLIGENCE - Assignment1')
# window.geometry("450x450+0+0")
# window.minsize(width=500, height=500)
# # window.maxsize(width=410, height=410)
# window.config(pady=5, bg='#252527')

# # -----------------MAZE------------------------
# window.columnconfigure(0, weight=1, minsize=250)
# window.rowconfigure(0, weight=1, minsize=250)

# frm_maze = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="light green", highlightthickness=2,
#                  bg='#252527')

# lbl_maze = Label(master=frm_maze, text='Maze Parameters', font='Helvetica 18 bold', foreground='light green', bg='#252527')

# lbl_rows = Label(master=frm_maze, text="Rows", bg='#252527', fg='white')
# lbl_cols = Label(master=frm_maze, text="Cols", bg='#252527', fg='white')

# ent_rows = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
# ent_rows.insert(END, string=f'{rows}')
# ent_cols = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
# ent_cols.insert(END, string=f'{cols}')

# lbl_goal = Label(master=frm_maze, text="Goal", font='Helvetica 14 bold', foreground='light green', bg='#252527')
# lbl_gridSize = Label(master=frm_maze, text="Grid Size", font='Helvetica 14 bold', foreground='light green', bg='#252527')

# lbl_goalX = Label(master=frm_maze, text="X", bg='#252527', fg='white')
# lbl_goalY = Label(master=frm_maze, text="Y", bg='#252527', fg='white')

# ent_goalX = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
# ent_goalX.insert(END, string=f'{goal_x}')
# ent_goalY = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
# ent_goalY.insert(END, string=f'{goal_y}')

# # | DRAW
# lbl_maze.grid(row=0, column=0, columnspan=2, sticky='nw')

# #   | ROW COL
# lbl_gridSize.grid(row=1, column=0, columnspan=2, sticky=W, pady=10)
# lbl_rows.grid(row=2, column=0, sticky=W, pady=2)
# ent_rows.grid(row=2, column=1, pady=2)

# lbl_cols.grid(row=3, column=0, sticky=W, pady=2)
# ent_cols.grid(row=3, column=1, pady=2)

# #   | GOAL
# lbl_goal.grid(row=4, column=0, columnspan=2, sticky=W, pady=10)
# lbl_goalX.grid(row=5, column=0, sticky=W, pady=2)
# ent_goalX.grid(row=5, column=1, pady=2, sticky=E)
# lbl_goalY.grid(row=6, column=0, sticky=W, pady=2)
# ent_goalY.grid(row=6, column=1, pady=2, sticky=E)

# # listbox_Algos.grid(row=7, column=0, columnspan=2)
# frm_maze.grid(column=0, row=0, sticky='nsew', padx=5)

# # ------------SEARCH-ALGORITHM-----------------
# window.columnconfigure(1, weight=1, minsize=170)
# window.rowconfigure(0, weight=1, minsize=200)

# frm_algo = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="#ecfc03", highlightthickness=2,
#                  bg='#252527')

# lbl_algo = Label(master=frm_algo, text='Search Algorithm', font='Helvetica 18 bold', foreground='yellow', bg='#252527')
# lbl_algos = Label(master=frm_algo, text='Run Algos', font='Helvetica 14 bold', foreground='yellow', bg='#252527')

# AlgoRunning = StringVar(value="Running Algos:\nDFS, BFS")
# lbl_algosRunning = Label(master=frm_algo, textvariable=AlgoRunning, font='Helvetica 14', foreground='#ecfc03',
#                          height=6, bg='#252527')

# CheckRunMode = IntVar(value=1)
# chk_runMode = Checkbutton(master=frm_algo, text='Run Together', variable=CheckRunMode, onvalue=1, offvalue=0,
#                           command=check_changed, bg='#252527', fg='white')

# CheckRunDFS = IntVar(value=1)
# chk_runDFS = Checkbutton(master=frm_algo, text='DFS', variable=CheckRunDFS, onvalue=1, offvalue=0,
#                           command=check_changed, bg='#252527', fg='white')

# CheckRunBFS = IntVar(value=1)
# chk_runBFS = Checkbutton(master=frm_algo, text='BFS', variable=CheckRunBFS, onvalue=1, offvalue=0,
#                           command=check_changed, bg='#252527', fg='white')

# CheckRunAStar = IntVar(value=1)
# chk_runAStar = Checkbutton(master=frm_algo, text='AStar', variable=CheckRunAStar, onvalue=1, offvalue=0,
#                           command=check_changed, bg='#252527', fg='white')

# btn_runAlgos = Button(master=frm_algo, text='RUN SEARCH ALGOS', fg='black', command=run_search_algo, bg='#252527',
#                       highlightbackground='#252527')

# # | DRAW
# lbl_algo.grid(column=0, row=0, sticky='nw')
# lbl_algos.grid(column=0, row=1, sticky='nw', pady=10)
# chk_runDFS.grid(column=0, row=2, sticky='nw')
# chk_runBFS.grid(column=0, row=3, sticky='nw')
# chk_runAStar.grid(column=0, row=4, sticky='nw')
# btn_runAlgos.grid(column=0, row=9, sticky='nsew')

# frm_algo.grid(column=1, row=0, sticky='nsew', padx=5)

# # -------------------MDP-----------------------
# window.columnconfigure(0, weight=1, minsize=170)
# window.rowconfigure(1, weight=1, minsize=10)

# frm_mdp = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="red", highlightthickness=2,
#                 bg='#252527')

# lbl_mdp = Label(master=frm_mdp, text='Markov Decision', font='Helvetica 18 bold', foreground='red',
#                 bg='#252527')

# CheckValueIteration = IntVar(value=1)
# chk_valueIteration = Checkbutton(master=frm_mdp, text='Value', variable=CheckValueIteration, onvalue=1,
#                                  offvalue=0, command=check_changed, bg='#252527', fg='white')

# CheckPolicyIteration = IntVar(value=1)
# chk_policyIteration = Checkbutton(master=frm_mdp, text='Policy', variable=CheckPolicyIteration, onvalue=1,
#                                   offvalue=0, command=check_changed, bg='#252527', fg='white')

# CheckDeterministic = IntVar(value=1)
# chk_deterministic = Checkbutton(master=frm_mdp, text='Deterministic', variable=CheckDeterministic, onvalue=1,
#                                 offvalue=0, command=check_changed, bg='#252527', fg='white')

# btn_runMDP = Button(master=frm_mdp, text='RUN MDP', fg='black', command=run_search_mdp, width=19,
#                     bg='#252527', highlightbackground='#252527')

# lbl_mdp.grid(column=0, row=0, sticky='nw')

# window.rowconfigure(1, weight=1)

# chk_valueIteration.grid(column=0, row=1, sticky='nw')
# chk_policyIteration.grid(column=1, row=1, sticky='nw')
# chk_deterministic.grid(column=0, row=2, sticky='nw')

# btn_runMDP.grid(column=0, row=3, sticky='nsew', columnspan=1)

# frm_mdp.grid(column=0, row=1, sticky='nsew', columnspan=2, padx=5, pady=4)


# # # Create a stack to keep track of frames
# # frame_stack = []

# # def go_back_to_home():
# #     global frame_stack
# #     # Check if there are frames in the stack
# #     if frame_stack:
# #         # Destroy the current frame
# #         current_frame = frame_stack.pop()
# #         current_frame.destroy()
# #         # Show the previous frame
# #         if frame_stack:
# #             previous_frame = frame_stack[-1]
# #             previous_frame.grid(row=0, column=0, sticky="nsew")

# # # When creating frames, append them to the stack
# # frame_stack.append(frm_maze)
# # frame_stack.append(frm_algo)
# # frame_stack.append(frm_mdp)

# # # Create a back button
# # btn_back = Button(master=window, text='Back', command=go_back_to_home, bg='#252527', fg='black')
# # btn_back.grid(column=0, row=2, sticky='nsew')


# # -------------------RUN-----------------------
# window.mainloop()



from tkinter import *

rows, cols = (30, 30)
goal_x, goal_y = (1, 1)

run_search_algos = False
run_mdp_algo = False
SearchAlgoMaze = None

AlgoRun = []
SetDeterministic = True

SetValueIteration = True
SetPolicyIteration = True

def set_values():
    global rows, cols, goal_x, goal_y
    rows, cols = ent_rows.get(), ent_cols.get()
    goal_x, goal_y = ent_goalX.get(), ent_goalY.get()

    global AlgoRun, SetDeterministic, SetPolicyIteration, SetValueIteration
    AlgoRun = [CheckRunDFS.get(), CheckRunBFS.get(), CheckRunAStar.get()]
    SetDeterministic = CheckDeterministic.get()
    SetValueIteration = CheckValueIteration.get()
    SetPolicyIteration = CheckPolicyIteration.get()

def run_search_algo():
    global run_search_algos
    set_values()
    run_search_algos = True
    window.destroy()

def run_search_mdp():
    global run_mdp_algo
    set_values()
    run_mdp_algo = True
    window.destroy()

def check_changed():
    global AlgoRun, SetDeterministic, SetPolicyIteration, SetValueIteration
    AlgoRun =[CheckRunDFS.get(), CheckRunBFS.get(), CheckRunAStar.get()]
    SetDeterministic = CheckDeterministic.get()
    SetValueIteration = CheckValueIteration.get()
    SetPolicyIteration = CheckPolicyIteration.get()

# ---------------WINDOW----------------------
window = Tk()
window.title('ARTIFICIAL INTELLIGENCE - Assignment1')
window.geometry("450x450+0+0")
window.minsize(width=750, height=100)
window.config(pady=5, bg='#252527')

# -----------------SEARCH ALGORITHM------------------------
window.columnconfigure(0, weight=1, minsize=150)
window.rowconfigure(0, weight=1, minsize=150)

frm_algo = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="#ecfc03", highlightthickness=2,
                 bg='#252527')

lbl_algo = Label(master=frm_algo, text='Search Algorithm', font='Helvetica 18 bold', foreground='yellow', bg='#252527')
lbl_algos = Label(master=frm_algo, text='Run Algos', font='Helvetica 14 bold', foreground='yellow', bg='#252527')

AlgoRunning = StringVar(value="Running Algos:\nDFS, BFS")
lbl_algosRunning = Label(master=frm_algo, textvariable=AlgoRunning, font='Helvetica 14', foreground='#ecfc03',
                         height=6, bg='#252527')

CheckRunMode = IntVar(value=1)
chk_runMode = Checkbutton(master=frm_algo, text='Run Together', variable=CheckRunMode, onvalue=1, offvalue=0,
                          command=check_changed, bg='#252527', fg='white')

CheckRunDFS = IntVar(value=1)
chk_runDFS = Checkbutton(master=frm_algo, text='DFS', variable=CheckRunDFS, onvalue=1, offvalue=0,
                          command=check_changed, bg='#252527', fg='white')

CheckRunBFS = IntVar(value=1)
chk_runBFS = Checkbutton(master=frm_algo, text='BFS', variable=CheckRunBFS, onvalue=1, offvalue=0,
                          command=check_changed, bg='#252527', fg='white')

CheckRunAStar = IntVar(value=1)
chk_runAStar = Checkbutton(master=frm_algo, text='AStar', variable=CheckRunAStar, onvalue=1, offvalue=0,
                          command=check_changed, bg='#252527', fg='white')

btn_runAlgos = Button(master=frm_algo, text='RUN SEARCH ALGOS', fg='black', command=run_search_algo, bg='#252527',
                      highlightbackground='#252527')

# | DRAW
lbl_algo.grid(column=0, row=0, sticky='nw')
lbl_algos.grid(column=0, row=1, sticky='nw', pady=10)
chk_runDFS.grid(column=0, row=2, sticky='nw')
chk_runBFS.grid(column=0, row=3, sticky='nw')
chk_runAStar.grid(column=0, row=4, sticky='nw')
btn_runAlgos.grid(column=0, row=9, sticky='nsew')

frm_algo.grid(column=0, row=0, sticky='nsew', padx=5)

# -------------------MDP-----------------------
window.columnconfigure(1, weight=1, minsize=150)

frm_mdp = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="red", highlightthickness=2,
                bg='#252527')

lbl_mdp = Label(master=frm_mdp, text='Markov Decision', font='Helvetica 18 bold', foreground='red',
                bg='#252527')

CheckValueIteration = IntVar(value=1)
chk_valueIteration = Checkbutton(master=frm_mdp, text='Value', variable=CheckValueIteration, onvalue=1,
                                 offvalue=0, command=check_changed, bg='#252527', fg='white')

CheckPolicyIteration = IntVar(value=1)
chk_policyIteration = Checkbutton(master=frm_mdp, text='Policy', variable=CheckPolicyIteration, onvalue=1,
                                  offvalue=0, command=check_changed, bg='#252527', fg='white')

CheckDeterministic = IntVar(value=1)
chk_deterministic = Checkbutton(master=frm_mdp, text='Deterministic', variable=CheckDeterministic, onvalue=1,
                                offvalue=0, command=check_changed, bg='#252527', fg='white')

btn_runMDP = Button(master=frm_mdp, text='RUN MDP', fg='black', command=run_search_mdp, width=19,
                    bg='#252527', highlightbackground='#252527')

lbl_mdp.grid(column=0, row=0, sticky='nw')

window.rowconfigure(1, weight=1)

chk_valueIteration.grid(column=0, row=1, sticky='nw')
chk_policyIteration.grid(column=0, row=2, sticky='nw')
chk_deterministic.grid(column=0, row=3, sticky='nw')

btn_runMDP.grid(column=0, row=4, sticky='nsew', columnspan=1)

frm_mdp.grid(column=1, row=0, sticky='nsew', padx=5, pady=4)

# -----------------MAZE------------------------
window.columnconfigure(2, weight=1, minsize=150)

frm_maze = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="light green", highlightthickness=2,
                 bg='#252527')

lbl_maze = Label(master=frm_maze, text='Maze Parameters', font='Helvetica 18 bold', foreground='light green', bg='#252527')

lbl_rows = Label(master=frm_maze, text="Rows", bg='#252527', fg='white')
lbl_cols = Label(master=frm_maze, text="Cols", bg='#252527', fg='white')

ent_rows = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_rows.insert(END, string=f'{rows}')
ent_cols = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_cols.insert(END, string=f'{cols}')

lbl_goal = Label(master=frm_maze, text="Goal", font='Helvetica 14 bold', foreground='light green', bg='#252527')
lbl_gridSize = Label(master=frm_maze, text="Grid Size", font='Helvetica 14 bold', foreground='light green', bg='#252527')

lbl_goalX = Label(master=frm_maze, text="X", bg='#252527', fg='white')
lbl_goalY = Label(master=frm_maze, text="Y", bg='#252527', fg='white')

ent_goalX = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_goalX.insert(END, string=f'{goal_x}')
ent_goalY = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_goalY.insert(END, string=f'{goal_y}')

# | DRAW
lbl_maze.grid(row=0, column=0, columnspan=2, sticky='nw')

#   | ROW COL
lbl_gridSize.grid(row=1, column=0, columnspan=2, sticky=W, pady=10)
lbl_rows.grid(row=2, column=0, sticky=W, pady=2)
ent_rows.grid(row=2, column=1, pady=2)

lbl_cols.grid(row=3, column=0, sticky=W, pady=2)
ent_cols.grid(row=3, column=1, pady=2)

#   | GOAL
lbl_goal.grid(row=4, column=0, columnspan=2, sticky=W, pady=10)
lbl_goalX.grid(row=5, column=0, sticky=W, pady=2)
ent_goalX.grid(row=5, column=1, pady=2, sticky=E)
lbl_goalY.grid(row=6, column=0, sticky=W, pady=2)
ent_goalY.grid(row=6, column=1, pady=2, sticky=E)

frm_maze.grid(column=2, row=0, sticky='nsew', padx=5)

# -------------------RUN-----------------------
window.mainloop()
