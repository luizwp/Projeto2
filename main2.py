from tkinter import *
from tkinter import messagebox

def clicou() -> None:
    Peso = txtPeso.get()
    altura = txtAltura.get()
    IMC =

    messagebox.showinfo('Dados enviados!', f'Seu Peso: {Peso} '
                                           f'\nSua Altura: {altura}' f'\nSeu IMC: {IMC}')


janela = Tk()

janela.title('Segunda janela')


labelIMC = Label(janela, text='IMC:', fg='red', font='Tahoma 16')
labelIMC.grid(row=3, column=0)


labelPeso = Label(janela, text='Peso:', fg='red', font='Tahoma 16')
labelPeso.grid(row=0, column=0)

labelAltura = Label(janela, text='Altura:', fg='red', font='Tahoma 16')
labelAltura.grid(row=1, column=0)

txtPeso = Entry(janela, font='Tahoma 16')
txtPeso.grid(row=0, column=1)

txtAltura = Entry(janela, font='Tahoma 16')
txtAltura.grid(row=1, column=1)

btnEnviar = Button(janela, text='Enviar', bg='red', fg='white',
                   font='Tahoma 14 bold', activebackground='white',
                   activeforeground='red', command=clicou)
btnEnviar.grid(row=2, column=0)







janela.mainloop()







