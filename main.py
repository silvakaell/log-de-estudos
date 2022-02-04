from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- procurar log do dia ------------------------------- #

def find_study():
    month = month_label_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="data not found")
    else:
        if month in data:
            day = data[month]["dia"]
            entrada = data[month]["entrada"]
            saida = data[month]["saida"]
            conteudo = data[month]["conteudo"]
            messagebox.showinfo(title=month, message=f"day: {day}\nentrada: {entrada}\nconteúdo: {conteudo}")
        else:
            messagebox.showinfo(title="error", message="entrada não encontrada")


# ---------------------------- escrever o log ------------------------------- #

# uma função aqui para escrever que coisas eu pego nas entries, e salvar em um arquivo JSON

def create_logfile():
    day = day_label_entry.get()
    month = month_label_entry.get()
    entrada = entrada_label_entry.get()
    saida = saida_label_entry.get()
    conteudo = conteudo_label_entry.get()

    new_data = {
        f"{day}/{month}": {
            "dia": day,
            "entrada": entrada,
            "saida": saida,
            "conteudo": conteudo,
        }
    }

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        with open("data.json", "w") as data_file:
            data.update(new_data)
            json.dump(data, data_file, indent=4)
    finally:
        day_label_entry.delete(0, END)
        month_label_entry.delete(0, END)
        entrada_label_entry.delete(0, END)
        saida_label_entry.delete(0, END)
        conteudo_label_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Log de estudos do Kamon")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="estudos.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, pady=10, padx=10)

day_label = Label(text="Dia")
day_label.grid(column=0, row=2)

day_label_entry = Entry(width=35)
day_label_entry.grid(column=1, row=2)

month_label = Label(text="Mês")
month_label.grid(column=0, row=3)

month_label_entry = Entry(width=35)
month_label_entry.grid(column=1, row=3)

entrada_label = Label(text="Entrada")
entrada_label.grid(column=0, row=4)

entrada_label_entry = Entry(width=35)
entrada_label_entry.grid(column=1, row=4)

saida_label = Label(text="Saída")
saida_label.grid(column=0, row=5)

saida_label_entry = Entry(width=35)
saida_label_entry.grid(column=1, row=5)

adicionar_entrada_button = Button(text="Adicionar entrada", width=15, command=create_logfile)
adicionar_entrada_button.grid(column=1, row=7, pady=10, padx=10)

conteudo_label = Label(text="Conteúdo")
conteudo_label.grid(column=0, row=6)

conteudo_label_entry = Entry(width=35)
conteudo_label_entry.grid(column=1, row=6, columnspan=4)

search_button = Button(text="Procurar entradas", width=15, command=find_study)
search_button.grid(column=1, row=8)

window.mainloop()
