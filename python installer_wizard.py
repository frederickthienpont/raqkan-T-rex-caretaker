import os
import subprocess

def install_requirements():
    """Installeer vereiste pakketten vanuit requirements.txt."""
    if os.path.exists("requirements.txt"):
        print("Bezig met het installeren van vereiste pakketten...")
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("Alle pakketten zijn geïnstalleerd!")
    else:
        print("requirements.txt niet gevonden. Zorg ervoor dat deze aanwezig is in de hoofdmap.")

def setup_configuration():
    """Maak een configuratiebestand aan."""
    config_file = "config.ini"
    if not os.path.exists(config_file):
        print("Configuratiebestand wordt aangemaakt...")
        with open(config_file, "w") as file:
            file.write("[Instellingen]\n")
            file.write("option1=waarde1\n")
            file.write("option2=waarde2\n")
        print(f"Configuratiebestand aangemaakt: {config_file}")
    else:
        print(f"Configuratiebestand bestaat al: {config_file}")

def show_welcome_message():
    """Toon een welkomstbericht."""
    print("=" * 40)
    print("Welkom bij de Installer Wizard voor Raqkan T-Rex Caretaker!")
    print("=" * 40)

def main():
    """Hoofdprogramma van de installer wizard."""
    show_welcome_message()
    
    # Installeer vereisten
    install_requirements()
    
    # Zet configuratie op
    setup_configuration()
    
    print("\nInstallatie voltooid! Je kunt nu het project gebruiken.")

if __name__ == "__main__":
    main()
