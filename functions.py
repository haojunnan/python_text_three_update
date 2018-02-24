#coding:gb2312
import pygame
import sys
from random import randint
from rain import Rain
def check_event():
	"""鼠标键盘控制退出"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()

def screen_update(al_setting,screen,rains):
	"""刷新界面"""
	screen.fill(al_setting.bg_color)
	rains.draw(screen)
	pygame.display.flip()
	
def creat_rain(al_setting,screen,rain_number,rain_row,rains):
	"""创建（随机）一个雨滴"""
	rain = Rain(al_setting,screen)
	rain.width = rain.rect.width
	rain.height = rain.rect.height
	rain.x = rain.width + 2 * rain.width * rain_number
	rain.rect.x = rain.x
	rain.y = rain.height + 2 * rain.height * rain_row
	rain.rect.y = rain.y
	rains.add(rain)
	
def rain_numbers(al_setting,screen):
	"""计算一行最多能容纳雨滴数"""
	rain = Rain(al_setting,screen)
	rain_numbers = int(al_setting.screen_width / (2 * rain.rect.width))
	return rain_numbers
	
def get_rows(al_setting,screen):
	"""计算雨滴行数"""
	rain = Rain(al_setting,screen)
	rain_rows = int(al_setting.screen_height / (2 * 
	rain.rect.height))
	return rain_rows
	
def rain_get(al_setting,screen,rains):
	"""生成雨滴"""
	for rain_row in range(get_rows(al_setting,screen)):
		for rain_number in range(rain_numbers(al_setting,screen)):
			creat_rain(al_setting,screen,rain_number,rain_row,rains)

def rain_update(al_setting,screen,rains):
	"""更新雨滴，移除屏幕外雨滴，补充雨滴"""
	rains.update()
	screen_rect = screen.get_rect()
	#移除屏幕外雨滴
	for rain in rains.copy():
		if rain.rect.bottom >= screen_rect.bottom:
			rains.remove(rain)
	al_number = rain_numbers(al_setting,screen)
	al_row = get_rows(al_setting,screen)
	now_row = int(len(rains) / al_number)
	#如果有一行消失，再生成一行
	if  now_row < al_row:
		for rain_number in range(al_number):
			creat_rain(al_setting,screen,rain_number,0,rains)
	print(len(rains))
