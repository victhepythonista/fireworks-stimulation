import pygame
from backend import *


pygame.init()

bg = pygame.image.load("nightsky.jpeg")
class FireworksScreen(Screen):
	def __init__(self):
		Screen.__init__(self,(900,500))
		self.fw_manager = FireworksManager()

	def display_widgets(self):
		self.window.blit(bg, (0,0))
		self.fw_manager.show(self.window)
		pass


FireworksScreen().show()
