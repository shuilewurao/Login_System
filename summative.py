from tkinter import *
import tkinter.messagebox
import random
import hashlib
import os

global entry, money, turn

global c

r = Tk()
r.title('Quick Strike Dice')
f = Frame(r)
c = Canvas(r)
text_var = StringVar(r)

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def game_sequence(d1, d2) :
    if d1 == d2 and d1 + d2 > 7:
        return 15
    if d1 == d2 :
        return 10
    if d1 + d2 > 7 :
        return 5
    if d1 + d2 < 7 and d1 != d2 :
        return -5
    if d1 + d2 == 7:
        return -10

def in_game(event = None) :
    # The actual game function that will be called repeatedly
    # Die and money are calculated here
    global money, turn
    
    for widget in f.winfo_children():
        widget.destroy()
    
    if turn >= 10 :
        restart()
        
    turn += 1
    spacer = Frame(f, height = 50)
    spacer.grid(row = 0, column = 0, columnspan = 2)    
    
    random_int_1 = random.randint(1,6)
    
    dice_1_1 = PhotoImage(file = str(random_int_1)+'.png')
    render = Label (f, image = dice_1_1)
    render.grid(row = 1, column = 0)
    
    spacer = Frame(f, width = 25)
    spacer.grid(row = 1, column = 1)
    
    random_int_2 = random.randint(1,6)
    dice_2_1 = PhotoImage(file = str(random_int_2)+'.png')
    render = Label (f, image = dice_2_1)
    render.grid(row = 1, column = 2)
    
    spacer = Frame(f, height = 100)
    spacer.grid(row = 2, column = 0, columnspan = 3)
    
    money += game_sequence(random_int_1, random_int_2)
    
    text = Label(f, text = 'Money: $' + str(money), font = ('Helvetica', 18))
    text.grid(row = 3, column = 0)
    text = Label(f, text = 'Turn:' + str(turn), font = ('Helvetica', 18))
    text.grid(row = 3, column = 2)    
    
    spacer = Frame(f, height = 25)
    spacer.grid(row = 4, column = 0, columnspan = 3)
    
    if (game_sequence(random_int_1, random_int_2) > 0 ) :
        text = Label(f, text = 'Earned $' + str(abs(game_sequence(random_int_1, random_int_2))) + '!', font = ('Helvetica', 18), height = 4)
    else :
        text = Label(f, text = 'Lost $' + str(abs(game_sequence(random_int_1, random_int_2))) + '!', font = ('Helvetica', 18), height = 4)
    text.grid(row = 5, column = 0, columnspan = 3)            
    
    start = Button(f,  text = 'Roll the Dice!', font = ('Helvetica', 16), fg = 'white', bg = 'grey', command = in_game, width = 10)
    start.grid(row = 6, column = 0, columnspan = 3)
    
    r.mainloop()
    
def start_game(event = None):
  # Initial game window with starting amount and at turn 0
    global money, turn
    turn = 0
    for widget in f.winfo_children():
        widget.destroy()

    c_height = 14*30
    c_width = 14*30
    r_height = c_height + 200
    r_width = c_width + 200
    
    screen_height = r.winfo_screenheight()
    screen_width = r.winfo_screenwidth()
    
    x = (screen_width/2) - (r_width/2)
    y = (screen_height/2) - (r_height/2)
    
    r.geometry("%dx%d+%d+%d" % (r_width, r_height, x, y))
    
    spacer = Frame(f, height = 50)
    spacer.grid(row = 0, column = 0, columnspan = 2)    
    
    dice_1_1 = PhotoImage(file = '1.png')
    render = Label (f, image = dice_1_1)
    render.grid(row = 1, column = 0)
    
    spacer = Frame(f, width = 25)
    spacer.grid(row = 1, column = 1)
    
    dice_2_1 = PhotoImage(file = '1.png')
    render = Label (f, image = dice_1_1)
    render.grid(row = 1, column = 2)
    
    spacer = Frame(f, height = 100)
    spacer.grid(row = 2, column = 0, columnspan = 3)    
    
    text = Label(f, text = 'Money: $'+str(money)+'0', font = ('Helvetica', 18))
    text.grid(row = 3, column = 0)
    text = Label(f, text = 'Turn: 0', font = ('Helvetica', 18))
    text.grid(row = 3, column = 2)    
    
    spacer = Frame(f, height = 100)
    spacer.grid(row = 4, column = 0, columnspan = 3)
    
    start = Button(f,  text = 'Roll the Dice!', font = ('Helvetica', 16), fg = 'white', bg = 'grey', command = in_game, width = 10)
    start.grid(row = 5, column = 0, columnspan = 3)

    r.mainloop()
    
