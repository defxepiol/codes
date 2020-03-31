import pygame

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Drawing in pygame")

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
		elif event.type == pygame.MOUSEMOTION:
			mouse_position = pygame.mouse.get_pos()
			pygame.draw.line(screen,(0,0,0),mouse_position,mouse_position)
	screen.fill((255,255,255))
	pygame.display.update()

pygame.quit()