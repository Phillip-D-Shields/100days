import colorgram

colors_raw = colorgram.extract('triangles.png', 12)

colors_clean = []

for color in colors_raw:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    new_color = (red, green, blue)
    colors_clean.append(new_color)

print(colors_clean)