def money_check(event = None) :
    # Check if the money amount is correctly entered
    global entry, money
    amount = entry.get()
    
    if isfloat(amount):
        if float(amount) < 100 :
          new_game()
        else :
            money = float(amount)
            start_game()
    else :
        new_game()

def new_game(event = None):
    # Redraw the root window for a new game
    # Add text and image using grid
    global entry, entry2, c
    
    for widget in f.winfo_children():
        widget.destroy()
    
    r_width = 500
    r_height = 500

    screen_height = r.winfo_screenheight()
    screen_width = r.winfo_screenwidth()
 
    x = (screen_width/2) - (r_width/2)
    y = (screen_height/2) - (r_height/2)
    
    r.geometry('%dx%d+%d+%d' % (r_width, r_height, x, y))
    
    spacer = Frame(f, height = 50)
    spacer.grid(row = 0, column = 0, columnspan = 2)        
    
    text = Label(f, text = 'Enter an amount of starting money\n(at least $100)\n Press ENTER to Start!', font = ('Helvetica', 18), height = 4)
    text.grid(row = 0, column = 0, columnspan = 2)
    
    entry = Entry(f, width = 10)
    label = Label(f, text = '$', font = ('Helvetica', 12))
    entry.grid(column = 1, row = 2, sticky=W)
    label.grid(column = 0, row = 2, sticky=E)
    
    entry.focus_set()
    entry.bind('<Return>', money_check)
    
    money_pic = PhotoImage(file = 'money.png')
    render = Label (f, image = money_pic)
    render.grid(row = 3, column = 0, columnspan = 3)
    
    r.mainloop()
    print ('New game!')
    
# menu and game commands
def restart(event = None):
    #global players_turn
    
    for ele in f.winfo_children():
        ele.destroy()
    c.place_forget()
    
    main()
    
def quit_program(event = None):
    r.destroy()
    print ('Goodbye!')
    raise SystemExit
    
def show_dice_rule(event = None) :
    tkinter.messagebox.showinfo('Quick Strike Dice Rules', "Game Sequence:\nRoll two dice\nIf the sum of the dice is more than 7, you win $5\nIf the dice are 'doubles' (the same value), you win $10\nIf the sum of the dice is less than 7 and not doubles, you lose $5\nIf the sum of the dice is 7, you lose $10.\nrepeat 10x.")
    print ('Show Rule')

def show_help(event = None):
    tkinter.messagebox.showinfo('Help', 'Ctrl + G to show rules\n\nCtrl + R to restart\n\nCtrl + Q to quit')
    print ('Show Help')


