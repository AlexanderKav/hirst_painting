import random
import turtle as turtle_module


my_color_list = [(253, 251, 247), (253, 247, 250), (236, 252, 244), (249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (240, 246, 251), (14, 205, 222)]

turtle_module.colormode(255)
tim = turtle_module.Turtle()
my_color_list = [(253, 251, 247), (253, 247, 250), (236, 252, 244), (249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (240, 246, 251), (14, 205, 222)]

tim.speed("fastest")
tim.hideturtle()
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot in range(1, number_of_dots +1):
    tim.dot(20, random.choice(my_color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()








