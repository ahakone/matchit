import pygame, os, sys
from pygame.locals import *


class Card(pygame.sprite.Sprite):
	def load_image(self, image_name):
		try:
			image = pygame.image.load(image_name)
		except pygame.error, message:
			print "Cannot load image: " + image_name
			raise SystemExit, message
		return image.convert_alpha()

	def __init__(self, screen, x, y, image_name):
		pygame.sprite.Sprite.__init__(self)
		#self.active = True
		self.image_name = image_name
		self.front = self.load_image(image_name)
		self.image_w, self.image_h = self.front.get_size()
		self.image_w /= 7
		self.image_h /= 7 #scale factor
		self.front = pygame.transform.scale(self.front, (self.image_w, self.image_h))

		self.back = self.load_image('Card back.gif') # change to load back
		self.back = pygame.transform.scale(self.back, (self.image_w, self.image_h))

		self.image = self.back
		self.side = 0
		self.screen = screen
		self.x = x
		self.y = y
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def draw(self):
		self.screen.blit(self.image, (self.rect.x, self.rect.y))
		

	def flip(self):
		self.side = (self.side + 1) % 2
		if (self.side == 0):
			self.image = self.back
		else:
			self.image = self.front
		
	def back(self):
		self.image = self.back