import cv2
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.animation import Animation

def build_intro_screen():
    label = Label(text='My Kivy App', font_size=50, color=[1, 1, 1, 0])

    # Create an animation to fade in the label
    anim = Animation(color=[1, 1, 1, 1], duration=2)

    # Start the animation and bind it to a callback function
    anim.start(label)

    # Return the label as the root widget
    return label

def build_screen():
    # Create a box layout with vertical orientation
    layout = BoxLayout(orientation='vertical')

    # Create two button widgets
    button1 = Button(text='Button 1')
    button2 = Button(text='Button 2')

    # Add the buttons to the layout
    layout.add_widget(button1)
    layout.add_widget(button2)

    # Return the layout as the root widget
    return layout

class MyApp(App):
    def build(self):
        return build_intro_screen()

if __name__ == '__main__':
    MyApp().run()