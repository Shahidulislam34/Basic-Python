import turtle

# Global variables to store input and press counts
pl = ''  # Store user input for circle
st = ''  # Store computer input for rectangle
press_count = 0  # Shared press counter for both user and computer
current_state = 'user'  # Tracks whose turn it is ('user' or 'computer')

# Function to store user input and handle key presses for circle
def storepl(choose):
    global pl, press_count
    pl += choose  # Append the character to the input
    press_count += 1  # Increment the keypress counter
    print(f"User input: {pl}, Press count: {press_count}")
    if press_count == 2:  # After 2 key presses
        draw_circle()  # Draw a circle
        reset_input()  # Reset input and counter
        switch_state()  # Switch to computer

# Function to store computer input and handle key presses for rectangle
def storest(choose):
    global st, press_count
    st += choose  # Append the character to the input
    press_count += 1  # Increment the keypress counter
    print(f"Computer input: {st}, Press count: {press_count}")
    if press_count == 2:  # After 2 key presses
        draw_rectangle()  # Draw a rectangle
        reset_input()  # Reset input and counter
        switch_state()  # Switch back to user

# Function to draw a circle
def draw_circle():
    turtle.clear()  # Clear previous drawings
    turtle.circle(100)  # Draw a circle

# Function to draw a rectangle
def draw_rectangle():
    turtle.clear()  # Clear previous drawings
    for _ in range(2):  # Draw a rectangle
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

# Reset input and counter
def reset_input():
    global pl, st, press_count
    pl, st = '', ''  # Clear inputs
    press_count = 0  # Reset counter

# Switch between user and computer states
def switch_state():
    global current_state
    if current_state == 'user':
        current_state = 'computer'
        computer()  # Call computer's turn
    else:
        current_state = 'user'
        user()  # Call user's turn

# Function to handle user key presses
def user():
    screen.listen()  # Start listening for keypresses
    for i in range(65, 91):  # ASCII for A-Z
        ch = chr(i)
        screen.onkeypress(lambda ch=ch: storepl(ch), ch)

# Function to handle computer key presses
def computer():
    screen.listen()  # Start listening for keypresses
    for i in range(65, 91):  # ASCII for A-Z
        ch = chr(i)
        screen.onkeypress(lambda ch=ch: storest(ch), ch)

# Set up the turtle screen
screen = turtle.Screen()
turtle.width(3)
turtle.screensize(canvwidth=500, canvheight=500, bg="green")
turtle.hideturtle()

# Start with the user's turn
user()

# Keep the turtle window open
turtle.done()
