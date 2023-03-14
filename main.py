import turtle as t
import threading as th
import time

# make the turtle invisible
t.ht()
# make the turtle faster
t.speed(10)
t.tracer(10)

def home_menu():
    # make the background black
    t.bgcolor("black")
    # make the text white
    t.color("white")
    t.clear()
    t.penup()
    t.goto(0, 125)
    t.pendown()
    t.write("Welcome to the home menu!", align="center", font=("Arial", 30, "normal"))
    t.penup()
    # add a "play ai" button
    # make a grey box with round corners for the button
    t.goto(-50, -55)
    t.pendown()
    t.color("grey")
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        for i in range(90):
            t.forward(0.1)
            t.left(1)
        t.forward(30)
        for i in range(90):
            t.forward(0.1)
            t.left(1)
    t.end_fill()
    t.color("white")
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.write("Play AI", align="center", font=("Arial", 20, "normal"))
    # add a "play friend" button
    t.penup()
    # make a grey box with round corners for the button
    t.goto(-70, -105)
    t.pendown()
    t.color("grey")
    t.begin_fill()
    for _ in range(2):
        t.forward(140)
        for i in range(90):
            t.forward(0.1)
            t.left(1)
        t.forward(30)
        for i in range(90):
            t.forward(0.1)
            t.left(1)
    t.end_fill()
    t.color("white")
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.write("Play Friend", align="center", font=("Arial", 20, "normal"))
    # add a "quit" button
    t.penup()
    # make a grey box with round corners for the button
    t.goto(-35, -155)
    t.pendown()
    t.color("grey")
    t.begin_fill()
    for _ in range(2):
        t.forward(70)
        for i in range(90):
            t.forward(0.1)
            t.left(1)
        t.forward(30)
        for i in range(90):
            t.forward(0.1)
            t.left(1)
    t.end_fill()
    t.color("white")
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.write("Quit", align="center", font=("Arial", 20, "normal"))

    def check_mouse():
        while True:
            global canvas
            canvas = t.getcanvas()
            x = canvas.winfo_pointerx()
            y = canvas.winfo_pointery()
            x -= canvas.winfo_rootx()
            y -= canvas.winfo_rooty()

            #print(y, x)

            if y > 423 and y < 423 + 40 and x > 429 and x < 429 + 110:
                # make the mouse a hand
                canvas.config(cursor="hand2")
            elif y > 473 and y < 473 + 40 and x > 408 and x < 408 + 153:
                # make the mouse a hand
                canvas.config(cursor="hand2")
            elif y > 523 and y < 523 + 40 and x > 443 and x < 443 + 80:
                # make the mouse a hand
                canvas.config(cursor="hand2")
            else:
                # make the mouse a normal arrow
                canvas.config(cursor="arrow")

            xx = 0
            yy = 0

            # listen for mouse clicks
            t.onscreenclick(get_pos)

            if xx != 0 and yy != 0:
                xx -= canvas.winfo_rootx()
                yy -= canvas.winfo_rooty()

                on_click(xx, yy)

                xx = 0
                yy = 0

            # check if the main thread is still running
            if not th.main_thread().is_alive():
                break

            time.sleep(0.1)

    # start the mouse checking thread
    th.Thread(target=check_mouse).start()

def on_click(x, y):
    print(x, y)
    # check if the user clicked on the "play ai" button
    if y > 423 and y < 423 + 40 and x > 429 and x < 429 + 110:
        # start the game
        print("play ai")
    # check if the user clicked on the "play friend" button
    elif y > 473 and y < 473 + 40 and x > 408 and x < 408 + 153:
        # start the game
        print("play friend")
    # check if the user clicked on the "quit" button
    elif y > 523 and y < 523 + 40 and x > 443 and x < 443 + 80:
        # quit the app
        print("quit")
        t.bye()

def get_pos(x, y):
    global xx, yy
    xx = x - canvas.winfo_rootx()
    yy = y - canvas.winfo_rooty()

    print(xx, yy)

if __name__ == "__main__":
    # start the home menu as a thread called main_thread
    th.Thread(target=home_menu, name="main_thread").start()
    # start the turtle screen
    t.mainloop()