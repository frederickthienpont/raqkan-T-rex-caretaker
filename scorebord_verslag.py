import time
import os
from datetime import datetime

# Scorebord bijwerken
class ScoreBoard:
    def __init__(self):
        self.scores = {}
    
    def update_score(self, team, points):
        if team in self.scores:
            self.scores[team] += points
        else:
            self.scores[team] = points
        print(f"Score bijgewerkt: {team} heeft nu {self.scores[team]} punten.")

    def display_scores(self):
        print("\n--- Scorebord ---")
        for team, score in self.scores.items():
            print(f"{team}: {score} punten")
        print("-----------------\n")

# Verslaggenerator
class ReportGenerator:
    def __init__(self, output_dir="verslagen"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate_report(self, title, content):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{title}_{timestamp}.txt"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"{title}\n")
            file.write("=" * len(title) + "\n")
            file.write(content + "\n")

        print(f"Verslag gegenereerd: {filepath}")

# Hoofdprogramma
if __name__ == "__main__":
    scoreboard = ScoreBoard()
    report_generator = ReportGenerator()

    # Scorebord bijwerken
    scoreboard.update_score("Team A", 10)
    scoreboard.update_score("Team B", 15)
    scoreboard.update_score("Team A", 5)
    scoreboard.display_scores()

    # Verslag genereren
    title = "Wedstrijdverslag"
    content = (
        "Dit is een automatisch gegenereerd verslag van de wedstrijd.\n"
        "De eindscore was als volgt:\n"
    )
    for team, score in scoreboard.scores.items():
        content += f"{team}: {score} punten\n"

    report_generator.generate_report(title, content)
