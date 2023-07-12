# import required modules

from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.icon_definitions import md_icons
import datetime

# window.size = (1920, 1080)
class Clock_app_by_PMApp(MDApp):
    
    
    def build(self):
        screen = Screen()
        tt=datetime.datetime.now()
        bottom = MDFlatButton(text="Don't Wast your Time.", 
                      pos_hint={'center_x': 0.5,'center_y': 0.45})
        
        clock = MDFlatButton(text=tt.strftime("%c"), 
                      pos_hint={'center_x': 0.5,'center_y': 0.5})
        
        heading = MDFlatButton(text='T.I.M.E.', font_size= 100,
                      pos_hint={'center_x': 0.5,'center_y': 0.6}) 
        
        
        screen.add_widget(bottom)
        screen.add_widget(clock)
        screen.add_widget(heading)
        return screen

	
# run application
Clock_app_by_PMApp().run()
