import pygame
import os
class VolumeSystem():	
	
	def __init__(self, source, times=1, play_song=True):
		self.volume_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
		self.index = 5 
		self.volume_vel = 0.1
		self.volume_max = 1.0
		self.volume_min = 0.1
		self.cur_volume = self.volume_list[self.index]		
		self.source = source
		self.times = times
		self.play_song = play_song
		self.load = pygame.mixer.Sound(self.source)
		self.load.set_volume(self.cur_volume)

	def play(self):
		if self.play_song:
			self.load.play()
			print("Audio has been started")
		pass

	def stop(self):
		if self.play_song:
			self.load.stop()
			print("Audio has been stopped")
		pass

	def volumeUP(self):
		print(f"Audio has been turned up {self.cur_volume}")
		# range 0.0 - 1.0
		if self.index <= 9:
			self.index += 1
			try:
				self.cur_volume = self.volume_list[self.index]
			except:
				print("index error")
			self.load.set_volume(self.cur_volume)
		else:
			print("Max volume reach.")			
		pass

	def volumeDOWN(self):
		print(f"Audio has been turned down {self.cur_volume}")
		# range 0.0 - 1.0
		if 1 <= self.index:
			self.index -= 1
			try:
				self.cur_volume = self.volume_list[self.index]
			except:
				print("index error")
			self.load.set_volume(self.cur_volume)
		else:
			print("Min volume reach.")
		pass

	def __del__(self):
		pass