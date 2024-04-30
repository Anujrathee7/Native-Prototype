from kivy.uix.bubble import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.filechooser import FileChooser
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton

class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"

        Window.size = (350,600)
        return Builder.load_string(
            '''
BoxLayout:
    orientation: 'vertical'

    MDBottomNavigation:
        selected_color_background: "purple"
        text_color_active: "purple"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Schedule'
            icon: 'calendar-clock'

            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'top': 1}  # Align to the top
                padding: [0, dp(30), dp(10), 0]  # Add padding to the top
                spacing: dp(30)  # Add spacing between children

                MDLabel:
                    text: 'March 1'
                    halign: 'center'
                    bold: 'true'
                    font_style: 'H5'  # Change the font style
                
                BoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: dp(10)

                    Image:
                        size_hint: None, None
                        size: 60, 60
                        source: "conifer.png"
                    MDLabel:
                        text: 'Programming Lecture       10-12'
                        bold: 'true'
                        font_style: 'Subtitle1'
                
                BoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: dp(10)

                    Image:
                        size_hint: None, None
                        size: 60, 60
                        source: "knight.png"
                    MDLabel:
                        text: 'Part-time Job      12-17'
                        bold: 'true'
                        font_style: 'Subtitle1'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Add Event'
            icon: 'calendar-plus'

            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'top': 1}  # Align to the top
                padding: [dp(10), dp(40), dp(10), 0]  # Add padding to the left, top, right, and bottom
                spacing: dp(35)  # Add spacing between children

                MDTextField:
                    hint_text: "Event Name"
                    mode: "rectangle"
                    size_hint_x: None  # Disable automatic width adjustment
                    hint_text_color: [0, 0, 0, 0.2] 
                    width: dp(290)
                    padding_x: dp(16)
                    mode: "fill"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color
                        Line:
                            width: 1
                            points: self.x, self.y, self.x + self.width, self.y


                MDTextField:
                    hint_text: "Event Date"
                    mode: "rectangle"
                    size_hint_x: None  # Disable automatic width adjustment
                    hint_text_color: [0, 0, 0, 0.2] 
                    width: dp(240)
                    padding_x: dp(16)
                    mode: "fill"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color
                        Line:
                            width: 1
                            points: self.x, self.y, self.x + self.width, self.y

                MDTextField:
                    hint_text: "Event Type"
                    mode: "rectangle"
                    size_hint_x: None  # Disable automatic width adjustment
                    width: dp(240)
                    hint_text_color: [0, 0, 0, 0.2]  # Set hint text color with lower alpha value

                    padding_x: dp(16)
                    mode: "fill"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color
                        Line:
                            width: 1
                            points: self.x, self.y, self.x + self.width, self.y

                MDTextField:
                    hint_text: "Notes (Not Mandatory)"
                    mode: "rectangle"
                    size_hint_x: None  # Disable automatic width adjustment
                    hint_text_color: [0, 0, 0, 0.0] 
                    width: dp(290)
                    padding_x: dp(16)
                    mode: "fill"
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color
                        Line:
                            width: 1
                            points: self.x, self.y, self.x + self.width, self.y
                       
            MDRaisedButton:
                text: "Submit"
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x":0.5,"center_y": 0.21}
                                


        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Profile'
            icon: 'calendar-account'

            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: "280dp", "380dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                md_bg_color: app.theme_cls.bg_darkest  # Use the darkest background color from the theme
                ripple_behavior: False
                elevation: 6

                MDIconButton:
                    icon: "dots-vertical"
                    pos_hint: {'right': 1, 'bottom': 1}
                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(20)  # Add spacing between children
                    padding: [0, dp(50), dp(10), 0]  # Add padding to the top


                    MDLabel:
                        text: 'Aayush Pandey (Student)'
                        font_style: 'H6'
                        size_hint_y: None
                        height: self.texture_size[1]
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .4}

                    Image:
                        source: 'profile.png'
                        size_hint: None, None
                        size: "120dp", "120dp"
                        pos_hint: {"center_x": .5, "center_y": .65}
                        allow_stretch: True

                    MDLabel:
                        text: 'Schedule Calender (School and other Activities)'
                        size_hint_y: None
                        font_style: 'Subtitle2'
                        height: self.texture_size[1]
                        halign: 'left'
                        padding_x: dp(16)
                        pos_hint: {"center_x": .5, "center_y": .4}
                    
                    MDLabel:
                        text: 'I am using this to maintain my schedule for my school events and part-time job.'
                        font_style: 'Body2'
                        size_hint_y: None
                        height: self.texture_size[1]
                        halign: 'left'
                        padding_x: dp(16)
                        pos_hint: {"center_x": .5, "center_y": .4}
                    
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        spacing: dp(10)
                        padding_x: dp(100)


                        MDIconButton:
                            icon: "disable.png"
                            theme_text_color: "Custom"
                            text_color: "purple"
                        
                        MDIconButton:
                            icon: "edit.png"
                            theme_text_color: "Custom"
                            text_color: "purple"
                            

'''
        )

Test().run()
