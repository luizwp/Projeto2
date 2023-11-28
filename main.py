from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def clicou() -> None:
    # Como pegar os dados digitados/selecionados nos campos?
    nome = txtNome.get()
    curso = txtCurso.get()

    # Como enviar caixas de alerta?
    messagebox.showinfo('Dados enviados!', f'Seu nome: {nome} '
                                           f'\nSeu curso: {curso}')

    # Como limpar os campos?
    txtNome.delete(0, END)
    txtCurso.set('')



# Como criar uma janela?
janela = Tk()

# Como colocar um título na janela?
janela.title('Primeira janela')

# Como modificar largura e altura da janela?
janela.geometry('300x150+750+400')

# Como criar um label?
labelNome = Label(janela, text='Nome:', fg='red', font='Tahoma 16')
# Como adicionar um widget na janela?
labelNome.grid(row=0, column=0)

labelCurso = Label(janela, text='Curso:', fg='red', font='Tahoma 16')
labelCurso.grid(row=1, column=0)

# Como criar um campo de texto?
txtNome = Entry(janela, font='Tahoma 16')
txtNome.grid(row=0, column=1)

# Como criar um ComboBox
txtCurso = ttk.Combobox(janela,
                        values=['Python', 'Java', 'Javascript', 'Node'],
                        font='Tahoma 16',  width=18)
txtCurso.grid(row=1, column=1)

# Como criar um botão?
btnEnviar = Button(janela, text='Enviar', bg='red', fg='white',
                   font='Tahoma 14 bold', activebackground='white',
                   activeforeground='red', command=clicou)
btnEnviar.grid(row=2, column=0)


# Como alterar o texto de um label?
texto = StringVar()
txtEnviar = Label(janela, text='', textvariable=texto, fg='red', font='Tahoma 16')
txtEnviar.grid(row=3, column=0, columnspan=2)





# Como exibir a janela?
janela.mainloop()
