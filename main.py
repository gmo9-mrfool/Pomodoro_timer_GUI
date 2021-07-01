import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Label_1.config(text="Timer", fg=GREEN)
    Label_2.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        Label_1.config(text="Long_break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        Label_1.config(text="Short_break", fg=PINK)
    else:
        countdown(work_sec)
        Label_1.config(text="work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            Label_2.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
# window.grid(column=2,row=2)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)

tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_image)
timer_text = canvas.create_text(100, 128, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# Labels
Label_1 = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
Label_1.grid(column=1, row=0)
tick = u'\u2713'
Label_2 = tkinter.Label(fg=GREEN, bg=YELLOW)
Label_2.grid(column=1, row=3)

# Buttons
Button_start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
Button_start.grid(column=0, row=2)

Button_reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_time)
Button_reset.grid(column=2, row=2)

window.mainloop()
