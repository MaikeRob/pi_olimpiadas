import tkinter as tk
from tkinter import messagebox
from threading import Thread
import time


class StartScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Times")
        self.master.configure(background="white")
        self.master.geometry("1080x720+100+100")
        self.master.resizable(True, True)
        self.master.minsize(width=1080, height=720)
        

        # Times cadastrados
        self.teams = [
            "França",
            "Brasil",
            "Alemanha",
            "Estados Unidos",
            "Japão",
            "Canadá",
            "Polônia",
            "Peru",
            "Bolívia",
            "Alemanha",
            "Iuguslavia Central",
            "Republica Democratica do Congo",
            "Italia",
            "Espanha",
            "Mexico",
        ]

        # Frame Principal da tela
        self.frame_startscreen = tk.Frame(master, bg="#E7E7EC")

        # Escolha de Times
        self.team1_label = tk.Label(
            self.frame_startscreen,
            text="Escolha os times:",
            bg="#E7E7EC",
            font=("", 15),
        )
        self.team1_label.place(relx=0.083, rely=0.204, relwidth=0.218, relheight=0.043)

        self.team1_var = tk.StringVar(master)
        self.team1_var.set(self.teams[0])  # Definir o primeiro time como padrão
        self.team1_option = tk.OptionMenu(
            self.frame_startscreen,
            self.team1_var,
            *self.teams,
            command=self.update_team2,
        )
        self.team1_option.config(
            bg="#040404",
            fg="white",
            activebackground="#5B5B5B",
            activeforeground="white",
            font=("", 15),
            border=0,
        )
        self.team1_option["menu"].config(
            bg="#040404",
            fg="white",
            activebackground="#5B5B5B",
            activeforeground="white",
            font=("", 15),
        )
        self.team1_option.place(relx=0.109, rely=0.279, relheight=0.105)

        self.team2_var = tk.StringVar(master)
        self.team2_option = tk.OptionMenu(self.frame_startscreen, self.team2_var, "")
        self.team2_option.config(
            bg="#040404",
            fg="white",
            activebackground="#5B5B5B",
            activeforeground="white",
            font=("", 15),
            border=0,
        )
        self.team2_option["menu"].config(
            bg="#040404",
            fg="white",
            activebackground="#5B5B5B",
            activeforeground="white",
            font=("", 15),
        )
        self.team2_option.place(relx=0.393, rely=0.279, relheight=0.105)

        # Escolha de tipo de partida
        self.game_type_label = tk.Label(
            self.frame_startscreen, text="Tipo de partida:", bg="#E7E7EC", font=("", 15)
        )
        self.game_type_label.place(
            relx=0.083, rely=0.436, relwidth=0.192, relheight=0.045
        )

        self.game_type_var = tk.StringVar(master)
        self.game_type_var.set("Amistosa")  # Definir amistosa como padrão
        self.game_type_option = tk.OptionMenu(
            self.frame_startscreen, self.game_type_var, "Amistosa", "Profissional"
        )
        self.game_type_option.config(
            bg="#3A3A3A",
            fg="white",
            activebackground="#8B8B8B",
            activeforeground="white",
            font=("", 15),
            border=0,
        )
        self.game_type_option["menu"].config(
            bg="#3A3A3A",
            fg="white",
            activebackground="#8B8B8B",
            activeforeground="white",
            font=("", 15),
        )
        self.game_type_option.place(relx=0.109, rely=0.5, relheight=0.105)

        self.start_button = tk.Button(
            self.frame_startscreen,
            text="Iniciar Partida",
            bg="#040404",
            fg="white",
            font=("", 15),
            command=self.start_game,
            activebackground="#5B5B5B",
            activeforeground="white",
        )
        self.start_button.place(relx=0.355, rely=0.775, relwidth=0.287, relheight=0.128)
        
        self.frame_startscreen.place(
            relx=0.125, rely=0.15, relwidth=0.75, relheight=0.7
        )
           
    def update_team2(self, *args):
        selected_team = self.team1_var.get()
        self.team2_options = [team for team in self.teams if team != selected_team]
        self.team2_var.set(
            self.team2_options[0]
        )  # Definir o primeiro time disponível como padrão
        menu = self.team2_option["menu"]
        menu.delete(0, "end")  # Limpar opções existentes
        for team in self.team2_options:
            menu.add_command(label=team, command=tk._setit(self.team2_var, team))

        #Calcula a posição X do botão team2_option
        self.frame_startscreen.update()
        x_position = self.team1_option.winfo_width()+163#Constante
        self.team2_option.place(relx=x_position/810, rely=0.279, relheight=0.105)
        
            

    def start_game(self):
        team1_name = self.team1_var.get()
        team2_name = self.team2_var.get()
        game_type = self.game_type_var.get()

        game_window = tk.Toplevel(self.master)
        app = App(game_window, team1_name, team2_name, game_type)

        self.master.withdraw()


