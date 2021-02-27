import pygame
import sys, os
from win32api import GetSystemMetrics
from modules.button import BTN
from modules.volume import VolumeSystem


pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)
click = False



# ------------------------------------------------ SAVES ------------------------------------------------ # 
file = open("metadata.txt", 'r')



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
COLOR_BACKGROUND_BLUE = (6, 21, 31)
COLOR_BORDER_BACKGROUND_BLUE = (21, 65, 117)
DARK_GREEN= (0, 63, 55)
LIGHT_GREEN= (0, 135, 138)
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
BTN_COLOR_BLUE = (23, 203, 209)
BTN_COLOR_BLUE_ACTIVE = (21, 65, 117)
BTN_COLOR_RED = (138, 3, 0)
BTN_COLOR_RED_ACTIVE = (227, 23, 23)
BTN_WIDTH = 300
BTN_HEIGHT = 70
BTNS_MIN_LINE_SPACE = 450 
BTN_CENTER = WIDTH//2 - BTN_WIDTH//2

# ------------------------------------------------ MENU ACTIVITY ------------------------------------------------ # 
MENU_ACTIVE = True
MENU_MUSIC = VolumeSystem("menu_music.mp3", "music")
CLICK_SOUND = VolumeSystem("clicking.wav", "music")
CLICK_SOUND_BURN_OUT = VolumeSystem("match_burn_out.mp3", "music")

# ------------------------------------------------ BTNS SETUP ------------------------------------------------ #

buttonStart = BTN(BTN_COLOR_BLUE, BTN_CENTER, 50+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='Start')
buttonOptions = BTN(BTN_COLOR_BLUE, BTN_CENTER, 150+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='Options')
buttonBack = BTN(BTN_COLOR_RED, BTN_CENTER, 50+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='back')
buttonAudio = BTN(BTN_COLOR_RED, BTN_CENTER, 150+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='Audio:on')
buttonPlus = BTN(BTN_COLOR_RED, BTN_CENTER+310, 150+BTNS_MIN_LINE_SPACE, 90, BTN_HEIGHT, text='+')
buttonMinus = BTN(BTN_COLOR_RED, BTN_CENTER-100, 150+BTNS_MIN_LINE_SPACE, 90, BTN_HEIGHT, text='-')
board_Volume = BTN((57, 165, 168), BTN_CENTER, 250+BTNS_MIN_LINE_SPACE, BTN_WIDTH, 100+BTN_HEIGHT, text=f'{MENU_MUSIC.cur_volume}')
buttonExit = BTN(BTN_COLOR_BLUE, BTN_CENTER, 250+BTNS_MIN_LINE_SPACE, BTN_WIDTH, BTN_HEIGHT, text='EXIT')

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
			button.color = BTN_COLOR_BLUE
		else:
			button.color = BTN_COLOR_BLUE_ACTIVE

def buttonsDrawOptions(mx, my, MASTER):
	for button in buttons_in_options_List:
		button.draw(MASTER, outline=1)
		if button.isOver((mx,my)):
			button.color = BTN_COLOR_RED
		else:
			button.color = BTN_COLOR_RED_ACTIVE








def menu():
	global click, MENU_MUSIC, file
	while True:
	
		mx, my = pygame.mouse.get_pos()
		for i, line in enumerate(file, start=1):
			print(line)
			
		MASTER.fill((33, 33, 33))
		MASTER.blit(MENU_BACKGROUND, (0,0))
		buttonsDrawMenu(mx, my, MASTER)
		MASTER.blit(DARK_TOM, (BTN_CENTER-55, 70))
		draw_text('Prototype 1.0.0', font, (255, 255, 255), MASTER, 20, 20)		

		

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





	
class MouseClickAnimation():
	def __init__(self):
		self.flx = 0
		self.fly = 0
		self.fly_max_point = 50
		self.mouse_click_particle_condition = False		
		print("CREATED")

	def draw(self, surface, point_per_click, mx, my):
		self.flx = mx
		self.fly = my
		if self.mouse_click_particle_condition:
			draw_text(f"+{point_per_click}", pygame.font.SysFont("Impact", 50), (132,232,32), surface, self.mx+10, self.my)
			if self.my >= self.fly_max_point:
				self.my -= 15 
			else:
				self.my = 0
				self.mx = -2200
		
		


