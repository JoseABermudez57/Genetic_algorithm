import tkinter as tk

window = tk.Tk()
window.title("Genetic Algorithm")
window.configure(bg="#C1FAA2")
window.geometry("500x200")
window.resizable(False, False)
resulting_value = tk.IntVar(value=0)

lbl_min_population = tk.Label(window, text="|Poblacion|")
first_population = tk.Entry(window, width=10)
lbl_min_population.place(x=30, y=20)
first_population.place(x=30, y=45)

lbl_max_population = tk.Label(window, text="|Poblacion_max|")
max_population = tk.Entry(window, width=10)
lbl_max_population.place(x=150, y=20)
max_population.place(x=165, y=45)

lbl_point_A = tk.Label(window, text="A")
pointA = tk.Entry(window, width=10)
lbl_point_A.place(x=300, y=20)
pointA.place(x=280, y=45)

labelPointB = tk.Label(window, text="B")
pointB = tk.Entry(window, width=10)
labelPointB.place(x=400, y=20)
pointB.place(x=380, y=45)

lbl_probability_crossbreeding = tk.Label(window, text="|Prob_cruza|")
probability_crossbreeding = tk.Entry(window, width=10)
lbl_probability_crossbreeding.place(x=30, y=80)
probability_crossbreeding.place(x=30, y=105)

lbl_individual_mutation_probability = tk.Label(window, text="|Prob_Mutacion_individuo|")
individual_mutation_probability = tk.Entry(window, width=10)
lbl_individual_mutation_probability.place(x=150, y=80)
individual_mutation_probability.place(x=185, y=105)

lbl_gen_mutation_probability = tk.Label(window, text="|Prob_Mutacion_gen|")
gen_mutation_probability = tk.Entry(window, width=10)
lbl_gen_mutation_probability.place(x=350, y=80)
gen_mutation_probability.place(x=385, y=105)

lbl_desired_resolution = tk.Label(window, text="Resolución deseada")
desired_resolution = tk.Entry(window, width=20)
lbl_desired_resolution.place(x=35, y=130)
desired_resolution.place(x=30, y=150)

lbl_resulting_value = tk.Label(window, text="Resultado")
min_values = tk.Checkbutton(window, text="Min", variable=resulting_value, onvalue=1)
max_values = tk.Checkbutton(window, text="Max", variable=resulting_value, onvalue=2)
lbl_resulting_value.place(x=220, y=130)
min_values.place(x=200, y=150)
max_values.place(x=250, y=150)

initiate_algorithm = tk.Button(window, text="Iniciar")
initiate_algorithm.place(x=380, y=145)

window.mainloop()
