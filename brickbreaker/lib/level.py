import pygame
import random
import block
import main


class Level(object):
	def __init__(self, level_number, block_number):
		self.level_number = level_number
		self.block_number = block_number
		self.blocks_hit_list = []
		## create lists
		global block_list
		block_list = pygame.sprite.Group()
		
		global all_sprites_list
		all_sprites_list = pygame.sprite.Group()
		
		self.win = False
		self.start = True

		

		
	def create_sprites(self):	
		
		file_key = self.level_number

		if self.start or self.win:
			## create blocks
			for i in range(self.block_number):
				newblock = block.Image("data/brick.png", main.screen_w/13, main.screen_h/45) ## adjust for size
			
				## in random location
				newblock.rect.x = random.randint(4, main.screen_w-4)
				newblock.rect.y = random.randint(4, main.screen_h/4)
			
				## add the block to the lists
				block_list.add(newblock)
				all_sprites_list.add(newblock)
				
				self.win = False
				self.start = False
		
	
	def next_level(self):
		if len(block_list) == 0:
			self.win = True
			
			self.level_number +=1 
			self.block_number += 20
			main.speedx += main.screen_w * .0001
			main.speedy += main.screen_h * .0001
			main.number_of_lives += 1
			main.win.play()
		else:
			self.win = False

	def create_border(self):
		
		## Crate border
		global border_list
		border_list = pygame.sprite.Group()

		left_wall = block.Block((255,255,255), 3, main.screen_h +2)
		all_sprites_list.add(left_wall)
		border_list.add(left_wall)
		left_wall.rect.x = -1
		left_wall.rect.y = -1
		self.left_wall=left_wall

		right_wall = block.Block((255,255,255), 3, main.screen_h +2)
		all_sprites_list.add(right_wall)
		border_list.add(right_wall)
		right_wall.rect.x = main.screen_w-2
		right_wall.rect.y = -1
		self.right_wall=right_wall

		top_wall = block.Block((255,255,255), main.screen_w + 2, 3)
		all_sprites_list.add(top_wall)
		border_list.add(top_wall)
		top_wall.rect.x = -1
		top_wall.rect.y = -1
		self.top_wall=top_wall
		
		
		paddle = block.Block((255,255,255), main.screen_w/6, 3)
		all_sprites_list.add(paddle)
		border_list.add(paddle)
		paddle.rect.x = -1
		paddle.rect.y = main.screen_h * .75
		self.paddle=paddle
		
		bottom_wall = block.Block((255,255,255), main.screen_w, 3)
		all_sprites_list.add(bottom_wall)
		bottom_wall.rect.x = -1
		bottom_wall.rect.y = main.screen_h -2
		self.bottom_wall=bottom_wall
		
		
	def check_collision(self):
		
		blocks_hit_list = pygame.sprite.spritecollide(main.ball, block_list, True)
		if len(blocks_hit_list) > len(self.blocks_hit_list):
			main.blip.play()
			main.dy = -main.dy
		self.blocks_hit_list = blocks_hit_list
		self.bounce_list = pygame.sprite.spritecollide(main.ball, border_list, False)
		
	
			
		## keep blocks off border
		pygame.sprite.groupcollide(block_list, border_list, True, False)
			
		if self.left_wall in self.bounce_list:
			main.dx = main.dt * main.speedx
			
		if self.right_wall in self.bounce_list:
			main.dx = -main.dt * main.speedx
			
		if self.top_wall in self.bounce_list:
			main.dy = main.dt * main.speedy
			
		if self.paddle in self.bounce_list:
			main.dy = -main.dt * main.speedy
			main.blip.play()
	
	def restart(self):
		
		## restart
		mouse = pygame.mouse.get_pos()
		dot = block.Block((0,0,0), 5, 5)
		dot.rect.x = mouse[0]
		dot.rect.y = mouse[1]
		mouse_pos = pygame.sprite.Group()
		mouse_pos.add(dot)
		mouse_pos.draw(main.screen)
		
		restart = block.Block((0,0,0), .25 * main.screen_w, .06 * main.screen_h)
		restart_font = main.font.render('restart', True, (0,255,0))
		restart.image.blit(restart_font, (0,0))
		restart.rect.x = .35 * main.screen_w
		restart.rect.y = .65 * main.screen_h
		main.screen.blit(restart.image, (restart.rect.x, restart.rect.y))
		loop=False
		if pygame.sprite.spritecollide(restart, mouse_pos, True) and loop == False:
			
			## ball
			main.speedx = .000375 * main.screen_w
			main.speedy = .000375 * main.screen_h
			main.dt = 0 
			main.dy=0
			main.dx=0
			main.ball.rect.x = 0
			main.ball.rect.y = 0
		
			## level number 
			self.level_number = 1
			self.block_number = 20
			self.start = True
			main.number_of_lives = 3
			
			loop = True
start=Level(1,20)