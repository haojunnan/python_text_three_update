#coding:gb2312
import pygame
import functions as gf
from rain import Rain
from pygame.sprite import Group
from settings import Settings
def run_game():
	#��ʼ��
	pygame.init()
	al_setting = Settings()
	#��ʼ����Ļ
	screen = pygame.display.set_mode((al_setting.screen_width,
	al_setting.screen_height))
	pygame.display.set_caption("rains")
	#�������ʵ������
	rain = Rain(al_setting,screen)
	rains = Group()
	#��������
	gf.rain_get(al_setting,screen,rains)
	while True:
		#�����̵���¼�
		gf.check_event()
		#���������
		gf.rain_update(al_setting,screen,rains)
		#������Ļ
		gf.screen_update(al_setting,screen,rains)
run_game()
