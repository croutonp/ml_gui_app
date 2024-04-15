from taipy.gui import Gui

img_path = "placeholder_image.png"

content = ""

index = """
<|text-center|
<|{logo.png}|image|>

<|{content}|file_selector|>
select an image from your file system
>
"""

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)

