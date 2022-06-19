
#Characters
import customtkinter
import tkinter.messagebox
import tkinter
import random
apexCharacters =["Ash", "Bangalore", "Bloodhound", "Caustic", "Crypto", "Fuse", "Gibraltar", "Horizon", "Lifeline", "Loba", "Mad Maggie", "Mirage", "Newcastle", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer", "Valkyrie", "Wattson", "Wraith"]
#weapons
apexWeapons =["Havoc Rifle", "VK-47 Flatline", "Hemlok Burst AR", "R-301 Carbine", "Alternator SMG", "Prowler-Burst PDW", "R-99 SMG", "Volt SMG", "C.A.R SMG", "Devotion LMG", "L-STAR EMG", "M600 Spitfire","Rampage LMG", "G7 Scout", "Triple Take", "30-30 Repeater", "Boceck Compund Bow",
              "Charge Rifle", "Longbow DMR", "Kraber", "Sentinel", "EVA-8 Auto", "Mastiff", "Mozambique", "Peacekeeper", "RE-45 Auto", "P2020", "Wingman"]


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x580")
app.title("Apex Legends Randomizer")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Apex Legends Randomizer", justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)
           
#Function called randomzie that will put a random character and weapon into the labels
def randomize(self):
    #Randomize the character
    self.label_legend.config(text=apexCharacters[random.randint(0, len(apexCharacters) - 1)])
    #Randomize the weapon
    self.label_weapon.config(text=apexWeapons[random.randint(0, len(apexWeapons) - 1)])

def change_appearance_mode(self, new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

def on_closing(self, event=0):
    self.destroy()


app.mainloop()

