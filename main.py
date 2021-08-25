import turtle
import pandas
score = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_list = []
missing_states = []
while len(answer_list)<50:
    answer_state = screen.textinput(f"Guess the State ({score}/50)", "Enter the name of the state: ").title()
    data_list = pandas.read_csv("50_states.csv")
    state_list = data_list["state"].to_list()
    x_list = data_list["x"].to_list()
    y_list = data_list["y"].to_list()
    if answer_state == "Exit":
        for state in state_list:
            if state not in answer_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        break
    if answer_state in state_list:
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data_list[data_list.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{answer_state}")
        answer_list.append(answer_state)
new_data.to_csv("missing_states.csv")