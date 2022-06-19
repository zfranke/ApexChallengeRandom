
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


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Apex Legends")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # create a frame
        self.frame = customtkinter.CTkFrame(master=self, corner_radius=10, background="black")
        
        #Create the header
        self.label_header = customtkinter.CTkLabel(master=self.frame,
                                              text="Apex Legends: Challenge Selector",
                                              text_font=("Roboto Medium", -24))
        
        self.label_legend = customtkinter.CTkLabel(master=self.frame,
                                                text="Legend:",
                                                text_font=("Roboto Medium", -12))
        
        self.label_weapons = customtkinter.CTkLabel(master=self.frame,
                                                    text="Weapon:",
                                                    text_font=("Roboto Medium", -12))
        
        self.button_select = customtkinter.CTkButton(master=self.frame,
                                                     text="Randomize",
                                                     text_font=("Roboto Medium", -12),
                                                     command=self.randomize)
        
        

       
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


if __name__ == "__main__":
    app = App()
    app.mainloop()

