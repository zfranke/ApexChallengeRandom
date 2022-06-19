
#Characters
import customtkinter
import tkinter.messagebox
import tkinter
import random
apexCharacters =["Ash", "Bangalore", "Bloodhound", "Caustic", "Crypto", "Fuse", "Gibraltar", "Horizon", "Lifeline", "Loba", "Mad Maggie", "Mirage", "Newcastle", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer", "Valkyrie", "Wattson", "Wraith"]
#weapons
apexWeapons =["Havoc Rifle", "VK-47 Flatline", "Hemlok Burst AR", "R-301 Carbine", "Alternator SMG", "Prowler-Burst PDW", "R-99 SMG", "Volt SMG", "C.A.R SMG", "Devotion LMG", "L-STAR EMG", "M600 Spitfire","Rampage LMG", "G7 Scout", "Triple Take", "30-30 Repeater", "Boceck Compund Bow",
              "Charge Rifle", "Longbow DMR", "Kraber", "Sentinel", "EVA-8 Auto", "Mastiff", "Mozambique", "Peacekeeper", "RE-45 Auto", "P2020", "Wingman"]


def randomize():
    #Randomize the character
    label_Legend.config(
        text=apexCharacters[random.randint(0, len(apexCharacters) - 1)])
    #Randomize the weapon
    label_Weapon.config(
        text=apexWeapons[random.randint(0, len(apexWeapons) - 1)])

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("200x500")
app.title("Apex Legends Randomizer")


frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Apex Legends Randomizer", text_font=("Roboto Medium", -16), justify = tkinter.LEFT)
label.pack(pady=12, padx=10)

label_Legend = customtkinter.CTkLabel(master=frame, text="Legend", text_font=(
    "Roboto Medium", -12), justify=tkinter.LEFT)
label_Legend.pack(pady=12, padx=10)

label_Weapon = customtkinter.CTkLabel(master=frame, text="Weapon", text_font=(
    "Roboto Medium", -12), justify=tkinter.LEFT)
label_Weapon.pack(pady=12, padx=10)
           
button = customtkinter.CTkButton(
    master=frame, text="Randomize", command=randomize)
button.pack(pady=12, padx=10)
           

app.mainloop()