class Shop():
	
	def __init__(self, color, x, y, text, img_active, img_unactive, img_bought, icon, score_to_buy):
		self.color = color
		self.x = x
		self.y = y		
		self.text = text
		self.img_active = img_active
		self.img_unactive = img_unactive
		self.bought = False
		self.active = False
		self.img_bought = img_bought
		self.score_to_buy = score_to_buy
		self.icon = icon
	

	def draw(self, surface, score):
		if not self.bought:
			if score < self.score_to_buy:  
				source = pygame.image.load(os.path.join('images', "shop_items", self.img_unactive))
			if score >= self.score_to_buy: 
				source = pygame.image.load(os.path.join('images', "shop_items", self.img_active))
				self.active = True
		else:
			source = pygame.image.load(os.path.join('images', "shop_items", self.img_bought))
		img = pygame.transform.scale(source, (562, 135))		
		surface.blit(img, (self.x, self.y))
		icon_source = pygame.image.load(os.path.join('images', "shop_items", self.icon))
		icon = pygame.transform.scale(icon_source, (20, 20))
		surface.blit(icon_source, (self.x + 15, self.y + 15))
		if self.bought:
			draw_text(self.text, pygame.font.SysFont(None, 25), (255, 255, 60), surface, self.x + 150, self.y + 15)
		else:
			draw_text(self.text, pygame.font.SysFont(None, 25), LIGHT_GREEN, surface, self.x + 150, self.y + 15)

	def isBought(self, pos, clicked):
		if not self.bought and self.active:
			if pos[0] > self.x and pos[0] < self.x + 562:
				if pos[1] > self.y and pos[1] < self.y + 135:
					if clicked:
						self.bought = True
						 
		pass


	



