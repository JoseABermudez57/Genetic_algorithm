from tkinter import *
from operations.do_operations import start_simulation as start


class Ventana:

    def __init__(self):
        window = Tk()
        window.title('Algoritmo Genético')
        window.geometry('801x259')
        window.config(bg='#1a1c1d')
        self.resulting_value = BooleanVar()

        window.resizable(False, False)
        self.population_min = Label(window, text='|Población minima|', bg='#1a1c1d', fg='#ffffff',
                                    font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.population_min.place(x=20, y=26)
        self.population_max = Label(window, text='|Población maxima|', bg='#1a1c1d', fg='#ffffff',
                                    font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.population_max.place(x=180, y=26)
        self.point_a = Label(window, text='A', bg='#1a1c1d', fg='#ffffff', font=('Comic Sans MS', 12, 'bold'),
                             justify=LEFT)
        self.point_a.place(x=405, y=26)
        self.point_b = Label(window, text='B', bg='#1a1c1d', fg='#ffffff', font=('Comic Sans MS', 12, 'bold'),
                             justify=LEFT)
        self.point_b.place(x=495, y=26)
        self.lbl_iterations = Label(window, text='Número de iteraciones', bg='#1a1c1d', fg='#ffffff',
                                    font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.lbl_iterations.place(x=560, y=26)
        self.min_population_entry = Entry(window, width=8, insertbackground='#000000', bg='#ffffff', fg='#000000',
                                          font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.min_population_entry.place(x=45, y=52)
        self.max_population_entry = Entry(window, width=9, insertbackground='#000000', bg='#ffffff', fg='#000000',
                                          font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.max_population_entry.place(x=195, y=52)
        self.entry_a = Entry(window, width=7, insertbackground='#000000', bg='#ffffff', fg='#000000',
                             font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.entry_a.place(x=375, y=52)
        self.entry_b = Entry(window, width=7, insertbackground='#000000', bg='#ffffff', fg='#000000',
                             font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.entry_b.place(x=465, y=52)
        self.iterations_entry = Entry(window, width=7, insertbackground='#000000', bg='#f2f2f2', fg='#000000',
                                      font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.iterations_entry.place(x=615, y=52)
        self.lbl_prob_mut_individual = Label(window, text='|Prob_mutación_individuo|', bg='#1a1c1d', fg='#ffffff',
                                             font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.lbl_prob_mut_individual.place(x=30, y=104)
        self.lbl_prob_mut_gen = Label(window, text='|Prob_mutación_gen|', bg='#1a1c1d', fg='#ffffff',
                                      font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.lbl_prob_mut_gen.place(x=300, y=104)
        self.lbl_resolution = Label(window, text='Resolución deseada', bg='#1a1c1d', fg='#ffffff',
                                    font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.lbl_resolution.place(x=548, y=104)
        self.prob_mut_individual_entry = Entry(window, width=16, insertbackground='#000000', bg='#ffffff',
                                               fg='#000000',
                                               font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.prob_mut_individual_entry.place(x=45, y=130)
        self.prob_mut_gen_entry = Entry(window, width=13, insertbackground='#000000', bg='#ffffff', fg='#000000',
                                        font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.prob_mut_gen_entry.place(x=323, y=130)
        self.resolution_entry = Entry(window, width=14, insertbackground='#000000', bg='#ffffff', fg='#000000',
                                      font=('Comic Sans MS', 12, 'normal'), justify=LEFT)
        self.resolution_entry.place(x=555, y=130)
        self.lbl_max_and_min = Label(window, text='Resultado', bg='#1a1c1d', fg='#ffffff',
                                     font=('Comic Sans MS', 12, 'bold'), justify=LEFT)
        self.lbl_max_and_min.place(x=105, y=182)
        self.min_value = Checkbutton(window, text='Minimizacion', bg='#1a1c1d', fg='#000000',
                                     font=('Comic Sans MS', 12, 'normal'), variable=self.resulting_value, onvalue=True)
        self.min_value.place(x=60, y=208)
        self.max_value = Checkbutton(window, text='Maximizacion', bg='#1a1c1d', fg='#000000',
                                     font=('Comic Sans MS', 12, 'normal'), variable=self.resulting_value, onvalue=False)
        self.max_value.place(x=185, y=208)

        Button(window, width=16, text='calcular', bg='#c2e3bf', fg='#000000',
               font=('Comic Sans MS', 12, 'bold'), command=self.do_simulation).place(x=555, y=195)

        window.mainloop()

    def do_simulation(self):
        data = {
            "a": self.entry_a.get(),
            "b": self.entry_b.get(),
            "pob_min": self.min_population_entry.get(),
            "pob_max": self.max_population_entry.get(),
            "iterations": self.iterations_entry.get(),
            "prob_mut_individual": self.prob_mut_individual_entry.get(),
            "prob_mut_gene": self.prob_mut_gen_entry.get(),
            "res": self.resolution_entry.get(),
            "max_or_min": self.resulting_value.get()
        }

        start(data)


if __name__ == "__main__":
    Ventana()
