import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def verificar_faltas():
    try:
        # Pegando os valores digitados pelo usuário
        carga_horaria = int(entry_carga_horaria.get())
        faltas = int(entry_faltas.get())
        limite_faltas = int(carga_horaria * 0.30)

        # Limpando a janela anterior
        for widget in root.winfo_children():
            widget.pack_forget()

        if faltas >= limite_faltas:
            mensagem = f"Você excedeu o limite de faltas! Você tem {faltas} faltas e não pode mais faltar."
            img = Image.open('PodnaoMan.jpeg') 
        else:
            faltas_restantes = limite_faltas - faltas
            mensagem = f"Você tem {faltas} faltas. Ainda pode faltar {faltas_restantes} vezes."
            img = Image.open('Podfaltar.jpeg')  

        label_mensagem = tk.Label(root, text=mensagem, font=("Helvetica", 12))
        label_mensagem.pack(pady=10)

        img_resized = img.resize((150, 150))  
        img_tk = ImageTk.PhotoImage(img_resized)
        label_imagem = tk.Label(root, image=img_tk)
        label_imagem.image = img_tk  
        label_imagem.pack()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")


root = tk.Tk()
root.title("Verificação de Faltas")


label_carga_horaria = tk.Label(root, text="Digite a carga horária do curso:")
label_carga_horaria.pack(pady=5)

entry_carga_horaria = tk.Entry(root)
entry_carga_horaria.pack(pady=5)

label_faltas = tk.Label(root, text="Digite o número de faltas:")
label_faltas.pack(pady=5)

entry_faltas = tk.Entry(root)
entry_faltas.pack(pady=5)


botao_verificar = tk.Button(root, text="Verificar", command=verificar_faltas)
botao_verificar.pack(pady=20)


root.mainloop()