def game(mx, my):
	'''
	** EARLY STAGE **
	LEVEL 1	LEVEL 2	LEVEL 3	LEVEL 4	LEVEL 5	LEVEL 6 LEVEL 7	LEVEL 8	LEVEL 9 LEVEL 10
	0.0001	0.001	0.01	0.1		1.0		2.0		5.0		10.0	15.0	20.0

	** MID STAGE **
	LEVEL 11	LEVEL 12	LEVEL 13	LEVEL 14	LEVEL 15	LEVEL 16 	LEVEL 17	LEVEL 18	LEVEL 19 	LEVEL 20
	25.0		50.0		65.0		70.0		80.0		90.0		100.0		115.0		125.0	 	150.0

	** END STAGE **
	LEVEL 11	LEVEL 12	LEVEL 13	LEVEL 14	LEVEL 15	LEVEL 16 	LEVEL 17	LEVEL 18	LEVEL 19 	LEVEL 20
	25.0		50.0		65.0		70.0		80.0		90.0		100.0		115.0		125.0	 	150.0
	

	MIlion	10^6
	BIlion	10^12
	TRYlion	10^18
	KWADRylion	10^24
	KWINTylion	10^30
	SEKSTylion	10^36
	SEPTylion	10^42
	OKTylion	10^48
	NONylion	10^54
	DECylion	10^60
	'''
	global MENU_MUSIC
	global click
	running = True
	click = False
	start_counting_score = False
	game_score = 0
	point_per_sec = 0.0
	point_per_click = 1
	floatingPoint = MouseClickAnimation()


	abi = "active_border_item.png"
	ubi = "unactive_border_item.png"
	bbi = "bought_border_item.png"

	whiteCigarette_icon ="whiteCigarette_icon.png"
	whiteCigaretteDesc = "Dodaje 0.1 papierosa na sekunde. koszt 10"
	whiteCigarette = Shop((255, 255, 555), 1250, 100, whiteCigaretteDesc, abi, ubi, bbi, whiteCigarette_icon, 10)
	whiteCigaretteHappened = False

	redCigarette_icon ="redCigarette_icon.png"
	redCigaretteDesc = "Dodaje 0.5 papierosa na sekunde. koszt 200"
	redCigarette = Shop((255, 255, 555), 1250, 250, redCigaretteDesc, abi, ubi, bbi, redCigarette_icon, 200)
	redCigaretteHappened = False

	goldCigarette_icon ="goldCigarette_icon.png"
	goldCigaretteDesc = "Dodaje 1.5 papierosa na sekunde. koszt 1000"
	goldCigarette = Shop((255, 255, 555), 1250, 400, goldCigaretteDesc, abi, ubi, bbi, goldCigarette_icon, 1000)
	goldCigaretteHappened = False

	while running:
		MASTER.fill((33, 33, 133))
		MASTER.blit(GAME_BACKGROUND, (0,0))
		
		mx, my = pygame.mouse.get_pos()
		
		game_score += point_per_sec

		panel_left = pygame.draw.rect(MASTER, (DARK_GREEN), (50, 50, 633, 980),0) # Left 
		panel_center = pygame.draw.rect(MASTER, (DARK_GREEN), (720, 50, 481, 980),0) # Center
		panel_right = pygame.draw.rect(MASTER, (DARK_GREEN), (1238, 50, 633, 980),0) # Right

		# ======================= LEFT PANEL ======================= #
		if panel_left.collidepoint((mx, my)):
			if click:
				game_score += point_per_click
				CLICK_SOUND_BURN_OUT.play()
				floatingPoint.mx = mx
				floatingPoint.my = my				
				floatingPoint.mouse_click_particle_condition = True								
				
		
		if floatingPoint.mouse_click_particle_condition:
			floatingPoint.draw(MASTER, point_per_click, floatingPoint.mx, floatingPoint.my)
			

		
		# ======================= CENTER PANEL ======================= #	
		if panel_center.collidepoint((mx, my)):
			if click:
				point_per_click += 0.5
				floatingPoint.draw(MASTER, point_per_click, mx, my)
						

		# ======================= RIGHT PANEL ======================= #
		#if panel_right.collidepoint((mx, my)):
		#	if click:
		#		point_per_sec += 110.000_1
				

		
		
			
	    # soon  -- still in progress
		whiteCigarette.draw(MASTER, game_score)
		whiteCigarette.isBought((mx, my), click)
		if whiteCigarette.bought:
			if not whiteCigaretteHappened:
				point_per_sec += 0.01
				game_score -= 10	
				whiteCigaretteHappened = True

		redCigarette.draw(MASTER, game_score)
		redCigarette.isBought((mx, my), click)
		if redCigarette.bought:
			if not redCigaretteHappened:
				point_per_sec += 0.05
				game_score -= 200	
				redCigaretteHappened = True		

		goldCigarette.draw(MASTER, game_score)
		goldCigarette.isBought((mx, my), click)
		if goldCigarette.bought:
			if not goldCigaretteHappened:
				point_per_sec += 0.15
				game_score -= 1000	
				goldCigaretteHappened = True

		draw_text("Papierosy:", pygame.font.SysFont(None, 25), (0,135,138), MASTER, 60, 70)
		draw_text(f" {round(game_score, 1)}", pygame.font.SysFont("IMPACT", 150), (0,165,138), MASTER, 240, 480)



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




def options(mx, my):
	global buttonAudio, board_Volume, MENU_MUSIC, click
	running = True
	

	while running:
		mx, my = pygame.mouse.get_pos()
		
		MASTER.fill((33, 133, 33))
		MASTER.blit(OPTION_BACKGROUND, (0,0))
		

		buttonsDrawOptions(mx, my, MASTER)

		if buttonMinus.isOver((mx,my)):
			if click:
				CLICK_SOUND.play()
				MENU_MUSIC.volumeDOWN()
				board_Volume.text = str(MENU_MUSIC.cur_volume)

		if buttonPlus.isOver((mx,my)):
			if click:
				CLICK_SOUND.play()
				MENU_MUSIC.volumeUP()
				board_Volume.text = str(MENU_MUSIC.cur_volume)

		if buttonAudio.isOver((mx,my)):
			if click:
				CLICK_SOUND.play()				
				if buttonAudio.text == "Audio:on":
					buttonAudio.text = "Audio:off"
					MENU_MUSIC.stop()
					print("stop")
				else:
					buttonAudio.text = "Audio:on"
					MENU_MUSIC.play()
					print("play")

		if buttonBack.isOver((mx,my)):
			if click:
				CLICK_SOUND.play()
				running = False		

				

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