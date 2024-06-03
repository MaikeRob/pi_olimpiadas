import tkinter as tk

#import configs
import db.queries as db
import random
from application import App, teams, root

class Team:
    def __init__(self, name):
        self.name = name

class Match:
    def __init__(self, team1, team2, winner=None):
        self.team1 = team1
        self.team2 = team2
        self.winner = winner

def generateBracket(teams):
    matches = []
    for i in range(0, len(teams), 2):
        match = Match(teams[i], teams[i + 1])
        matches.append(match)
    return matches

def showBracket(matches):
    for i, match in enumerate(matches, start=1):
        print(f"Match {i}: {match.team1.name} vs {match.team2.name}")

def playMatch(match, team1, team2):
    game_window = tk.Toplevel(root)
    app_instance = App(game_window, team1.name, team2.name, 'Profissional')


def advanceWinners(matches):
    next_round = []
    for i in range(0, len(matches), 2):
        winner = matches[i].winner
        next_round.append(Match(matches[i].winner, matches[i + 1].winner))
    return next_round


def run():
    teams = db.getCountries()
    selected_teams_names = random.sample(teams, 8)
    selected_teams = [Team(name) for name in selected_teams_names]

    # Gera chaveamento inicial 
    bracket = generateBracket(selected_teams)

    for match in bracket:
        playMatch(match, match.team1, match.team2)  
        next_round = advanceWinners(bracket)

