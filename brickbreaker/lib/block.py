import pygame
import main
pictures = {
	'1' : "data/brick.png"
		}

class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		self.color = color
		self.width = width
		self.height = height
		
		pygame.sprite.Sprite.__init__(self)
		
		## create block image
		self.image=pygame.Surface([width, height])
		self.image.fill(color)
		
		self.rect = self.image.get_rect()
		

class Image(pygame.sprite.Sprite):
	def __init__(self, file_name, width, height):
		
		pygame.sprite.Sprite.__init__(self)
		
		## create block image
		
	
		self.image=pygame.image.load(file_name)
		self.image.convert_alpha()
		self.image=pygame.transform.scale(self.image, (width,height))
		
		
		self.rect = self.image.get_rect()
		