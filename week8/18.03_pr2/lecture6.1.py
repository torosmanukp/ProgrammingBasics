def change_coords(x1, y1, x2, y2, dick):
    dick["coords"]=[[x1, y1], [x2, y2]]
    dick["width"]=abs(x1-x2)
    dick["height"]=abs(y1-y2)
    return dick

figures=[
    {"width": 7, "height": 6, "color": "blue", "coords": [[0, 6], [7, 0]]},
    {"width": 10, "height": 5, "color": "blue", "coords": [[0, 5], [10, 0]]}
]

rectangle = {
    "width" : 7,
    "height" : 6,
    "color" : "blue",
    "coords" : [[0, 6], [7, 0]]
}
print(rectangle)

for figure in figures:
    print(figure["coords"])

rectangle2=change_coords(1, 7, 4, 4, rectangle)
print(rectangle2)