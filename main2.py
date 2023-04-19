import time
import cv2
from kivy.uix.camera import Camera
from kivy.graphics.texture import Texture
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.core.window import Window

Window.size = (300, 600)

class IntroApp(App):
    def build(self):
        # Create a label with the app name
        label = Label(text='My Kivy App', font_size=50, color=[1, 1, 1, 0])

        # Create an animation to fade in the label
        anim = Animation(color=[1, 1, 1, 1], duration=2)

        # Start the animation and bind it to a callback function
        anim.bind(on_complete=self.switch_to_home)
        anim.start(label)

        # Return the label as the root widget
        return label

    def switch_to_camera_app(self, *args):
        # Create an instance of CameraApp
        camera_app = CameraApp()

        # Switch to the CameraApp window
        self.stop()
        camera_app.run()

    def switch_to_home(self, *args):
        # Create an instance of CameraApp
        home = Homescreen()

        # Switch to the CameraApp window
        self.stop()
        home.run()


class CameraApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.camera = Camera(resolution=(640, 480), play=False)
        self.camera.texture = Texture.create(size=self.camera.resolution)
        self.camera.texture_size = self.camera.texture.size
        self.camera.opacity = 1.0
        self.camera.play = True
        return self.camera

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            self.camera.texture.blit_buffer(frame.tobytes(), colorfmt='bgr')

    def on_stop(self):
        self.capture.release()

class Homescreen(App):
    def build(self):
        return self.build_screen()

    def build_screen(self):
        # Create a box layout with vertical orientation
        layout = BoxLayout(orientation='vertical')
        # Create two button widgets
        button1 = Button(text='Button 1', size_hint=(0.5, 0.2), size=(20, 50))
        button2 = Button(text='Button 2', size_hint=(0.5, 0.2), size=(2, 50))

        # Add the buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)

        # Return the layout as the root widget
        return layout



if __name__ == '__main__':
    # Start the IntroApp and wait for 2 seconds before switching to the CameraApp
    intro_app = IntroApp()
    #intro_app.run()
    time.sleep(2)
    Homescreen().run()
