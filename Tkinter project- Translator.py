import tkinter as tk
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.argosopentech.com/")

language_data = lt.languages()
language_names = [lang["name"] for lang in language_data]
language_codes = {lang["name"]: lang["code"] for lang in language_data}

print(language_data)
app = tk.Tk()
app.geometry("700x400")
app.title("happy name")
app.config(bg="white")

app_name = tk.Label(app, text="happy translator", font="arial 15 bold", bg="white")
app_name.place(x=230, y=0)
# input
input_lable = tk.Label(app, text="Enter Text", font="arial 13 bold", bg="white", pady=5)
input_lable.place(x=85, y=45)

input_text = tk.Text(app, font="arial 10", height=11, width=30)
input_text.place(x=22, y=100)

input_lang = ttk.Combobox(app, width=19, values=language_names)
input_lang.place(x=56, y=75)
input_lang.set("Choose input language")
# ------------------------------------------------------------------------------------------
# output
output_lable = tk.Label(app, text="Output", font="arial 13 bold", bg="white", pady=5)
output_lable.place(x=480, y=45)

output_text = tk.Text(app, font="arial 10", height=11, width=30)
output_text.place(x=400, y=100)

output_lang = ttk.Combobox(app, width=19, values=language_names)
output_lang.place(x=440, y=75)
output_lang.set("Choose output language")


# ------------------------------------------------------------------------------------------
# button
def Translate():
    try:
        translated_text = lt.translate(
            input_text.get("1.0", tk.END),
            language_codes[input_lang.get()],
            language_codes[output_lang.get()],
        )
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
    except KeyError as ke:
        output_text.insert(tk.END, ke)


trans_btn = tk.Button(
    app, text=("Translate"), font="arial 10 bold", padx=5, command=Translate
)
trans_btn.place(x=305, y=180)
app.mainloop()
