from tkinter import *
from PIL import ImageTk, Image

# Create an environment and title with root
root = Tk()
root.title("Putting an icon on the title")

# Upload pictures that I want to use for slide show
my_img1 = ImageTk.PhotoImage(Image.open("image/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("image/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("image/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("image/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("image/img5.jpg"))

# Create an array to pack all pic files into this list 
img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Create a label of showing how many pic a user is curretly looking 
status = Label(root, text="Image 1 of " +
               str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

# Display a first pic on the screen for the initial page when users enter this app  
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

# Function to activate the forward button to help users jump to the next pic
def forward(image_number):
    global my_label
    global button_forward
    global button_back
  
    # Once user click the forward button, the current pic on the screen will be disappered
    my_label.grid_forget()
    
    # Looking for an image matched with a right number from the above pic list
    my_label = Label(image=img_list[image_number-1])
    
    # Make a change in the parameter of this function, image_number, by click either forward or back buttons
    # Capture a new number and enter this function with it again  
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(
        root, text="<<", command=lambda: back(image_number - 1))
  
    # The number reaches up to 5, the button would not be clickable
    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    # Positon these three buttons with grid function 
    # Imporatnt: anytime you use grid, you dont need to use pack!
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    # Change the number of status everytime user jumps to a new pic
    status = Label(root, text="Image " + str(image_number) + " of " +
                   str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()

    my_label = Label(image=img_list[image_number-1])

    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(
        root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " +
                   str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