def create_r_window(event = None) :
    ''' This function configs the game window, menu and main page is create here '''
    
    # config key bindings
    r.bind('<Control-Shift-R>', restart)
    r.bind('<Control-Shift-Q>', quit_program)
    r.bind('<Control-Shift-G>', show_dice_rule)
    r.bind('<Control-Shift-H>', show_help)
    r.protocol("WM_DELETE_WINDOW", quit_program)
    # config window size and position
    r.resizable(width = FALSE, height = FALSE)
    screen_height = r.winfo_screenheight()
    screen_width = r.winfo_screenwidth()
    
    r_width = 500
    r_height = 500
    
    x = (screen_width/2) - (r_width/2)
    y = (screen_height/2) - (r_height/2)
    
    r.geometry('%dx%d+%d+%d' % (r_width, r_height, x, y))    
    # config menu
    menu = Menu(r)
    
    gamemenu = Menu(menu, tearoff = 0)
    gamemenu.add_command(label = 'Restart      Ctrl+R', command = restart)
    gamemenu.add_separator()
    gamemenu.add_command(label = 'Quit         Ctrl+Q', command = quit_program)
    menu.add_cascade(label = 'Game', menu = gamemenu)
    
    helpmenu = Menu(menu, tearoff = 0)
    helpmenu.add_command(label = 'Rules        Ctrl+G', command = show_dice_rule)
    helpmenu.add_command(label = 'Help         Ctrl+H', command = show_help)
    menu.add_cascade(label = 'Help', menu = helpmenu)
    
    r.config(menu = menu)
    
    spacer = Frame(f, height = 20)
    spacer.pack()
    
    dice_img = PhotoImage(file = 'dice.png')
    render = Label (f, image = dice_img)
    render.pack()
    
    spacer = Frame(f, height = 15)
    spacer.pack()
    
    text = Label(f, text = 'Are you feeling lucky enough to trust the dice?\nStrike it rich quick with this dice game!', font = ('Helvetica', 16), height = 2)
    text.pack()
    
    spacer = Frame(f, height = 25)
    spacer.pack()
    
    start = Button(f,  text = 'Start New Game!', font = ('Helvetica', 18), fg = 'white', bg = 'grey', command = new_game)
    start.pack()
    
    f.pack()

    r.mainloop()
    
def main():
    create_r_window()
    r.mainloop()

class login_screen:
    def __init__(self, master):
        self.login_frame = Frame(master)
        self.master = master

        #draw login window
        login_name = Label(self.login_frame, text = "Username").grid(row = 0,  column = 0,sticky = E)
        login_pass = Label(self.login_frame, text="Password").grid(row = 1,  column = 0,sticky = E)
        login_no_account = Label(self.login_frame, text="Don't have an account?").grid(row = 2, column = 0, columnspan = 2)
        self.login_name_box = Entry(self.login_frame)
        self.login_name_box.grid(row = 0, column = 1)
        self.login_pass_box = Entry(self.login_frame, show="*")
        self.login_pass_box.grid(row = 1, column = 1)
        login_button = Button(self.login_frame, text="Sign In")
        login_button.grid(row = 0, column = 2, rowspan = 2)
        login_button.bind('<Button-1>', self.login)
        self.login_pass_box.bind('<Return>', self.login)
        login_create_button = Button(self.login_frame, text="Sign Up", command = self.to_register).grid(row = 2, column = 2)
        pass_warning = Label(self.login_frame, text= "").grid(row =4,  column = 0, columnspan = 2)
        self.login_frame.pack()

        #read user info username + password 
        f = open("data.bin","a+")
        f.seek(0)
        data = f.readlines()
        for line in data:
            line = line.rstrip()
            if(line == ""):
                continue
            pair = line.split()
            pairs[pair[0]] = pair[1]
        f.close()

    
    def login(self, event):#check entered login info agaist registered users
        match = 0;
        u_name = self.login_name_box.get().lstrip()
        u_name = u_name.rstrip()
        if(u_name in pairs):
            if(pairs[u_name] == hashlib.sha224(self.login_pass_box.get().encode('utf-8')).hexdigest()):
                match = 1;

        if(match == 1):
            self.login_frame.forget();
            del self
            print("login succeed")
            
            main()
            
        else:
            pass_warning = Label(self.login_frame, text= "Incorrect username or password", fg = "red").grid(row =4,  column = 0, columnspan = 2)
            return 1

    
    def to_register(self):# goto register window
        self.login_frame.forget();
        reg_screen = register_screen(self.master)
        del self
        r.mainloop()



