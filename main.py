from tkinter import *
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


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    timer = None
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmark_label.config(text="")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

    elif reps == 8:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
        reps = 0
    else:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer=window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks+="\u2713"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))

label = Label(window, text="Timer", font=(FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)

button1 = Button(window, text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)

button2 = Button(window, text="Reset", font=(FONT_NAME, 10, "bold"),command=reset_timer)

checkmark_label = Label(window, font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)

canvas.grid(row=1, column=1)
label.grid(row=0, column=1)
button1.grid(row=2, column=0)
button2.grid(row=2, column=2)
checkmark_label.grid(row=3, column=1)

window.mainloop()
