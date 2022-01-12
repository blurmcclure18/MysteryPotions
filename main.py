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
            root.getOption()
        on_release:
            root.manager.current = 'potion'
    
    MDFillRoundFlatButton:
        id: rollBtn
        text: 'Roll'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press:
            root.optionRoll()
        on_release:
            root.manager.current = 'potion'
    
    MDFillRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.clearText()
"""
class HomeScreen(Screen):

    def searchPotion(self):
        try:
            potionScreen = self.manager.get_screen('potion')
            homeScreen = self.manager.get_screen('home')

            roll = int(homeScreen.ids.rollInput.text)

            global num

            if roll > 1 and roll <= 50:
                num = 0
            elif roll > 50 and roll <= 55:
                num = 1
            elif roll > 55 and roll <= 60:
                num = 2
            elif roll > 60 and roll <= 65:
                num = 3
            elif roll > 65 and roll <=70:
                num = 4
            elif roll > 70 and roll <= 75:
                num = 5
            elif roll > 75 and roll <= 80:
                num = 6
            elif roll > 80 and roll <= 85:
                num = 7
            elif roll > 85 and roll <= 90:
                num = 8
            elif roll > 90 and roll <= 95:
                num = 9
            elif roll > 95 and roll <= 100:
                num = 10

            rolledPotionName = potions[num]['PotionName']
            potionScreen.ids.potionName.text = rolledPotionName
            rolledPotionDescription = potions[num]['PotionDescription']
            potionScreen.ids.potionDescription.text = rolledPotionDescription

            global potionOptions

            try:
                potionOptions = len(potions[num]['Options'])
                self.manager.get_screen('option').ids.optionName.text = f"Roll A d{potionOptions}"

                if potionOptions > 0:
                    MDApp.get_running_app().root.current = "option"
                else:
                    pass
            except:
                MDApp.get_running_app().root.current = "potion"
        except:
            pass

    def rollPotion(self):
        potionScreen = self.manager.get_screen('potion')
        try:
            roll = randint(1,100)

            if roll > 1 and roll <= 50:
                num = 0
            elif roll > 50 and roll <= 55:
                num = 1
            elif roll > 55 and roll <= 60:
                num = 2
            elif roll > 60 and roll <= 65:
                num = 3
            elif roll > 65 and roll <=70:
                num = 4
            elif roll > 70 and roll <= 75:
                num = 5
            elif roll > 75 and roll <= 80:
                num = 6
            elif roll > 80 and roll <= 85:
                num = 7
            elif roll > 85 and roll <= 90:
                num = 8
            elif roll > 90 and roll <= 95:
                num = 9
            elif roll > 95 and roll <= 100:
                num = 10

            rolledPotionName = potions[num]['PotionName']
            potionScreen.ids.potionName.text = rolledPotionName
            rolledPotionDescription = potions[num]['PotionDescription']
            potionScreen.ids.potionDescription.text = rolledPotionDescription

            try:
                potionOptions = len(potions[num]['Options'])
                
                if potionOptions > 0:
                    self.manager.get_screen('option').ids.optionName.text = f"Roll A d{potionOptions}"
                    MDApp.get_running_app().root.current = "option"
                else:
                    pass
            except:
                MDApp.get_running_app().root.current = "potion"
        except:
            pass

class PotionScreen(Screen):
    def clearText(self):
        homeScreen = self.manager.get_screen('home')
        optionScreen = self.manager.get_screen('option')

        homeScreen.ids.rollInput.text = ''
        optionScreen.ids.optionInput.text = ''

        MDApp.get_running_app().root.current = 'home'

class OptionScreen(Screen):
    def getOption(self):
        potionScreen = self.manager.get_screen('potion')
        rolledPotionOptions = potions[num]['Options']
        optionsRoll = int(self.manager.get_screen('option').ids.optionInput.text)
        rolledPotionName = f"{rolledPotionOptions[optionsRoll]}"
        potionScreen.ids.potionName.text = rolledPotionName
    
    def optionRoll(self):
        try:
            global potionOptions
            print(potionOptions)
            roll = randint(1, potionOptions)

            potionScreen = self.manager.get_screen('potion')
            rolledPotionOptions = potions[num]['Options']
            optionsRoll = roll
            rolledPotionName = f"{rolledPotionOptions[optionsRoll]}"
            potionScreen.ids.potionName.text = rolledPotionName
        except:
            pass
    def clearText(self):
        homeScreen = self.manager.get_screen('home')
        optionScreen = self.manager.get_screen('option')

        homeScreen.ids.rollInput.text = ''
        optionScreen.ids.optionInput.text = ''

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