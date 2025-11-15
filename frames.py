import customtkinter as ctk
import fileHandler
import AppData.GlobalVars as GV

class BossDataFrame():
    # Frame for displaying boss data based on selected expedition
    def __init__(self, app, expeditions):
        
        self.secondBossToggle = False
        self.app = app
        self.padx = 5
        self.pady = 5

        self.expeditions = expeditions
        self.labelFont = ctk.CTkFont(family=GV.FONT_FAMILY, size=GV.FONT_SIZE)

        # Labels for displaying boss information
        self.bossNameLabel = ctk.CTkLabel(self.app, text="Boss: ", font=self.labelFont, anchor="w")
        self.strongAgainstLabel = ctk.CTkLabel(self.app, text="Stronger VS: ", font=self.labelFont, anchor="w")
        self.weakAgainstLabel = ctk.CTkLabel(self.app, text="Weak to: ", font=self.labelFont, anchor="w")
        self.resistancesLabel = ctk.CTkLabel(self.app, text="Resistances: ", font=self.labelFont, anchor="w")
        self.negationsLabel = ctk.CTkLabel(self.app, text="Negations: ", font=self.labelFont, anchor="w")
        self.damageLabel = ctk.CTkLabel(self.app, text="Damage: ", font=self.labelFont, anchor="w")
        self.inflictsLabel = ctk.CTkLabel(self.app, text="Inflicts: ", font=self.labelFont, anchor="w")
        self.stanceLabel = ctk.CTkLabel(self.app, text="Stance: ", font=self.labelFont, anchor="w")   
		
        # Place all widgets in the frame
        self.bossNameLabel.place(x=20 , y=75)
        self.strongAgainstLabel.place(x=20, y=125)
        self.weakAgainstLabel.place(x=260, y=125)
        self.resistancesLabel.place(x=260, y=195)
        self.negationsLabel.place(x=20, y=175)
        self.damageLabel.place(x=320, y=400)
        self.inflictsLabel.place(x=150, y=400)
        self.stanceLabel.place(x=20, y=400)

    # Dropdown menu calback for selecting expeditions
    def optionMenu_callback(self, choice):
        
        if choice == "Choose Expedition":
            bossDataDict = GV.BOSS_DATA_DICT.copy()
            self.secondBossToggle = False
            try:
                self.bossNameLabelTwo.destroy()
                self.strongAgainstLabelTwo.destroy()
                self.weakAgainstLabelTwo.destroy()
                self.resistancesLabelTwo.destroy()
                self.negationsLabelTwo.destroy()
                self.damageLabelTwo.destroy()
                self.inflictsLabelTwo.destroy()
                self.stanceLabelTwo.destroy()
            except AttributeError:
                pass
        else:
            bossDataDict = fileHandler.parseJson(choice)
            if len(bossDataDict) == 2:
                self.sentientPestSecondBoss(bossDataDict)
                self.secondBossToggle = True
            else:
                self.secondBossToggle = False
                try:
                    self.bossNameLabelTwo.destroy()
                    self.strongAgainstLabelTwo.destroy()
                    self.weakAgainstLabelTwo.destroy()
                    self.resistancesLabelTwo.destroy()
                    self.negationsLabelTwo.destroy()
                    self.damageLabelTwo.destroy()
                    self.inflictsLabelTwo.destroy()
                    self.stanceLabelTwo.destroy()
                except AttributeError:
                    pass
         

        self.bossNameLabel.configure(text=f"Boss: {bossDataDict[0]['bossName']}")
        self.strongAgainstLabel.configure(text=f"Stronger VS: {bossDataDict[0]['resistant']}")
        self.weakAgainstLabel.configure(text=f"Weak to: {bossDataDict[0]['weak']}")
        self.resistancesLabel.configure(text=f"Resistances: {bossDataDict[0]['resistances']}")
        self.negationsLabel.configure(text=f"Negations: {bossDataDict[0]['negations']}")
        self.damageLabel.configure(text=f"Damage: {bossDataDict[0]['damage']}")
        self.inflictsLabel.configure(text=f"Inflicts: {bossDataDict[0]['inflicts']}")
        self.stanceLabel.configure(text=f"Stance: {bossDataDict[0]['stance']}")
    
    def sentientPestSecondBoss(self, bossDataDict):
        if not self.secondBossToggle:
            #Second boss of Sentient Pest labels
            self.bossNameLabelTwo = ctk.CTkLabel(self.app, text="Boss: ", font=self.labelFont, anchor="w")
            self.strongAgainstLabelTwo = ctk.CTkLabel(self.app, text="Stronger VS: ", font=self.labelFont, anchor="w")
            self.weakAgainstLabelTwo = ctk.CTkLabel(self.app, text="Weak to: ", font=self.labelFont, anchor="w")
            self.resistancesLabelTwo = ctk.CTkLabel(self.app, text="Resistances: ", font=self.labelFont, anchor="w")
            self.negationsLabelTwo = ctk.CTkLabel(self.app, text="Negations: ", font=self.labelFont, anchor="w")
            self.damageLabelTwo = ctk.CTkLabel(self.app, text="Damage: ", font=self.labelFont, anchor="w")
            self.inflictsLabelTwo = ctk.CTkLabel(self.app, text="Inflicts: ", font=self.labelFont, anchor="w")
            self.stanceLabelTwo = ctk.CTkLabel(self.app, text="Stance: ", font=self.labelFont, anchor="w")   

            # Place all second boss widgets in the frame
            self.bossNameLabelTwo.place(x=20 , y=475)
            self.strongAgainstLabelTwo.place(x=20, y=525)
            self.weakAgainstLabelTwo.place(x=260, y=525)
            self.resistancesLabelTwo.place(x=260, y=595)
            self.negationsLabelTwo.place(x=20, y=575)
            self.damageLabelTwo.place(x=320, y=800)
            self.inflictsLabelTwo.place(x=150, y=800)
            self.stanceLabelTwo.place(x=20, y=800)

        # Configure second boss labels with boss data
        self.bossNameLabelTwo.configure(text=f"Boss: {bossDataDict[1]['bossName']}")
        self.strongAgainstLabelTwo.configure(text=f"Stronger VS: {bossDataDict[1]['resistant']}")
        self.weakAgainstLabelTwo.configure(text=f"Weak to: {bossDataDict[1]['weak']}")
        self.resistancesLabelTwo.configure(text=f"Resistances: {bossDataDict[1]['resistances']}")
        self.negationsLabelTwo.configure(text=f"Negations: {bossDataDict[1]['negations']}")
        self.damageLabelTwo.configure(text=f"Damage: {bossDataDict[1]['damage']}")
        self.inflictsLabelTwo.configure(text=f"Inflicts: {bossDataDict[1]['inflicts']}")
        self.stanceLabelTwo.configure(text=f"Stance: {bossDataDict[1]['stance']}")       