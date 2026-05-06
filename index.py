from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#janela principal
janela = Tk()
janela.title("Cadastro de Pacientes")
janela.geometry("900x400")

#### Notebook (abas)
abas = ttk.Notebook(janela)
abas.pack(fill="both",expand=True)

#aba1 - Cadastro
aba1 = Frame(abas)
abas.add(aba1, text="Pacientes")

#aba2 - Tabela
aba2 = Frame(abas)
abas.add(aba2, text="Cadastros")

#Funcao Cadastrar
def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    nascimento = entry_nascimento.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    convenio = entry_convenio.get()
    contato = entry_contato.get()

    if nome == "" or cpf == "" or nascimento == "" or telefone == "" or email =="" or convenio =="" or contato == "" :
        messagebox.showwarning("Erro","Todos os campos sao obrigatorios! ")
    else:
        tabela.insert("",END,values=(nome, cpf, nascimento, telefone, email, convenio, contato))
        entry_nome.delete(0,END)
        entry_cpf.delete(0,END)
        entry_nascimento.delete(0,END)
        entry_telefone.delete(0,END)  
        entry_email.delete(0,END)  
        entry_convenio.delete(0,END)  
        entry_contato.delete(0,END)  

        messagebox.showinfo("sucesso","Cliente cadastrado com sucesso")  


###aba Cadastro
Label(aba1, text="Nome Completo").pack(pady=5)
entry_nome = Entry(aba1, width=40)
entry_nome.pack()

Label(aba1, text="CPF").pack(pady=2)
entry_cpf = Entry(aba1, width=13)
entry_cpf.pack()

Label(aba1, text="Data de Nascimento").pack(pady=1)
entry_nascimento = Entry(aba1, width=40)
entry_nascimento.pack()

Label(aba1, text="Telefone").pack(pady=1)
entry_telefone = Entry(aba1, width=11)
entry_telefone.pack()

Label(aba1, text="E-mail").pack(pady=1)
entry_email = Entry(aba1, width=11)
entry_email.pack()

Label(aba1, text="Convenio/SUS").pack(pady=1)
entry_convenio = Entry(aba1, width=11)
entry_convenio.pack()

Label(aba1, text="Contato de Emergencia").pack(pady=1)
entry_contato = Entry(aba1, width=11)
entry_contato.pack()

Button(
    aba1,
    text="Cadastrar",
    bg="green",
    fg="white",
    width=20,
    command=cadastrar
).pack(pady=20)



####aba tabela
colunas = ("Nome", "CPF","nascimento", "Telefone", "email","convenio", "contato")
tabela=ttk.Treeview(
    aba2,
    columns=colunas,
    show= "headings"
)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)

tabela.pack(fill = "both", expand=True, pady=20)

janela.mainloop()