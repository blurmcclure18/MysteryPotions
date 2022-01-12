def searchPotion(self,obj):
    
        screen1 = MDScreen()

        close_btn=MDFillRoundFlatButton(
            text='Close',
            on_release=self.close_dialog,
            )
        
        roll = int(self.rollInput.text)
        
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
        rolledPotionDescription = potions[num]['PotionDescription'] 
        
        try:
            potionOptions = len(potions[num]['Options'])
            
            if potionOptions > 0:
                rolledPotionOptions = potions[num]['Options']
                self.rollInput = Builder.load_string(roll_input)
                screen1.add_widget(roll_input)
                optionsRoll = randint(1,len(rolledPotionOptions))
                rolledPotionName = f"{rolledPotionOptions[optionsRoll]}"
                optionsRoll_btn = MDFillRoundFlatButton(
                    text='Get Potion',
                )
                self.dialog = MDDialog(
                    text=f"{rolledPotionDescription}",
                    title=f"{rolledPotionName}",
                    size_hint=(0.7,1),
                    buttons=[close_btn,optionsRoll],
                    )
            else:
                pass
        except:
            self.dialog = MDDialog(
                text=f"{rolledPotionDescription}",
                title=f"{rolledPotionName}",
                size_hint=(0.7,1),
                buttons=[close_btn],
            )
        self.dialog.open()

        return screen1
    
def rollPotion(self,obj):
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
            rolledPotionDescription = potions[num]['PotionDescription'] 
            try:
                potionOptions = len(potions[num]['Options'])
                if potionOptions > 0:
                    rolledPotionOptions = potions[num]['Options']
                    optionsRoll = randint(1,len(rolledPotionOptions))
                    rolledPotionName = f"{rolledPotionOptions[optionsRoll]}"
                else:
                    pass
            except:
                pass   
            
            close_btn=MDFillRoundFlatButton(
            text='Close',
            on_release=self.close_dialog,
            )
        
            self.dialog = MDDialog(
                text=f"{rolledPotionDescription}",
                title=f"{rolledPotionName}",
                size_hint=(0.7,1),
                buttons=[close_btn],
            )
            
            self.dialog.open()
        except:
            pass

def close_dialog(self,obj):
        self.dialog.dismiss()
