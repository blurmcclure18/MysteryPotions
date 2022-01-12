roll_input = """
MDTextField:
    hint_text: "Enter Roll"
    helper_text: "Enter the d100 roll of your player"
    helper_text_mode:"on_focus"
    required: True
    max_text_length: 3
    icon_right: "dice-d20"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x':0.5, 'center_y':0.7}
    size_hint_x:None
    width:300
"""

title_Header= """
MDLabel:
    text: "Mystery Potion Finder"
    halign: 'center'
    pos_hint: {'center_y':0.9}
    font_style: 'H1'
    theme_text_color: "Custom"
    text_color: 243, 160, 81, 1
"""

screen_helper = """
ScreenManager:
    MenuScreen:
    PotionScreen:
<MenuScreen>:
    name: 'MysteryPotion'

    MDLabel:
        text: "Mystery Potion Finder"
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H1'
        theme_text_color: "Custom"
        text_color: 243, 160, 81, 1
    
    MDTextField:
        hint_text: "Enter Roll"
        helper_text: "Enter the d100 roll of your player"
        helper_text_mode:"on_focus"
        required: True
        max_text_length: 3
        icon_right: "dice-d20"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        size_hint_x:None
        width:300
    
    MDFillRoundFlatButton:
        text:'Search'
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        on_release: searchPotion

    MDFillRoundFlatButton:
        text: 'Roll'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'Potion'
    
<PotionScreen>:
    name: 'Potion'
    MDLabel:
        text: 'Potion'
        halign: 'center'
    
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'        
"""