#define two set of colors
color_list_1 = set(["White","Black","Red"])
color_list_2 = set(["Red","Green"])

#find colors in color_list_1 but not in color_list_2
result = color_list_1-color_list_2
print(result)