class App:
    def __init__(self, master, team1_name, team2_name, game_type):
        self.master = master
        self.master.configure(background="white")
        self.master.geometry("1080x720+100+100")
        self.master.resizable(True, True)
        self.master.minsize(width=1080, height=720)
        
        self.time = 0
        self.running = False
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.game_type = game_type

        # Pontuação
        self.score_team1 = 0
        self.score_team2 = 0

        # Sets
        self.sets_team1 = 0
        self.sets_team2 = 0

        # Interface
        self.placar_frame = tk.Frame(master, bg="#E7E7EC")

        self.team1_name_label = tk.Label(
            self.placar_frame, 
            bg="#040404", 
            text=self.team1_name,
            fg="white",
            font=("", 15)
            )
        self.team1_name_label.place(relx=0,rely=0.053,relwidth=0.215, relheight=0.888)

        self.team1_sets_title = tk.Label(
            self.placar_frame,
            bg="#040404", 
            text="SETS",
            fg="white",
            font=("", 15))
        self.team1_sets_title.place(relx=0.223,rely=0.053,relwidth=0.120, relheight=0.223)

        self.team1_sets_points= tk.Label(
            self.placar_frame,
            bg="#040404", 
            text=self.sets_team1,
            fg="white",
            font=("", 60))
        self.team1_sets_points.place(relx=0.223,rely=0.276,relwidth=0.120, relheight=0.664)
        
        self.team1_points= tk.Label(
            self.placar_frame,
            bg="#F2C468", 
            text=self.score_team1,
            fg="white",
            font=("", 90))
        self.team1_points.place(relx=0.350,rely=0.053,relwidth=0.134, relheight=0.888)
        

        self.team2_name_label = tk.Label(
            self.placar_frame, 
            bg="#040404", 
            text=self.team2_name,
            fg="white",
            font=("", 15)
            )
        self.team2_name_label.place(relx=0.784,rely=0.053,relwidth=0.219, relheight=0.888)

        self.team2_sets_title = tk.Label(
            self.placar_frame,
            bg="#040404", 
            text="SETS",
            fg="white",
            font=("", 15))
        self.team2_sets_title.place(relx=0.656,rely=0.053,relwidth=0.120, relheight=0.223)

        self.team2_sets_points= tk.Label(
            self.placar_frame,
            bg="#040404", 
            text=self.sets_team2,
            fg="white",
            font=("", 60))
        self.team2_sets_points.place(relx=0.656,rely=0.276,relwidth=0.120, relheight=0.664)
        
        self.team2_points= tk.Label(
            self.placar_frame,
            bg="#F2C468", 
            text=self.score_team2,
            fg="white",
            font=("", 90))
        self.team2_points.place(relx=0.513,rely=0.053,relwidth=0.134, relheight=0.888)

        self.placar_frame.place(relx=0,rely=0.031,relwidth=1, relheight=0.261)


        self.timer_label = tk.Label(
            self.master,
            bg="#040404", 
            text="00:00",
            fg="white",
            font=("", 100))
        self.timer_label.place(relx=0.312, rely=0.336, relwidth=0.374, relheight=0.220)


        self.start_button = tk.Button(
            self.master,
            text="Iniciar",
            bg="#E7E7EC",
            fg="black",
            font=("", 30),
            command=self.start_timer,
            activebackground="#EBEBEB",
            activeforeground="black",
        )
        self.start_button.place(relx=0.047, rely=0.404, relwidth=0.175, relheight=0.084)


        self.point_button1 = tk.Button(
            self.master,
            text=f"Ponto para {self.team1_name}",
            bg="#E7E7EC",
            fg="black",
            font=("", 20),
            command=self.point_team1,
            activebackground="#EBEBEB",
            activeforeground="black",
        )
        self.point_button1.place(relx=0.029, rely=0.644, relwidth=0.287, relheight=0.084)


        self.point_button2 = tk.Button(
            self.master,
            text=f"Ponto para {self.team2_name}",
            bg="#E7E7EC",
            fg="black",
            font=("", 20),
            command=self.point_team2,
            activebackground="#EBEBEB",
            activeforeground="black",
        )
        self.point_button2.place(relx=0.029, rely=0.748, relwidth=0.287, relheight=0.084)

        self.restart_button = tk.Button(
            self.master,
            text="Recomeçar",
            bg="#E7E7EC",
            fg="black",
            font=("", 20),
            command=self.restart_game,
            activebackground="#EBEBEB",
            activeforeground="black",
        )
        self.restart_button.place(relx=0.029, rely=0.852, relwidth=0.287, relheight=0.084) 

    def start_timer(self):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self.timer)
            self.thread.start()
            self.timer_label.config(bg="#135C0C")

    def timer(self):
        while self.running:
            mins, secs = divmod(self.time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(mins, secs))
            time.sleep(1)
            self.time += 1

    def point_team1(self):
        # if not self.running:
        #     messagebox.showwarning("Alerta", "O cronômetro está parado. Inicie o cronômetro antes de pontuar.")
        #     return
        self.score_team1 += 1
        self.team1_points.config(text=self.score_team1)
        if (
            self.game_type == "Amistosa"
            and self.score_team1 >= 25
            and self.score_team1 >= self.score_team2 + 2
        ):
            self.end_game()
        elif (
            self.game_type == "Profissional"
            and self.sets_team1 == 2
            and self.sets_team2 == 2
        ):
            if self.score_team1 >= 15 and self.score_team1 >= self.score_team2 + 2:
                self.sets_team1 += 1
                self.check_sets()
            elif self.score_team1 == 14 and self.score_team2 == 14:
                messagebox.showinfo(
                    "Informação",
                    "O set está empatado em 14 a 14. Ganha quem abrir 2 pontos de vantagem",
                )
        elif (
            self.game_type == "Profissional"
            and self.sets_team1 != 2
            and self.score_team1 >= 25
            and self.score_team1 >= self.score_team2 + 2
        ):
            self.sets_team1 += 1
            self.check_sets()
        elif self.score_team1 == 24 and self.score_team2 == 24:
            messagebox.showinfo(
                "Informação",
                "O set só terminará quando houver uma diferença de pelo menos dois pontos.",
            )
            return
        self.pause_timer()

    def point_team2(self):
        # if not self.running:
        #     messagebox.showwarning("Alerta", "O cronômetro está parado. Inicie o cronômetro antes de pontuar.")
        #     return
        self.score_team2 += 1
        self.team2_points.config(text=self.score_team2)
        if (
            self.game_type == "Amistosa"
            and self.score_team2 >= 25
            and self.score_team2 >= self.score_team1 + 2
        ):
            self.end_game()
        elif (
            self.game_type == "Profissional"
            and self.sets_team1 == 2
            and self.sets_team2 == 2
        ):
            if self.score_team2 >= 15 and self.score_team2 >= self.score_team1 + 2:
                self.sets_team2 += 1
                self.check_sets()
            elif self.score_team1 == 14 and self.score_team2 == 14:
                messagebox.showinfo(
                    "Informação",
                    "O set está empatado em 14 a 14. Ganha quem abrir 2 pontos de vantagem.",
                )
        elif (
            self.game_type == "Profissional"
            and self.sets_team2 != 2
            and self.score_team2 >= 25
            and self.score_team2 >= self.score_team1 + 2
        ):
            self.sets_team2 += 1
            self.check_sets()
        elif self.score_team1 == 24 and self.score_team2 == 24:
            messagebox.showinfo(
                "Informação",
                "O set só terminará quando houver uma diferença de pelo menos dois pontos.",
            )
            return
        self.pause_timer()

    def check_sets(self):
        if self.sets_team1 == 3 or self.sets_team2 == 3:
            self.end_game()
        else:
            self.score_team1 = 0
            self.score_team2 = 0
            self.team1_points.config(text=self.score_team1)
            self.team2_points.config(text=self.score_team2)
            if self.sets_team1 == 2 and self.sets_team2 == 2:
                messagebox.showinfo("Informação", "OVERTIME - Último set iniciado!")
            self.team1_sets_points.config(text=self.sets_team1)
            self.team2_sets_points.config(text=self.sets_team2)

    def end_game(self):
        self.running = False
        if self.sets_team1 > self.sets_team2:
            winner = self.team1_name
        elif self.sets_team2 > self.sets_team1:
            winner = self.team2_name
        else:
            winner = "Empate"
        messagebox.showinfo("Fim de Jogo", f"O jogo terminou! O vencedor é: {winner}")

    def pause_timer(self):
        self.running = False
        self.timer_label.config(bg="#040404")
        

    def restart_game(self):
        self.master.destroy()  # Destruir a janela atual do jogo
        root.deiconify()  # Mostrar a janela principal novamente


root = tk.Tk()
start_screen = StartScreen(root)
root.mainloop()