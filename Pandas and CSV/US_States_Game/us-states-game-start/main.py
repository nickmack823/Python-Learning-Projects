import turtle
import pandas

correct_guesses = []
data = pandas.read_csv("50_states.csv")
print(data)
states = data["state"].to_list()


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # Use this to get state coords (in csv) for placing labels
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(correct_guesses) != 50:
    guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Guess a state, or "
                                                                                       "type 'exit' to end the game.")
    if guess == 'exit':
        missed_states = []
        # Get list of user's missed states
        for state in states:
            if state not in correct_guesses:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # To normalize user input in terms of letter casing
    if len(guess) > 1:
        guess = guess[0].upper() + guess[1:].lower()
    # Correct (non-duplicate) guess
    if guess in states and guess not in correct_guesses:
        correct_guesses.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        coords = (int(state_data.x), int(state_data.y))
        t.goto(coords)
        t.write(state_data.state.item())
