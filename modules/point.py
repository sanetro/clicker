import pygame


def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

class MouseClickAnimation():
	def __init__(self, mx, my):
		self.mx = mx
		self.my = my
		self.fly = 0
		self.fly_max_point = 50
		self.mouse_click_particle_condition = False
		self.flx = 0
		print("CREATED")

	def draw(self, surface, point_per_click):
		draw_text(f"+{point_per_click}", font, (200, 0, 0), surface, self.flx+10, self.fly)
		# Draw when you find top of the roof, then delete object
		if self.mouse_click_particle_condition:
			# fly mean vel, iteriation		
			self.fly -= 5 
			if self.fly <= self.fly_max_point:
				#draw till the end of box
				draw_text(f"+{point_per_click}", font, (200, 0, 0), surface, self.flx+10, self.fly)
			else:
				# stop condition and delete element
				self.mouse_click_particle_condition = False
		