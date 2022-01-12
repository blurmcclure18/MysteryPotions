from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from potionsdict import potions
from random import randint

__version__ = 1.0

screen_helper = """
ScreenManager:
    HomeScreen:
    PotionScreen:
    OptionScreen:

<HomeScreen>:
    name: 'home'
    
    MDTextField:
        id: rollInput
        hint_text: "Enter Roll"
        helper_text: "Enter the d100 roll of your player"
        helper_text_mode:"on_focus"
        icon_right: "dice-d20"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x':0.5, 'center_y':0.6}
        size_hint_x:None
        width:300
    
    MDLabel:
        text: "Mystery Potion Finder"
        halign: 'center'
        pos_hint: {'center_y':0.8}
        font_style: 'H2'
        theme_text_color: "Custom"
        text_color: 243, 160, 81, 1
    
    MDFillRoundFlatButton:
        text:'Search'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press:
            root.searchPotion()
    
    MDFillRoundFlatButton:
        text: 'Roll'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press:
            root.rollPotion()
    
<PotionScreen>:
    name: 'potion'
    
    MDLabel:
        id: potionName
        text: "Potion"
        multiline: True
        halign: 'center'
        pos_hint: {'center_y':0.8}
        font_style: 'H2'
        theme_text_color: "Custom"
        text_color: 243, 160, 81, 1
    
    MDLabel:
        id: potionDescription
        text: "Description"
        halign: 'center'
        pos_hint: {'center_y':0.5}
        font_style: 'Body1'
        theme_text_color: "Secondary"

    MDFillRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.clearText()

<OptionScreen>:
    name: 'option'
    
    MDLabel:
        id: optionName
        text: "Roll a dNum"
        halign: 'center'
        pos_hint: {'center_y':0.8}
        font_style: 'H2'
        theme_text_color: "Custom"
        text_color: 243, 160, 81, 1
    
    MDTextField:
        id: optionInput
        hint_text: "Enter Roll"
        icon_right: "dice-d20"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x':0.5, 'center_y':0.6}
        size_hint_x:None
        width:300

    MDFillRoundFlatButton:
        id: searchBtn
        text:'Search'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press:
            root.searchOption()
    
    MDFillRoundFlatButton:
        id: rollBtn
        text: 'Roll'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press:
            root.rollOption()
    
    MDFillRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.clearText()
"""
class HomeScreen(Screen):

    global potionsearched
    potionsearched = False

    global potionrolled
    potionrolled = False

    def searchPotion(self):
        try:
            potionScreen = self.manager.get_screen('potion')
            homeScreen = self.manager.get_screen('home')

            roll = int(homeScreen.ids.rollInput.text)

            global searchNum

            if roll > 1 and roll <= 50:
                searchNum = 0
            elif roll > 50 and roll <= 55:
                searchNum = 1
            elif roll > 55 and roll <= 60:
                searchNum = 2
            elif roll > 60 and roll <= 65:
                searchNum = 3
            elif roll > 65 and roll <=70:
                searchNum = 4
            elif roll > 70 and roll <= 75:
                searchNum = 5
            elif roll > 75 and roll <= 80:
                searchNum = 6
            elif roll > 80 and roll <= 85:
                searchNum = 7
            elif roll > 85 and roll <= 90:
                searchNum = 8
            elif roll > 90 and roll <= 95:
                searchNum = 9
            elif roll > 95 and roll <= 100:
                searchNum = 10

            global potionsearched
            
            try:
                global searchPotionOptions
                
                searchPotionOptions = len(potions[searchNum]['Options'])
                self.manager.get_screen('option').ids.optionName.text = f"Roll A d{searchPotionOptions}"

                searchedPotionDescription = potions[searchNum]['PotionDescription']
                potionScreen.ids.potionDescription.text = searchedPotionDescription
                
                potionsearched = True

                MDApp.get_running_app().root.current = "option"

            except:
                searchedPotionName = potions[searchNum]['PotionName']
                potionScreen.ids.potionName.text = searchedPotionName

                searchedPotionDescription = potions[searchNum]['PotionDescription']
                potionScreen.ids.potionDescription.text = searchedPotionDescription
                
                potionsearched = True

                MDApp.get_running_app().root.current = "potion"
        except:
            pass

    def rollPotion(self):
        potionScreen = self.manager.get_screen('potion')
        
        global rollNum
        global potionrolled

        try:
            roll = randint(1,100)

            if roll > 1 and roll <= 50:
                rollNum = 0
            elif roll > 50 and roll <= 55:
                rollNum = 1
            elif roll > 55 and roll <= 60:
                rollNum = 2
            elif roll > 60 and roll <= 65:
                rollNum = 3
            elif roll > 65 and roll <=70:
                rollNum = 4
            elif roll > 70 and roll <= 75:
                rollNum = 5
            elif roll > 75 and roll <= 80:
                rollNum = 6
            elif roll > 80 and roll <= 85:
                rollNum = 7
            elif roll > 85 and roll <= 90:
                rollNum = 8
            elif roll > 90 and roll <= 95:
                rollNum = 9
            elif roll > 95 and roll <= 100:
                rollNum = 10

            try:
                global rolledPotionOptions
                
                rolledPotionOptions = len(potions[rollNum]['Options'])
                self.manager.get_screen('option').ids.optionName.text = f"Roll A d{rolledPotionOptions}"

                rolledPotionDescription = potions[rollNum]['PotionDescription']
                potionScreen.ids.potionDescription.text = rolledPotionDescription
                
                potionrolled = True

                MDApp.get_running_app().root.current = "option"

            except:
                searchedPotionName = potions[rollNum]['PotionName']
                potionScreen.ids.potionName.text = searchedPotionName

                searchedPotionDescription = potions[rollNum]['PotionDescription']
                potionScreen.ids.potionDescription.text = searchedPotionDescription

                potionrolled = True

                MDApp.get_running_app().root.current = "potion"
        except:
            pass

