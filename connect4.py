from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Connect4')
# root.iconbitmap('c:/gui/codemy.ico')

# Create menu
my_menu=Menu(root)
root.config(menu=my_menu)

# X always starts, so set boolean to True
#True=Red turn, False=Yellow turn
clicked=True
count=0 # max value 42

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42 
    global button_list
    global clicked
    global count
    button_list=[]
    b1=Button(root, text="1 1", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b1), fg='white')
    b1.grid(row=0, column=0)

    b2=Button(root, text="1 2", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b2), fg='white')
    b2.grid(row=0, column=1)

    b3=Button(root, text="1 3", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b3), fg='white')
    b3.grid(row=0, column=2)

    b4=Button(root, text="1 4", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b4), fg='white')
    b4.grid(row=0, column=3)

    b5=Button(root, text="1 5", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b5), fg='white')
    b5.grid(row=0, column=4)

    b6=Button(root, text="1 6", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b6), fg='white')
    b6.grid(row=0, column=5)

    b7=Button(root, text="1 7", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b7), fg='white')
    b7.grid(row=0, column=6)

    b8=Button(root, text="2 1", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b8), fg='white')
    b8.grid(row=1, column=0)

    b9=Button(root, text="2 2", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b9), fg='white')
    b9.grid(row=1, column=1)

    b10=Button(root, text="2 3", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b10), fg='white')
    b10.grid(row=1, column=2)

    b11=Button(root, text="2 4", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b11), fg='white')
    b11.grid(row=1, column=3)

    b12=Button(root, text="2 5", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b12), fg='white')
    b12.grid(row=1, column=4)

    b13=Button(root, text="2 6", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b13), fg='white')
    b13.grid(row=1, column=5)

    b14=Button(root, text="2 7", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b14), fg='white')
    b14.grid(row=1, column=6)

    b15=Button(root, text="3 1", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b15), fg='white')
    b15.grid(row=2, column=0)

    b16=Button(root, text="3 2", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b16), fg='white')
    b16.grid(row=2, column=1)

    b17=Button(root, text="3 3", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b17), fg='white')
    b17.grid(row=2, column=2)

    b18=Button(root, text="3 4", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b18), fg='white')
    b18.grid(row=2, column=3)

    b19=Button(root, text="3 5", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b19), fg='white')
    b19.grid(row=2, column=4)

    b20=Button(root, text="3 6", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b20), fg='white')
    b20.grid(row=2, column=5)

    b21=Button(root, text="3 7", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b21), fg='white')
    b21.grid(row=2, column=6)

    b22=Button(root, text="4 1", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b22), fg='white')
    b22.grid(row=3, column=0)

    b23=Button(root, text="4 2", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b23), fg='white')
    b23.grid(row=3, column=1)

    b24=Button(root, text="4 3", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b24), fg='white')
    b24.grid(row=3, column=2)

    b25=Button(root, text="4 4", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b25), fg='white')
    b25.grid(row=3, column=3)

    b26=Button(root, text="4 5", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b26), fg='white')
    b26.grid(row=3, column=4)

    b27=Button(root, text="4 6", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b27), fg='white')
    b27.grid(row=3, column=5)

    b28=Button(root, text="4 7", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b28), fg='white')
    b28.grid(row=3, column=6)

    b29=Button(root, text="5 1", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b29), fg='white')
    b29.grid(row=4, column=0)

    b30=Button(root, text="5 2", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b30), fg='white')
    b30.grid(row=4, column=1)

    b31=Button(root, text="5 3", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b31), fg='white')
    b31.grid(row=4, column=2)

    b32=Button(root, text="5 4", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b32), fg='white')
    b32.grid(row=4, column=3)

    b33=Button(root, text="5 5", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b33), fg='white')
    b33.grid(row=4, column=4)

    b34=Button(root, text="5 6", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b34), fg='white')
    b34.grid(row=4, column=5)

    b35=Button(root, text="5 7", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b35), fg='white')
    b35.grid(row=4, column=6)

    b36=Button(root, text="6 1", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b36), fg='white')
    b36.grid(row=5, column=0)

    b37=Button(root, text="6 2", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b37), fg='white')
    b37.grid(row=5, column=1)

    b38=Button(root, text="6 3", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b38), fg='white')
    b38.grid(row=5, column=2)

    b39=Button(root, text="6 4", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b39), fg='white')
    b39.grid(row=5, column=3)

    b40=Button(root, text="6 5", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b40), fg='white')
    b40.grid(row=5, column=4)

    b41=Button(root, text="6 6", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b41), fg='white')
    b41.grid(row=5, column=5)

    b42=Button(root, text="6 7", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b42), fg='white')
    b42.grid(row=5, column=6)

    button_list.append([b1, b2, b3, b4, b5, b6, b7])
    button_list.append([b8, b9, b10, b11, b12, b13, b14])
    button_list.append([b15, b16, b17, b18, b19, b20, b21])
    button_list.append([b22, b23, b24, b25, b26, b27, b28])
    button_list.append([b29, b30, b31, b32, b33, b34, b35])
    button_list.append([b36, b37, b38, b39, b40, b41, b42])

    count=0
    clicked=True


