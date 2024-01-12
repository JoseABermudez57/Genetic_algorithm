import tkinter as tk

window = tk.Tk()
window.title("Genetic Algorithm")
window.configure(bg="#C1FAA2")
window.geometry("500x200")
window.resizable(False, False)
resultingValue = tk.IntVar(value=0)

labelMinPopulation = tk.Label(window, text="|Poblacion|")
firstPopulation = tk.Entry(window, width=10)
labelMinPopulation.place(x=30, y=20)
firstPopulation.place(x=30, y=45)

labelMaxPopulation = tk.Label(window, text="|Poblacion_max|")
maxPopulation = tk.Entry(window, width=10)
labelMaxPopulation.place(x=150, y=20)
maxPopulation.place(x=165, y=45)

labelPointA = tk.Label(window, text="A")
pointA = tk.Entry(window, width=10)
labelPointA.place(x=300, y=20)
pointA.place(x=280, y=45)

labelPointB = tk.Label(window, text="B")
pointB = tk.Entry(window, width=10)
labelPointB.place(x=400, y= 20)
pointB.place(x=380, y=45)

labelProbabilityOfCrossbreeding = tk.Label(window, text="|Prob_cruza|")
probabilityOfCrossbreeding = tk.Entry(window, width=10)
labelProbabilityOfCrossbreeding.place(x=30, y=80)
probabilityOfCrossbreeding.place(x=30, y=105)

labelIndividualMutationProbability = tk.Label(window, text="|Prob_Mutacion_individuo|")
individualMutationProbability = tk.Entry(window, width=10)
labelIndividualMutationProbability.place(x=150, y=80)
individualMutationProbability.place(x=185, y=105)

labelGenMutationProbability = tk.Label(window, text="|Prob_Mutacion_gen|")
genMutationProbability = tk.Entry(window, width=10)
labelGenMutationProbability.place(x=350, y=80)
genMutationProbability.place(x=385, y=105)

labelDesiredResolution = tk.Label(window, text="Resolución deseada")
desiredResolution = tk.Entry(window, width=20)
labelDesiredResolution.place(x=35, y=130)
desiredResolution.place(x=30, y=150)

labelResultingValue = tk.Label(window, text="Resultado")
minValues = tk.Checkbutton(window, text="Min", variable=resultingValue, onvalue=1)
maxValues = tk.Checkbutton(window, text="Max", variable=resultingValue, onvalue=2)
labelResultingValue.place(x=220, y=130)
minValues.place(x=200, y=150)
maxValues.place(x=250, y=150)

initiateAlgorithm = tk.Button(window, text="Iniciar")
initiateAlgorithm.place(x=380, y=145)

window.mainloop()