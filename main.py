import customtkinter as ctk
import frames, fileHandler 
import AppData.GlobalVars as GV

# Main application class for instantiating the window
class App(ctk.CTk):

    def __init__(self, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # Define window properties
        self.title(GV.TITLE)
        self.geometry(GV.RESOLUTION)
        self._set_appearance_mode(GV.THEME)
        self.resizable(width=False, height=False)
        self.optionMenuFont = ctk.CTkFont(family=GV.FONT_FAMILY, size=24)

        # Load expeditions and create the main frame
        self.expeditions = fileHandler.loadExpeditions()
        self.bossDataFrame = frames.BossDataFrame(self, self.expeditions)
        self.optionMenu = ctk.CTkOptionMenu(self, values=self.expeditions, command=self.bossDataFrame.optionMenu_callback, font=self.optionMenuFont)
        self.optionMenu.set("Choose Expedition")
        self.optionMenu.place(x=20, y=20)


# Main entry point
if __name__ == "__main__":
    app = App()
    app.mainloop()
