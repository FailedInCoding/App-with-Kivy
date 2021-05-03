#imports
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pygame

#How many grids and Names for in the grids
class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1
		
		self.inside = GridLayout()
		self.inside.cols = 2
		
		self.inside.add_widget(Label(text="First Name: ", font_size= 20))
		self.name = TextInput(multiline=False)
		self.inside.add_widget(self.name)
		
		self.inside.add_widget(Label(text="Last Name: ", font_size= 20))
		self.name = TextInput(multiline=False)
		self.inside.add_widget(self.name)
		
		self.inside.add_widget(Label(text="Emailadress: ", font_size= 20))
		self.email = TextInput(multiline=False)
		self.inside.add_widget(self.email)
		
		self.add_widget(self.inside)
		
		self.submit = Button(text="Submit ", font_size=50)
		self.submit.bind(on_press=self.pressed())
		self.add_widget(self.submit)
		
def pressed(self, instance):
	print("Pressed")
		

#Normal grid that defines how it looks      
class MyApp (App):
	def build(self):
		return MyGrid()

	
if __name__ == "__main__":
	MyApp() .run()