from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder

from random import randint
from potionsDict import potions
from helpers import roll_input,title_Header
 
class MyApp(MDApp):
    
    def build(self):
        screen = MDScreen()
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.primary_hue='200'
        self.theme_cls.theme_style="Dark"
        #UI Widgets go here
        self.rollInput = Builder.load_string(roll_input)
        self.titleHeader = Builder.load_string(title_Header)
        #self.searchBtn = Builder.load_string(search_btn)
        
        #UI Widgets go here
        
        search_btn = MDFillRoundFlatButton(
            text='Search',
            pos_hint={'center_x':0.5, 'center_y':0.6},
            on_release=self.searchPotion
            )
        
        roll_btn = MDFillRoundFlatButton(
            text='Roll',
            pos_hint={'center_x':0.5, 'center_y':0.5},
            on_release=self.rollPotion
            )
        
        screen.add_widget(self.titleHeader)
        screen.add_widget(self.rollInput)
        screen.add_widget(search_btn)
        screen.add_widget(roll_btn)    
        
        return screen
    
    def searchPotion(self,obj):
        try:
            num = int(self.rollInput.text)
            rolledPotionName = potions[num]['PotionName']
            rolledPotionDescription = potions[num]['PotionDescription'] 
            try:
                potionOptions = len(potions[num]['Options'])
                if potionOptions > 0:
                    rolledPotionOptions = potions[num]['Options']
                    optionsRoll = randint(1,len(rolledPotionOptions))
                else:
                    pass
            except:
                pass
            
            print(f"\nYou got a {rolledPotionName}\n")
            print(f"Potion Description: \n\n{rolledPotionDescription}")

            try:
                if potionOptions > 0:
                    print(f"\n{rolledPotionOptions[optionsRoll]}")
                else:
                    pass
            except:
                pass
            
            close_btn=MDFillRoundFlatButton(
            text='Close',
            on_release=self.close_dialog,
            )
        
            self.dialog = MDDialog(
                text=f"{rolledPotionName}",
                title='Mystery Potion',
                size_hint=(0.7,1),
                buttons=[close_btn],
            )
            self.dialog.open()
        except:
            pass
    
    def rollPotion(self,obj):
        try:
            num = randint(1,20)
            rolledPotionName = potions[num]['PotionName']
            rolledPotionDescription = potions[num]['PotionDescription'] 
            try:
                potionOptions = len(potions[num]['Options'])
                if potionOptions > 0:
                    rolledPotionOptions = potions[num]['Options']
                    optionsRoll = randint(1,len(rolledPotionOptions))
                else:
                    pass
            except:
                pass
            
            print(f"\nYou got a {rolledPotionName}\n")
            print(f"Potion Description: \n\n{rolledPotionDescription}")

            try:
                if potionOptions > 0:
                    print(f"\n{rolledPotionOptions[optionsRoll]}")
                else:
                    pass
            except:
                pass
        except:
            pass

        def close_dialog(self,obj):
            self.dialog.dismiss()
if __name__ == '__main__':
    MyApp().run()