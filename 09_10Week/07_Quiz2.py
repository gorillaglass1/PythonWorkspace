import tkinter as tk
import random

# 기본 설정

WIDTH = 500
HEIGHT = 400
CIRCLE_SIZE = 40
TIME_LIMIT = 30

score = 0
time_left = TIME_LIMIT
circle_id = None

# 동그라미 생성 함수
def create_circle():
    global circle_id
    canvas.delete("target")

    if time_left > 0:

        x = random.randint(0, WIDTH - CIRCLE_SIZE)
        y = random.randint(0, HEIGHT - CIRCLE_SIZE)

        circle_id = canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, fill="blue", tags="target")

        canvas.tag_bind(circle_id, "<Button-1>", click_circle)

#동그라미 클릭 함수
def click_circle(event):
    global score
    global circle_id

    score += 1
    score_label.config(text=f"점수: {score}")
    create_circle()



#타이머 함수
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text=f"남은 시간: {time_left}초")
        root.after(1000, countdown)
    else:
        game_over()

def game_over():
    canvas.delete("all")
    canvas.create_text(WIDTH / 2, HEIGHT / 2, text="게임 종료!", font=("Arial", 30), fill="red")
    canvas.create_text(WIDTH / 2, HEIGHT / 2 + 50, text=f"최종 점수: {score}", font=("Arial", 20), fill="red")


#tkinter 화면 구성
root = tk.Tk()
root.title("동그라미 클릭 게임")

info_frame = tk.Frame(root)
info_frame.pack(pady=10)

score_label = tk.Label(info_frame, text=f"점수: {score}", font=("Arial", 16))
score_label.pack(side="left", padx=20)

time_label = tk.Label(info_frame, text=f"남은 시간: {time_left}초", font=("Arial", 16))
time_label.pack(side="left", padx=20)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

create_circle()
countdown()
root.mainloop()


