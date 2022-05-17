import colorgram as cg

color_list = cg.extract("colorgram.jpeg", 30)
color_palette = []
for count in range(len(color_list)):
    rgb = color_list[count]
    color = rgb.rgb
    color_palette.append(color)
print(color_palette)