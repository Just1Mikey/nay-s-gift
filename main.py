import customtkinter as ctk
import frames, fileHandler, threading, time
import AppData.GlobalVars as GV


# Main application class for instantiating the window
class App(ctk.CTk):

    def __init__(self, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.runToggle = False
        
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
        self.timerLabel = ctk.CTkLabel(self, text="Run Time: 00:00:00", font=self.optionMenuFont)
        self.timerLabel.place(x=700, y=60)
        self.timeStartButton = ctk.CTkButton(self, text="Start Run", font=self.optionMenuFont, command=self.startTimer)
        self.timeStartButton.place(x=700, y=20)
        self.phaseLabel = ctk.CTkLabel(self, text="Phase: N/A", font=self.optionMenuFont)
        self.phaseLabel.place(x=700, y=120)

    def startTimer(self):
        # Timer function to update the run time every second
        if self.runToggle:
            self.runToggle = False
            self.timeStartButton.configure(text="Start Run")
        else:
            self.runToggle = True
            self.startTime = time.time()
            self.updateTimer()
            self.timeStartButton.configure(text="Stop Run")
            

    def updateTimer(self):
        if self.runToggle:    
            elapsedTime = int(time.time() - self.startTime)
            h, r = divmod(elapsedTime, 3600)
            m, s = divmod(r, 60)
            self.timerLabel.configure(text=f"Run Time: {h:02}:{m:02}:{s:02}")

            match elapsedTime:
                case x if x < 270:  # 4.5m
                    m,s = divmod((270 - elapsedTime), 60)
                    phase = f"Free roam - prepare for Circle 1 closing in: {m:02}:{s:02}"
                case x if x < 450:  # 7.5m
                    m,s = divmod((450 - elapsedTime), 60)
                    phase = f"Circle 1 closes in: {m:02}:{s:02}"
                case x if x < 660:  # 11m
                    m,s = divmod((660 - elapsedTime), 60)
                    phase = f"Circle 1 closed - prepare for Circle 2 closing in: {m:02}:{s:02}"
                case x if x < 840:  # 14m
                    m,s = divmod((840 - elapsedTime), 60)
                    phase = f"Circle 2 closes in: {m:02}:{s:02}"
                case _:
                    phase = "Night Boss! After Defeating - Reset Timer!"

            self.phaseLabel.configure(text=f"Phase: {phase}")
            # Schedule the next update after 1 second
            self.after(1000, self.updateTimer)
        


# Main entry point
if __name__ == "__main__":
    app = App()
    app.mainloop()
