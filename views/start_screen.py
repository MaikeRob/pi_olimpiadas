import configs



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
