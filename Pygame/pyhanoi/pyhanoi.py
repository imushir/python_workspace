from pygame import *

def wait_for_key():
	ourevent = event.wait()
	while ourevent.type != KEYDOWN:
		ourevent = event.wait()

def draw_discs():
	offset = 50

	for x in range (0, 3):
		if stack[x] == [3, 2, 1]:
			screen.blit(disc3, (offset, 400))
			screen.blit(disc2, (offset+25, 380))
			screen.blit(disc1, (offset+50, 360))
		if stack[x] == [3, 2]:
			screen.blit(disc3, (offset, 400))
			screen.blit(disc2, (offset+25, 380))
		if stack[x] == [3, 1]:
			screen.blit(disc3, (offset, 400))
			screen.blit(disc1, (offset+50, 380))
		if stack[x] == [2, 1]:
			screen.blit(disc2, (offset+25, 400))
			screen.blit(disc1, (offset+50, 380))
		if stack[x] == [3]:
			screen.blit(disc3, (offset, 400))
		if stack[x] == [2]:
			screen.blit(disc2, (offset+25, 400))
		if stack[x] == [1]:
			screen.blit(disc1, (offset+50, 400))
		offset += 200

def try_move(first, second):
	if len(stack[first]) == 0:
		return 0
	if len(stack[first]) > 0 and len(stack[second]) == 0:
		a = stack[first].pop()
		stack[second].append(a)
		return 1
	else:
		if len(stack[first]) > 0 and len(stack[second]) > 0:
			a = stack[first].pop()
			b = stack[second].pop()
			if a > b:
				invalidtext = movesfont.render('Invalid move!', True, (255,255,255), (0,0,0))
				screen.blit(invalidtext, (235,200))
				display.update()
				wait_for_key()
				stack[first].append(a)
				stack[second].append(b)
				return 0
			else:
				stack[second].append(b)
				stack[second].append(a)
				return 1

init()
screen = display.set_mode((640,480))
display.set_caption('PyHanoi')

backdrop = image.load('data/backdrop.jpg')

disc1 = image.load('data/disc1.png')
disc2 = image.load('data/disc2.png')
disc3 = image.load('data/disc3.png')

highlight1 = image.load('data/highlight1.png')
highlight2 = image.load('data/highlight2.png')

movesfont = font.Font(None, 40)

mixer.music.load('data/music.mod')
mixer.music.play(-1)

stack = [[3, 2, 1], [], []]

moves = 0
position = 0
selected1 = -1
selected2 = -1

quit = 0

while (quit == 0):
	screen.blit(backdrop, (0,0))
	draw_discs()

	if selected1 == -1:
		screen.blit(highlight1, (position * 200 + 30, 250))
	else:
		screen.blit(highlight2, (position * 200 + 30, 250))

	movestext = movesfont.render('Moves: ' + str(moves), True, (255,255,255), (0,0,0))
	screen.blit(movestext, (5,5))

	display.update()

	ourevent = event.wait()
	if ourevent.type == KEYDOWN:
		if ourevent.key == K_ESCAPE:
			quit = 1
		if ourevent.key == K_LEFT and position > 0:
			position -= 1
		if ourevent.key == K_RIGHT and position < 2:
			position += 1
		if ourevent.key == K_RETURN:
			if selected1 == -1:
				selected1 = position
			else:
				selected2 = position
				if selected2 == selected1:
					selected1 = -1
					selected2 = -1
				else:
					x = try_move(selected1, selected2)
					moves += x
					selected1 = -1
					selected2 = -1

