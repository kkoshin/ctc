import json
import os

def load_data():
    global colors
    color_json = open("./scripts/colors.json")
    colors = json.load(color_json)
    color_json.close()

def generate():
    path = "./build/scripts/"

    if not os.path.exists(path):
        os.makedirs(path)

    with open(os.path.join(path, 'colors.kt'), 'w') as file:
        file.write("""
import androidx.compose.ui.graphics.Color

""")
        for color in colors:
            file.write(f"""\
val {color['name']} = Color(0xFF{color['hex'][1:].upper()})
""")

if  __name__ == '__main__':
    load_data()
    generate()