def disable_all_buttons():
    b1['text'] = " "
    b2['text'] = " "
    b3['text'] = " "
    b4['text'] = " "
    b5['text'] = " "
    b6['text'] = " "
    b7['text'] = " "
    b8['text'] = " "
    b9['text'] = " "
    b10['text'] = " "
    b11['text'] = " "
    b12['text'] = " "
    b13['text'] = " "
    b14['text'] = " "
    b15['text'] = " "
    b16['text'] = " "
    b17['text'] = " "
    b18['text'] = " "
    b19['text'] = " "
    b20['text'] = " "
    b21['text'] = " "
    b22['text'] = " "
    b23['text'] = " "
    b24['text'] = " "
    b25['text'] = " "
    b26['text'] = " "
    b27['text'] = " "
    b28['text'] = " "
    b29['text'] = " "
    b30['text'] = " "
    b31['text'] = " "
    b32['text'] = " "
    b33['text'] = " "
    b34['text'] = " "
    b35['text'] = " "
    b36['text'] = " "
    b37['text'] = " "
    b38['text'] = " "
    b39['text'] = " "
    b40['text'] = " "
    b41['text'] = " "
    b42['text'] = " "
    
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)
    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)
    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)
    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)
    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)
    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)



# # Check if someone won
def checkIfWon():
    global winner
    winner=False
   
    

    # Check horizontal locations for win
    for c in range(4):
        for r in range(6):
            if button_list[r][c]["bg"] == button_list[r][c+1]["bg"] and button_list[r][c]["bg"] == button_list[r][c+2]["bg"] and button_list[r][c]["bg"] == button_list[r][c+3]["bg"] and (button_list[r][c]["bg"]=="red" or button_list[r][c]["bg"]=="yellow"):
                winner=True
                if(button_list[r][c]["bg"]=="red"):
                    button_list[r][c]["bg"] = "green"
                    button_list[r][c+1]["bg"] = "green"  
                    button_list[r][c+2]["bg"] = "green"
                    button_list[r][c+3]["bg"] = "green"
                    button_list[r][c]["fg"] = "green"
                    button_list[r][c+1]["fg"] = "green"  
                    button_list[r][c+2]["fg"] = "green"
                    button_list[r][c+3]["fg"] = "green"
                    messagebox.showinfo("Connect 4", "Congratulations! Red Wins!")
                else:
                    button_list[r][c]["bg"] = "green"
                    button_list[r][c+1]["bg"] = "green"  
                    button_list[r][c+2]["bg"] = "green"
                    button_list[r][c+3]["bg"] = "green"
                    button_list[r][c]["fg"] = "green"
                    button_list[r][c+1]["fg"] = "green"  
                    button_list[r][c+2]["fg"] = "green"
                    button_list[r][c+3]["fg"] = "green"
                    messagebox.showinfo("Connect 4", "Congratulations! Yellow Wins!")
                disable_all_buttons()

    # Check vertical locations for win
    for c in range(7):
        for r in range(3):
            if button_list[r][c]["bg"] == button_list[r+1][c]["bg"] and button_list[r][c]["bg"] == button_list[r+2][c]["bg"] and button_list[r][c]["bg"] == button_list[r+3][c]["bg"] and (button_list[r][c]["bg"]=="red" or button_list[r][c]["bg"]=="yellow"):
                winner=True
                if(button_list[r][c]["bg"]=="red"):
                    button_list[r][c]["bg"] = "green"
                    button_list[r+1][c]["bg"] = "green"  
                    button_list[r+2][c]["bg"] = "green"
                    button_list[r+3][c]["bg"] = "green"
                    button_list[r][c]["fg"] = "green"
                    button_list[r+1][c]["fg"] = "green"  
                    button_list[r+2][c]["fg"] = "green"
                    button_list[r+3][c]["fg"] = "green"
                    messagebox.showinfo("Connect 4", "Congratulations! Red Wins!")
                else:
                    button_list[r][c]["bg"] = "green"
                    button_list[r+1][c]["bg"] = "green"  
                    button_list[r+2][c]["bg"] = "green"
                    button_list[r+3][c]["bg"] = "green"
                    button_list[r][c]["fg"] = "green"
                    button_list[r+1][c]["fg"] = "green"  
                    button_list[r+2][c]["fg"] = "green"
                    button_list[r+3][c]["fg"] = "green"
                    messagebox.showinfo("Connect 4", "Congratulations! Yellow Wins!")
                disable_all_buttons()

    # Check positively sloped diaganols
    for c in range(3, 7):
        for r in range(3):
            if button_list[r][c]["bg"] == button_list[r+1][c-1]["bg"] and button_list[r][c]["bg"] == button_list[r+2][c-2]["bg"] and button_list[r][c]["bg"] == button_list[r+3][c-3]["bg"] and (button_list[r][c]["bg"]=="red" or button_list[r][c]["bg"]=="yellow"):
                winner=True
                if(button_list[r][c]["bg"]=="red"):
                    button_list[r][c]["bg"] = "green"
                    button_list[r+1][c-1]["bg"] = "green"  
                    button_list[r+2][c-2]["bg"] = "green"
                    button_list[r+3][c-3]["bg"] = "green"
                    button_list[r][c]["fg"] = "green"
                    button_list[r+1][c-1]["fg"] = "green"  
                    button_list[r+2][c-2]["fg"] = "green"
                    button_list[r+3][c-3]["fg"] = "green"
                    messagebox.showinfo("Connect 4", "Congratulations! Red Wins!")
                else:
                    button_list[r][c]["bg"] = "green"
                    button_list[r+1][c-1]["bg"] = "green"  
                    button_list[r+2][c-2]["bg"] = "green"
                    button_list[r+3][c-3]["bg"] = "green"
                    button_list[r][c]["fg"] = "green"
                    button_list[r+1][c-1]["fg"] = "green"  
                    button_list[r+2][c-2]["fg"] = "green"
                    button_list[r+3][c-3]["fg"] = "green"
                    messagebox.showinfo("Connect 4", "Congratulations! Yellow Wins!")
                disable_all_buttons()

    # Check negatively sloped diaganols
    for c in range(4):
        for r in range(3):
            if button_list[r][c]["bg"] == button_list[r+1][c+1]["bg"] and button_list[r][c]["bg"] == button_list[r+2][c+2]["bg"] and button_list[r][c]["bg"] == button_list[r+3][c+3]["bg"] and (button_list[r][c]["bg"]=="red" or button_list[r][c]["bg"]=="yellow"):
                winner=True
                if(button_list[r][c]["bg"]=="red"):
                    button_list[r][c]["bg"] = "green"
                    button_list[r+1][c+1]["bg"] = "green"  
                    button_list[r+2][c+2]["bg"] = "green"
                    button_list[r+3][c+3]["bg"] = "green"
                    button_list[r][c]["fg"] = "green"
                    button_list[r+1][c+1]["fg"] = "green"  
                    button_list[r+2][c+2]["fg"] = "green"
                    button_list[r+3][c+3]["fg"] = "green"
                    messagebox.showinfo("Connect 4", "Congratulations! Red Wins!")  
                else:
                    button_list[r][c]["bg"] = "green"
                    button_list[r+1][c+1]["bg"] = "green"  
                    button_list[r+2][c+2]["bg"] = "green"
                    button_list[r+3][c+3]["bg"] = "green"
                    button_list[r][c]["fg"] = "green"
                    button_list[r+1][c+1]["fg"] = "green"  
                    button_list[r+2][c+2]["fg"] = "green"
                    button_list[r+3][c+3]["fg"] = "green"
                    messagebox.showinfo("Connect 4", "Congratulations! Yellow Wins!")
                disable_all_buttons() 
    # Check If a Tie
    if count == 42 and winner == False:
        messagebox.showinfo("Connect 4", "It's A Tie \n Better Luck Next Time")
        disable_all_buttons()

#Button clicked function
def b_click(button):
    global clicked, count
    global button_list
    foundEmpty=False
    for x in range(6):
        y=5-x
        Coord=button["text"]
        CoordX=int(Coord[0:1])-1
        CoordY=int(Coord[2:3])-1
        check=button_list[y][CoordY]
        if(check["bg"]=="white"):
            foundEmpty=True
            break
    if foundEmpty and clicked:
        check["bg"] = "red"
        check["fg"] = "red"
        clicked=False
        count+=1
        checkIfWon()
    elif foundEmpty and not clicked:
        check["bg"] = "yellow"
        check["fg"] = "yellow"
        clicked=True
        count+=1
        checkIfWon()
    else:
        messagebox.showerror("Connect 4", "Hey! That was not a valid move, Please place coin on a white space")

# Create menu
my_menu=Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)


reset()

root.mainloop()
