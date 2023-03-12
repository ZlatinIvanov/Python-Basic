from math import pi
type_of_figure = input()
if type_of_figure == "square":
    a_sq = float(input())
    area_square = a_sq*a_sq
    print(f"{area_square:.3f}")
if type_of_figure == "rectangle":
    a_rec = float(input())
    b_rec = float(input())
    area_rectangle = a_rec * b_rec
    print(f"{area_rectangle:.3f}")
if type_of_figure == "circle":
    r_circle = float(input())
    area_circle = pi*r_circle*r_circle
    print(f"{area_circle:.3f}")
if type_of_figure == "triangle":
    a_triangle = float(input())
    h_triangle = float(input())
    area_triangle = (a_triangle*h_triangle)/2
    print(f"{area_triangle:.3f}")