##########################################
#                                        #
#           85pt - Lab 11                # 
#                                        #
##########################################

# Make the ball bounce up and down instead of left and right

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)

# Create the oval
circle = drawpad.create_oval(10, 10, 50, 50, fill='green')
direction = 3000
# Create our animation function
def animate():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)
    if y2 > drawpad.winfo_height(): 
        direction = - 3000
    elif y1 < 0:
        direction = 3000
    #Move our oval object by the value of direction
    drawpad.move(circle,0,direction)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(1, animate)

# Kick off our animation
animate()
root.mainloop()
