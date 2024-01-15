from tkinter import *
from operations.do_operations import start_simulation as start


class Ventana:

    def __init__(self):
        principal = Tk()
        principal.title('Algoritmo Genético')
        principal.geometry('801x259')
        principal.config(bg='#1a1c1d')
        self.resulting_value = BooleanVar()

        principal.resizable(0, 0)
        self.pobation = Label(principal, text='|Población|', bg='#1a1c1d', fg='#ffffff',
                              font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.pobation.place(x=45, y=26)
        self.poblation = Label(principal, text='|Población max|', bg='#1a1c1d', fg='#ffffff',
                               font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.poblation.place(x=180, y=26)
        self.pointa = Label(principal, text='A', bg='#1a1c1d', fg='#ffffff', font=('Comic Sans MS', 12, 'bold'),
                            justify=LEFT)
        self.pointa.place(x=405, y=26)
        self.pointb = Label(principal, text='B', bg='#1a1c1d', fg='#ffffff', font=('Comic Sans MS', 12, 'bold'),
                            justify=LEFT)
        self.pointb.place(x=495, y=26)
        self.lbliterations = Label(principal, text='Número de iteraciones', bg='#1a1c1d', fg='#ffffff',
                                   font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.lbliterations.place(x=560, y=26)
        self.entrypoblation = Entry(principal, width='8', insertbackground='#000000', bg='#ffffff', fg='#000000',
                                    font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.entrypoblation.place(x=45, y=52)
        self.maxpoblationentry = Entry(principal, width='9', insertbackground='#000000', bg='#ffffff', fg='#000000',
                                       font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.maxpoblationentry.place(x=195, y=52)
        self.entrya = Entry(principal, width='7', insertbackground='#000000', bg='#ffffff', fg='#000000',
                            font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.entrya.place(x=375, y=52)
        self.entryb = Entry(principal, width='7', insertbackground='#000000', bg='#ffffff', fg='#000000',
                            font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.entryb.place(x=465, y=52)
        self.iterationsentry = Entry(principal, width='7', insertbackground='#000000', bg='#f2f2f2', fg='#000000',
                                     font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.iterationsentry.place(x=615, y=52)
        self.probmutindv = Label(principal, text='|Prob_mutación_individuo|', bg='#1a1c1d', fg='#ffffff',
                                 font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.probmutindv.place(x=30, y=104)
        self.probmutgen = Label(principal, text='|Prob_mutación_gen|', bg='#1a1c1d', fg='#ffffff',
                                font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.probmutgen.place(x=300, y=104)
        self.lblresolution = Label(principal, text='Resolución deseada', bg='#1a1c1d', fg='#ffffff',
                                   font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.lblresolution.place(x=548, y=104)
        self.probmutindventry = Entry(principal, width='16', insertbackground='#000000', bg='#ffffff', fg='#000000',
                                      font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.probmutindventry.place(x=45, y=130)
        self.probmutgenentry = Entry(principal, width='13', insertbackground='#000000', bg='#ffffff', fg='#000000',
                                     font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.probmutgenentry.place(x=323, y=130)
        self.resolutionentry = Entry(principal, width='14', insertbackground='#000000', bg='#ffffff', fg='#000000',
                                     font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.resolutionentry.place(x=555, y=130)
        self.mandandmin = Label(principal, text='Resultado', bg='#1a1c1d', fg='#ffffff',
                                font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.mandandmin.place(x=105, y=182)
        self.minvalue = Checkbutton(principal, text='Min', bg='#1a1c1d', fg='#000000',
                                    font=('Comic Sans MS', 12, 'normal'), variable=self.resulting_value, onvalue=True)
        self.minvalue.place(x=60, y=208)
        self.maxvalue = Checkbutton(principal, text='Max', bg='#1a1c1d', fg='#000000',
                                    font=('Comic Sans MS', 12, 'normal'), variable=self.resulting_value, onvalue=False)
        self.maxvalue.place(x=185, y=208)

        Button(principal, width='16', text='calcular', bg='#c2e3bf', fg='#000000',
               font=('Comic Sans MS', 12, 'bold'), command=self.do_simulation).place(x=555, y=195)

        principal.mainloop()

    def do_simulation(self):
        data = {
            "a": self.entrya.get(),
            "b": self.entryb.get(),
            "pob_min": self.entrypoblation.get(),
            "pob_max": self.maxpoblationentry.get(),
            "iterations": self.iterationsentry.get(),
            "prob_mut_individual": self.probmutindventry.get(),
            "prob_mut_gene": self.probmutgenentry.get(),
            "res": self.resolutionentry.get(),
            "max_or_min": self.resulting_value
        }

        start(data)


if __name__ == "__main__":
    Ventana()
