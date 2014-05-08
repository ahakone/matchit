import pygame, os, sys, random
from pygame.locals import *
from Card import Card
import time
import random

pygame.init()
 
FPS = 30
image_w = 600 #
image_h = 800 #
screenDimensions = (image_w, image_h)
window = pygame.display.set_mode(screenDimensions, pygame.RESIZABLE)

font = pygame.font.Font(None, 28)

screen = pygame.display.get_surface()



START_X = 75
START_Y = 75





END_LOCATION = (image_w/2 - 75, image_h/2 - 50)


clock = pygame.time.Clock()

BACKGROUND_COLOR = (0, 0, 0)
COUNTER_LOCATION = (10, 10)


for i in range(3):
	NUM_COLS = i + 3
	NUM_ROWS = i + 4
	NUM_CARDS = NUM_COLS * NUM_ROWS
	matches_found = 0
	MATCHES = NUM_CARDS / 2
	X_OFFSET = 100 #
	Y_OFFSET = 140 #
	last_card = 0
	current_card = 0
	score = 1000

	cards = pygame.sprite.Group()

	cardList = []

	for i in range(MATCHES):
		cardList.append(i+1) 
	for i in range(MATCHES):
		cardList.append(i+1)

	for i in range(NUM_CARDS):
		card_num = random.choice(cardList);
		cards.add(Card(screen, START_X + (i % NUM_COLS) * X_OFFSET, START_Y + (i / NUM_COLS) * Y_OFFSET, 'Card' + str(card_num) + '.gif')) #get card
		cardList.remove(card_num);


	flipped = 0

	while matches_found != MATCHES:
		if score > 0:
			time_passed = clock.tick(FPS)
		
			screen.fill(BACKGROUND_COLOR)

			text = font.render("Score: " + str(score), 1, (255, 255, 255))

			screen.blit(text, COUNTER_LOCATION)
			cards.draw(screen)
			pygame.display.flip()

			ev = pygame.event.get()

			# proceed events
			for event in ev:
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						quit()
				# handle MOUSEBUTTONUP
				elif event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()

					# get a list of all sprites that are under the mouse cursor
					clicked_sprites = [s for s in cards if s.rect.collidepoint(pos)]
					for card in clicked_sprites:
						card.flip()
						cards.draw(screen)
						pygame.display.flip()
						sound = pygame.mixer.Sound('card_flip.wav')
						sound.play()
						time.sleep(1.0)
						last_card = current_card
						current_card = card
						flipped += 1	
					
					if flipped == 2:
						#correct match
						if last_card.image_name == current_card.image_name:
							sound = pygame.mixer.Sound('corrrect.wav') ##correct sound
							sound.play()
							last_card.kill()
							current_card.kill()
							matches_found += 1
						else: #incorrect match
							sound = pygame.mixer.Sound('incorrect.wav')## incorrect sound
							sound.play()
							last_card.flip()
							current_card.flip()
							score -= 40 #decrease score for incorrect match
						flipped = 0;

			score -= 1

		else:
			screen.fill(BACKGROUND_COLOR)
			game_over = font.render("GAME OVER", 1, (255, 255, 255))
			screen.blit(game_over, END_LOCATION)
			pygame.display.flip()

			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						quit()

		
screen.fill(BACKGROUND_COLOR)
game_over = font.render("You Win!", 1, (255, 255, 255))
screen.blit(game_over, END_LOCATION)
pygame.display.flip()

	

	



