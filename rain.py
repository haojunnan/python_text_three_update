#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Rain(Sprite):
	"""����һ�����"""
	def __init__(self,al_setting,screen):
		"""��ʼ����β�ȷ����λ��"""
		super(Rain,self).__init__()
		self.screen = screen
		self.al_setting = al_setting
		self.image = pygame.image.load("rain.bmp")
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.y = float(self.rect.y)
	def update(self):
		"""������δ����ױߣ���������"""
		self.y += self.al_setting.rain_speed
		self.rect.y = self.y
