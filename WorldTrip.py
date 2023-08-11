import tkinter as tk
from tkinter import ttk
import random

class UnusualTravelPlanner:
    def __init__(self):
        self.destinations = [
            "Ilha de Páscoa, Chile",
            "Bled, Eslovênia",
            "Luang Prabang, Laos",
            "Svalbard, Noruega",
            "Machu Picchu, Peru",
            "Cappadocia, Turquia",
            "Salar de Uyuni, Bolívia",
            "Chefchaouen, Marrocos",
            "Fernando de Noronha, Brasil",
            "Plitvice Lakes, Croácia"
        ]
        
        self.activities = [
            "Participar de um festival local",
            "Explorar trilhas desconhecidas",
            "Experimentar a culinária local",
            "Conhecer artistas locais",
            "Fazer um passeio de balão",
            "Participar de um retiro espiritual",
            "Fazer mergulho",
            "Realizar voluntariado comunitário",
            "Visitar um museu incomum",
            "Fazer um piquenique em um local pitoresco"
        ]

    def suggest_destination(self):
        return random.choice(self.destinations)

    def suggest_activity(self):
        return random.choice(self.activities)

class TravelAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistente de Planejamento de Viagem")
        

        self.planner = UnusualTravelPlanner()

        self.main_label = ttk.Label(root, text="Bem-vindo ao Word Trip!")
        self.main_label.pack()

        self.menu_frame = ttk.Frame(root)
        self.menu_frame.pack()

        self.destination_button = ttk.Button(self.menu_frame, text="Clique para receber uma sugestão de destino", command=self.show_destination)
        self.destination_button.pack(side="left")

        self.activity_button = ttk.Button(self.menu_frame, text="Clique para receber uma sugestão de Atividade", command=self.show_activity)
        self.activity_button.pack(side="left")

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack()

    def show_destination(self):
        destination = self.planner.suggest_destination()
        self.result_label.config(text=f"Sugestão de Destino: {destination}")
        self.menu_frame.pack_forget()
        self.result_label.pack()

    def show_activity(self):
        activity = self.planner.suggest_activity()
        self.result_label.config(text=f"Sugestão de Atividade: {activity}")
        self.menu_frame.pack_forget()
        self.result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelAssistantApp(root)
    root.mainloop()
