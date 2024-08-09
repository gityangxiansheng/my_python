from tkinter import *
import requests


def get_quote():
        data_s = requests.get(url="https://api.xygeng.cn/one")
        data_json = data_s.json()
        while len(data_json["data"]["content"]) > 40:
            data_s = requests.get(url="https://api.xygeng.cn/one")
            data_json = data_s.json()
        canvas.itemconfig(quote_text,text=data_json["data"]["content"])



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"python\33day\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"python\33day\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


get_quote()
window.mainloop()