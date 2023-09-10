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
timerr = "None"

from tkinter import *
import math


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timerr)
    canvas.itemconfig(timer, text="00:00")
    timer_text.config(text="Timer")
    tick_mark.config(text="")




# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_text.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        tick_mark.grid(column=reps, row=3)
        timer_text.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    else:
        timer_text.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timerr
        timerr = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        tick_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

window.after(1000)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_text = Label(text="Timer", bg=YELLOW)
timer_text.config(fg=GREEN, font=(FONT_NAME, 33, "bold"))
timer_text.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=3, row=2)

tick_mark = Label(text="✔", fg="black", font=(FONT_NAME, 25, "bold"), bg=YELLOW)
#tick_mark.grid(column=1, row=3)

window.mainloop()
