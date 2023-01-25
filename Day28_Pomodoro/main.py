import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
checkmarks_number = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global checkmarks_number
    window.after_cancel(timer)
    pom_title.config(text="Timer", foreground=GREEN, background=YELLOW , font=(FONT_NAME, 48, "normal"))
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks_number = 0
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 1 #60
    short_break_sec = SHORT_BREAK_MIN * 1 #60
    long_break_sec = LONG_BREAK_MIN * 1 #60

    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        pom_title.config(text = "Long Break", foreground = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        pom_title.config(text = "Short Break", foreground = PINK)
    else:
        count_down(work_sec)
        pom_title.config(text = "Work", foreground = GREEN)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # if int(count_sec) == 0:
    #     count_sec = "00"
    
    if int(count_sec) < 10:
        count_sec = "0" + str(count_sec)

    if int(count_min) < 10:
        count_min = "0" + str(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        print(f"Reps={reps}, and floor = {math.floor((reps)/2)}")
        checkmarks_number = math.floor((reps)/2)
        pom_counter = tkinter.Label(text="✔"*checkmarks_number, foreground=GREEN, background=YELLOW , font=(FONT_NAME, 16, "bold"))
        pom_counter.grid(column=1, row=3)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="./Day28_Pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


pom_title = tkinter.Label(text="Timer", foreground=GREEN, background=YELLOW , font=(FONT_NAME, 48, "normal"))
pom_title.grid(column=1, row=0)

pom_start = tkinter.Button(text="Start", font=("Arial", 16, "normal"), command=start_timer)
pom_start.grid(column=0, row=2)
pom_reset = tkinter.Button(text="Reset", font=("Arial", 16, "normal"), command=reset_timer)
pom_reset.grid(column=2, row=2)

# pom_counter = tkinter.Label(text="✔", foreground=GREEN, background=YELLOW , font=(FONT_NAME, 16, "bold"))
# pom_counter.grid(column=1, row=3)

window.mainloop()