class register_screen:
    def __init__(self, master):
        self.reg_frame = Frame(master)
        self.master = master

        #draw register window
        reg_name = Label(self.reg_frame, text = "Username").grid(row = 0,  column = 0,sticky = E)
        reg_pass = Label(self.reg_frame, text= "Password").grid(row =1,  column = 0,sticky = E)
        reg_re_pass = Label(self.reg_frame, text= "Re-enter Password").grid(row =2,  column = 0,sticky = E)
        self.reg_name_box = Entry(self.reg_frame)
        self.reg_name_box.grid(row = 0, column = 1)
        self.reg_pass_box = Entry(self.reg_frame, show = "*")
        self.reg_pass_box.grid(row = 1, column = 1)
        self.reg_re_pass_box = Entry(self.reg_frame, show = "*")
        self.reg_re_pass_box.grid(row = 2, column = 1)
        reg_create_button = Button(self.reg_frame, text = "To login", command = self.to_login).grid(row = 3, column = 0)
        reg_create_button = Button(self.reg_frame, text = "Sign Up", command = self.register).grid(row = 3, column = 1, columnspan = 2)
        self.name_err = StringVar()
        name_warning = Label(self.reg_frame, textvariable = self.name_err, fg ="red").grid(row =4,  column = 0, columnspan = 4)
        self.pass_err = StringVar()
        pass_warning = Label(self.reg_frame, textvariable = self.pass_err, fg ="red").grid(row =5,  column = 0, columnspan = 4)
        name_warning1 = Label(self.reg_frame, width = 3).grid(row =0,  column = 3)
        pass_warning1 = Label(self.reg_frame, width = 3).grid(row =2,  column = 3)
        self.reg_frame.pack()

    
    def to_login(self):#goto login window
        self.reg_frame.forget();
        log_screen = login_screen(self.master)
        del self
        r.mainloop()

    
    def register(self):#chech if username and password is valid for registration
        valid_pair = -1;

        #verify username unique
        u_name = self.reg_name_box.get().lstrip()
        u_name = u_name.rstrip()
        if(u_name in pairs):
            self.name_err.set("Username already exist")
            Label(self.reg_frame, width = 3, bg = "red").grid(row =0,  column = 3)
        else:
            self.name_err.set("")
            Label(self.reg_frame, width = 3, bg = "green").grid(row =0,  column = 3)
            valid_pair += 1;

        #verify passord meet requirement
        #print(self.reg_pass_box.get()+"  "+self.reg_re_pass_box.get())
        x = self.pwd_check(u_name, self.reg_pass_box.get())
        if x == 0 : #verify password match     
            if(self.reg_re_pass_box.get() != self.reg_pass_box.get() ):
                self.pass_err.set("Password don't match")
                Label(self.reg_frame, width = 3, bg = "red").grid(row =2,  column = 3)
            else:
                self.pass_err.set("")
                Label(self.reg_frame, width = 3, bg = "green").grid(row =2,  column = 3)
                valid_pair += 1;
        elif x == 1 :
            self.pass_err.set("Password must be between 7 and 15 characters")
            Label(self.reg_frame, width = 3, bg = "red").grid(row =2,  column = 3)
        elif x == 2 :
            self.pass_err.set("Password must contain one CAPITAL letter")
            Label(self.reg_frame, width = 3, bg = "red").grid(row =2,  column = 3)
        elif x == 3 :
            self.pass_err.set("Password must contain one numerical value")
            Label(self.reg_frame, width = 3, bg = "red").grid(row =2,  column = 3)
        elif x == 4 :
            self.pass_err.set("Password must not contain username")
            Label(self.reg_frame, width = 3, bg = "red").grid(row =2,  column = 3)

        if(valid_pair == 1): #all check passed
            f = open("data.bin","a+")
            f.write("\n"+u_name+" "+hashlib.sha224(self.reg_re_pass_box.get().encode('utf-8')).hexdigest())
            f.close()
            self.reg_frame.forget();
            log_screen = login_screen(self.master)
            del self
            r.mainloop()
        else:
            return 0

    def pwd_check (self, username, pwd):
        if len(pwd) < 7 or len(pwd) > 15 :
            return 1
        elif not any(x.isupper() for x in pwd) :
            return 2
        elif not any(x.isdigit() for x in pwd) :
            return 3
        elif username in pwd :
            return 4
        else :
            return 0


#hashlib.sha224('asdasdsd'.encode('utf-8')).hexdigest()
pairs = dict() #make user info a global variable

login_screen(r)

r.mainloop()
