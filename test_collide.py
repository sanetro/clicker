import pygame
import sys, os
from win32api import GetSystemMetrics
from modules.button import BTN
from modules.volume import VolumeSystem


pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 20)
click = False



# ------------------------------------------------ SAVES ------------------------------------------------ # 
file = open("metadata.txt", 'r')

for line in file:
	print(line.split())



# ------------------------------------------------ MASTER RESOLUTION ------------------------------------------------ # 
FPS = 50
WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)
MASTER = pygame.display.set_mode((WIDTH, HEIGHT))


# ------------------------------------------------ TITLE AND ICON SETUP ------------------------------------------------ # 
pygame.font.init()
pygame.display.set_caption("Cigarettes Clicker")
icon = pygame.image.load(os.path.join('images', 'icon.png'))
title = pygame.image.load(os.path.join('images', 'title1.png'))
title = pygame.transform.scale(title, (1024,454))
pygame.display.set_icon(icon)

# ------------------------------------------------ COLORS AND THEMES ------------------------------------------------ # 
COLOR_BACKGROUND = (6, 21, 31)
COLOR_BORDER_BACKGROUND = (21, 65, 117)
GREEN = (11, 100, 241)

DARK_TOM = pygame.image.load(os.path.join('images', 'mroczny_tom.png'))
DARK_TOM = pygame.transform.scale(DARK_TOM, (400, 400))

MENU_BACKGROUND = pygame.image.load(os.path.join('images', 'menu_background.png'))
MENU_BACKGROUND = pygame.transform.scale(MENU_BACKGROUND, (WIDTH, HEIGHT))

GAME_BACKGROUND = pygame.image.load(os.path.join('images', 'game_background.png'))
GAME_BACKGROUND = pygame.transform.scale(GAME_BACKGROUND, (WIDTH, HEIGHT))

OPTION_BACKGROUND = pygame.image.load(os.path.join('images', 'option_background.png'))
OPTION_BACKGROUND = pygame.transform.scale(OPTION_BACKGROUND, (WIDTH, HEIGHT))

# ------------------------------------------------ SOUNDS ------------------------------------------------ #
pygame.mixer.init()


 
# ------------------------------------------------ BTNS STANDRADS ------------------------------------------------ #
BTN_COLOR = (23, 203, 209)
BTN_COLOR_ACTIVE = (21, 65, 117)
BTN_WIDTH = 300
BTN_HEIGHT = 70
BTNS_MIN_LINE_SPACE = 450 
BTN_CENTER = WIDTH//2 - BTN_WIDTH//2

# ------------------------------------------------ MENU ACTIVITY ------------------------------------------------ # 
MENU_ACTIVE = True
MENU_MUSIC = VolumeSystem("menu_music.mp3", "music")
CLICK_SOUND = VolumeSystem("clicking.wav", "music")

# ------------------------------------------------ BTNS SETUP ------------------------------------------------ #

buttonStart = BTN(BTN_COLOR, BTN_CENTER, 50+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='Start')
buttonOptions = BTN(BTN_COLOR, BTN_CENTER, 150+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='Options')
buttonBack = BTN(BTN_COLOR, BTN_CENTER, 150+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='back')
buttonAudio = BTN(BTN_COLOR, BTN_CENTER, 150+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='Audio:on')
buttonPlus = BTN(BTN_COLOR, BTN_CENTER+310, 150+BTNS_MIN_LINE_SPACE, 90, BTN_HEIGHT, text='+')
buttonMinus = BTN(BTN_COLOR, BTN_CENTER-100, 150+BTNS_MIN_LINE_SPACE, 90, BTN_HEIGHT, text='-')
board_Volume = BTN((57, 165, 168), BTN_CENTER, 250+BTNS_MIN_LINE_SPACE, BTN_WIDTH, 100+BTN_HEIGHT, text=f'{MENU_MUSIC.cur_volume}')
buttonExit = BTN(BTN_COLOR, BTN_CENTER, 250+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='EXIT')

# Add button pointer if you created 
buttons_in_menu_List = [buttonStart, buttonOptions, buttonExit]
buttons_in_options_List = [buttonBack, buttonMinus, buttonPlus, buttonAudio, board_Volume]

def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

def buttonsDrawMenu(mx, my, MASTER):
	for button in buttons_in_menu_List:
		button.draw(MASTER, outline=1)
		if button.isOver((mx,my)):
			button.color = BTN_COLOR
		else:
			button.color = BTN_COLOR_ACTIVE

def buttonsDrawOptions(mx, my, MASTER):
	for button in buttons_in_options_List:
		button.draw(MASTER, outline=1)
		if button.isOver((mx,my)):
			button.color = BTN_COLOR
		else:
			button.color = BTN_COLOR_ACTIVE




	



click = False




def menu():
	global click
	while True:	
		MASTER.fill((33, 33, 33))
		MASTER.blit(MENU_BACKGROUND, (0,0))
		draw_text('menu', font, (255, 255, 255), MASTER, WIDTH-100, HEIGHT-100)

		mx, my = pygame.mouse.get_pos()

		buttonsDrawMenu(mx, my, MASTER)
		MASTER.blit(DARK_TOM, (BTN_CENTER-55, 70))

		if buttonStart.isOver((mx,my)):
			if click:
				CLICK_SOUND.play()
				click = False
				game(mx, my)
		if buttonOptions.isOver((mx,my)):
			if click:
				CLICK_SOUND.play()
				click = False
				options(mx, my)

		if buttonExit.isOver((mx,my)):
			if click:
				CLICK_SOUND.play()
				click = False
				pygame.quit()
				sys.exit()
		
		click = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # when user click close
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: # when event key is esc in menu close
					pygame.quit()
					sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		clock.tick(60)		
	
def game(mx, my):
	global click
	running = True
	while running:
		MASTER.fill((33, 33, 133))
		MASTER.blit(GAME_BACKGROUND, (0,0))
		
		mx, my = pygame.mouse.get_pos()
		
		draw_text('GAME', font, (255, 255, 255), MASTER, 20, 20)



		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # when user click close
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

		pygame.display.update()
		clock.tick(60)




def options(mx, my):
	global click
	running = True
	while running:
		mx, my = pygame.mouse.get_pos()
		
		MASTER.fill((33, 133, 33))
		MASTER.blit(OPTION_BACKGROUND, (0,0))
		draw_text('options', font, (255, 255, 255), MASTER, 20, 20)

		buttonsDrawOptions(mx, my, MASTER)

		if buttonMinus.isOver((mx,my)):
			if click:
				CLICK_SOUND.play()
				MENU_MUSIC.volumeDOWN()
		if buttonPlus.isOver((mx,my)):
			if click:
				CLICK_SOUND.play()
				MENU_MUSIC.volumeUP()
				

		click = False	

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # when user click close
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		clock.tick(60)

if __name__ == "__main__":
	MENU_MUSIC.play()
	menu()