class PotionScreen(Screen):
    def clearText(self):
        homeScreen = self.manager.get_screen('home')
        optionScreen = self.manager.get_screen('option')

        homeScreen.ids.rollInput.text = ''
        optionScreen.ids.optionInput.text = ''

        global potionsearched
        potionsearched = False

        global potionrolled
        potionrolled = False

        MDApp.get_running_app().root.current = 'home'

class OptionScreen(Screen):
    def searchOption(self):
        global potionrolled
        global potionsearched
        try:
            if potionsearched == True:
                print(potionsearched)
                global searchPotionOptions
                global searchNum
                
                roll = int(self.manager.get_screen('option').ids.optionInput.text)

                print(roll)
                
                searchOptions = potions[searchNum]['Options']
                searchedName = f"{searchOptions[roll]}"
                
                potionScreen = self.manager.get_screen('potion')
                potionScreen.ids.potionName.text = searchedName

                MDApp.get_running_app().root.current = 'potion'
            elif potionrolled == True:
                global rolledPotionOptions
                global rollNum

                roll = int(self.manager.get_screen('option').ids.optionInput.text)

                rollOptions = potions[rollNum]['Options']
                rolledName = f"{rollOptions[roll]}"

                potionScreen = self.manager.get_screen('potion')
                potionScreen.ids.potionName.text = rolledName

                MDApp.get_running_app().root.current = 'potion'
        except:
            pass
    
    def rollOption(self):
        global potionsearched
        global potionrolled

        try:
            if potionsearched == True:
                global searchPotionOptions
                global searchNum
                roll = randint(1, searchPotionOptions)
                
                searchOptions = potions[searchNum]['Options']
                searchedName = f"{searchOptions[roll]}"
                
                potionScreen = self.manager.get_screen('potion')
                potionScreen.ids.potionName.text = searchedName

                MDApp.get_running_app().root.current = 'potion'

            elif potionrolled == True:
                global rolledPotionOptions
                global rollNum

                roll = randint(1, rolledPotionOptions)

                rollOptions = potions[rollNum]['Options']
                rolledName = f"{rollOptions[roll]}"

                potionScreen = self.manager.get_screen('potion')
                potionScreen.ids.potionName.text = rolledName

                MDApp.get_running_app().root.current = 'potion'
        except:
            pass
    
    def clearText(self):
        homeScreen = self.manager.get_screen('home')
        optionScreen = self.manager.get_screen('option')

        homeScreen.ids.rollInput.text = ''
        optionScreen.ids.optionInput.text = ''
        
        global potionrolled
        global potionsearched

        potionsearched = False
        potionrolled = False

        MDApp.get_running_app().root.current = 'home'

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(PotionScreen(name='potion'))
sm.add_widget(OptionScreen(name='option'))
class MysteryPotionApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.theme_style = 'Dark'
        return screen

if __name__ == '__main__':
    MysteryPotionApp().run()