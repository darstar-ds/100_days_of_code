import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./Day25_US_STates_quiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_dataframe = pd.read_csv("./Day25_US_States_quiz/50_states.csv")
# print(states_dataframe.head())
states_list = states_dataframe["state"].tolist()
# print(states_list)
answer_state = turtle.textinput(title="Guess the State", prompt="What is another state's name:").title()
# print(answer_state)

def print_the_state_name(state_name, x_cor, y_cor):
    printer = turtle.Turtle()
    printer.penup()
    printer.hideturtle()
    printer.color("black")
    printer.goto(x_cor, y_cor)
    printer.write(state_name, align='left', font=('Arial', 10, 'bold'))

user_answers = []
state_counter = 0
is_end_game = False

while is_end_game == False:
    if answer_state == "Exit":
        rest_states_list = [st for st in states_list if st not in user_answers]
        # for state in user_answers:
        #     states_list.remove(state)
        # print(rest_states_list)
        df = pd.DataFrame(rest_states_list, columns = ["stany"])
        df.to_csv("./Day25_US_States_quiz/states_to_learn.csv")        
        break
    if answer_state in states_list:
        # print("Bingo")
        if answer_state in user_answers:
            pass
        else:
            state = states_dataframe[states_dataframe["state"] == answer_state]
            # print(state)
            x_cor = int(state.x)
            y_cor = int(state.y)
            # print(x_cor + y_cor)
            print_the_state_name(answer_state, x_cor, y_cor)
            user_answers.append(answer_state)
            state_counter += 1
    else:
        pass    
    answer_state = turtle.textinput(title=f"{state_counter}/50 - States correct", prompt="What is another state's name:").title()

screen.exitonclick()
