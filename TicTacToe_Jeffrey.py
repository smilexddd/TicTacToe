# Jeffrey Chiu
# PM
import random
import sys
from random import randint

checkgame = None
board=[1,2,3,4,5,6,7,8,9]
x = "X"
currentuser = x
z = 0
jk = None

o = "O"

intro="Welcome to a game of Tic-Tac-Toe! The object of the game is to get three in a row!"
def tiegame():
	showtheboard()
	print "Tie Game"


def mode():
	global z
	global x
	global o
	global checkgame
	global currentusers
	k = None
	print "    	"
	print "						"
	print intro
	print "											"
	print "							"
	k = raw_input ("Choose a Mode:  1) 1 Player         2) 2 Player   3) Computer vs Computer   4) Smart AI vs Dumb AI   5) Quit ")
	if k == "5":
		return None
	if k == "2":
		choosespace(x)
		return
	if k == "1":
		one(x)
		return
	if k == "3":
		testAI(x)
		return
	if k == "4":
		dumbAI(x)
	
	else:
		print "Invalid Input"
		mode()

	

def goodgame():
	print 'Game Over'
	

def RandomAI(gooh):
	global jk
	global board
	global z
	global x
	global o
	global checkgame
	player2 = gooh
	d= random.randint(0,8)
	fos= True
	while fos:
		if board[d] != x and board[d] != o:
			board[d] = gooh
			showtheboard()
			fos = False
		else:
			RandomAI(gooh)
		if gooh == x:
			gooh == o
		elif gooh == o:
			gooh == x
	checkgame = checkwin()
	if checkgame == True:
		print ' '
		showtheboard()
		print ' '
		print "Game Over"
		print ' '
	elif checkgame == False:
		print ' '
		print 'Next Turn'
		print ' '
		RandomAI(gooh)
	



def one(oneplayer):
	global board
	global z
	global x
	global o
	global checkgame
	global currentuser
	showtheboard()
	print ' '
	g = raw_input("Choose an availible spot from 1~9! ")
	print ' '
	if g == "1" or g == "2" or g == "3" or g =="4" or g == "5" or g == "6" or g == "7" or g == "8" or g =="9":
		g=int(g)
	else:
		print "Invalid Input"
		one(oneplayer)
	if board[g-1] != x and board[g-1] != o:
		board[g-1] = x
	else:
		print ' '
		print "Spot Taken"
		print ' '
		one(x)
	checkgame = checkwin()
	if checkgame == True:
		showtheboard()
		print "Game Over"
		return
		
	if checkgame == False:
		z = z+1
		print ' '
		print "Next Turn"
		computer()
	
def computer():
	global board
	global z
	global x
	global o
	global checkgame
	global currentuser
	
	finding = True
	d = random.randint(0,8)
	while finding:
		if board[d] != x and board[d] != o:
			board[d] = o
			finding = False
		else:
			computer()
			finding = False
	checkgame = checkwin()
	if checkgame == True:
		showtheboard()
		goodgame()
		
	if checkgame == False:
		z = z+1
		print ' '
		print ""
		print ' '
		one(x)
	



def start():
	print intro
def showtheboard():
	global board
	print board[0],'|',board[1],'|',board[2]
	print "----------"
	print board[3],"|",board[4],"|",board[5]
	print "----------"
	print board[6],"|",board[7],"|",board[8]
def checkwin():
	global board
	global z
	global x
	global o

	if  board[0] == x and board[1]==x and board[2]== x:
		return True
	if board[0]==x and board[4]== x and board[8]== x:
		return True
	if board[2]==x and board[4]== x and board[6]== x:
		return True
	if board[3]==x and board[4]== x and board[5]== x:
		return True
	if board[6]==x and board[7]== x and board[8]== x:
		return True
	if board[0]==x and board[3]== x and board[6]== x:
		return True
	if board[1]==x and board[4]== x and board[7]== x:
		return True
	if board[2]==x and board[5]== x and board[8]== x:
		return True
	if  board[0] == o and board[1]==o and board[2]== o:
		return True
	if board[0]==o and board[4]== o and board[8]== o:
		return True
	if board[2]==o and board[4]== o and board[6]== o:
		return True
	if board[3]==o and board[4]== o and board[5]== o:
		return True
	if board[6]==o and board[7]== o and board[8]== o:
		return True
	if board[0]==o and board[3]== o and board[6]== o:
		return True
	if board[1]==o and board[4]== o and board[7]== o:
		return True
	if board[2]==o and board[5]== o and board[8]== o:
		return True
	elif z == 8:
		return(tiegame())
	else:
		return False


def choosespace(player):
	global z
	global x
	global o
	global checkgame
	global currentuser
	global board
	currentplayer = player
	printplayer = currentplayer
	
	showtheboard()
	n= raw_input("Choose an availible spot from 1~9! ")
	if n == "1" or n == "2" or n == "3" or n =="4" or n == "5" or n == "6" or n == "7" or n == "8" or n =="9":
		n=int(n)
	else:
		print "Invalid Input"
		choosespace(currentplayer)
	if board[n-1] != x and board[n-1] != o:
		board[n-1] = player
	else:
		print " "
		print "Spot Taken"
		print " "
		choosespace(currentplayer)
	if currentplayer == x:
		currentplayer = o
	elif currentplayer == o:
		currentplayer = x
	checkgame = checkwin()
	currentuser = currentplayer
	if checkgame == True:
		showtheboard()
		print "Game Over"
	elif checkgame == False:
		z = z+1
		print ' '
		choosespace(currentuser)

def testAI(inpu):
	global board
	global z
	global x
	global o
	global checkgame
	global currentuser
	
	finding = True
	d = random.randint(0,8)
	while finding:
		if board[d] != x and board[d] != o:
			board[d] = x
			finding = False
			print ' '
			showtheboard()
		else:
			testAI(x)
			finding = False
	checkgame = checkwin()
	if checkgame == True:
		print ' '
		return(goodgame())
		showtheboard()
	elif checkgame == False:
		z = z+1
		print ' '
		print ""
		print ' '
		AItest(o)
def AItest(inp):
	global board
	global z
	global x
	global o
	global checkgame
	global currentuser
	
	finding = True
	d = random.randint(0,8)
	while finding:
		if board[d] != x and board[d] != o:
			board[d] = o
			print ' '
			finding = False
		else:
			AItest(o)
			finding = False
	checkgame = checkwin()
	if checkgame == True:
		print ' '
		showtheboard()
		return(goodgame())
		
	elif checkgame == False:
		z = z+1
		print ' '
		print ""
		print ' '
		testAI(x)
def SmartAI(you):
	global board
	global z
	global x
	global o
	global checkgame
	global currentuser
	if board[0] == x and board[1] == x and board[2] != x and board[2] != o:
		board[2] = o
		
	elif board[0] == x and board[4] == x and board[8] !=x and board[8] != o:
		board[8] = o
		
	elif board[2] == x and board[4] == x and board[6] !=x and board[6] != o:
		board[6] = o

	elif board[3] == x and board[4] == x and board[5] !=x and board[5] != o:
		board[5] = o
	
	elif board[6] == x and board[7] == x and board[8] != x and board[8] !=o:
		board[8] = o

	elif board[0] == x and board[3] == x and board[6] != x and board[6] != o:
		board[6] = o

	elif board[1] == x and board[4] == x and board[7] != x and board[7] != o:
		board[7] = o
	elif board[2] == x and board[5] == x and board[8] !=x and board[8] !=o:
		board[8] = o
	elif board[4] != x and board[4] != o:
		board[4] = o
	elif board[0] != x and board[0] != o:
		board[0] = o
	elif board[2] != x and board[2] != o:
		board[2] = o
	elif board[6] != x and board[6] != o:
		board[6] = o
	elif board[8] != x and board[8] != o:
		board[8] = o
	elif board[1] != x and board[1] != o:
		board[1] = o
	elif board[3] != x and board[3] != o:
		board[3] = o
	elif board[5] != x and board[5] != o:
		board[5] = o
	else :
		board[7] = o
	checkgame = checkwin()
	if checkgame == True:
		showtheboard()
		print ' '
		return(goodgame())
	elif checkgame == False:
		showtheboard()
		z = z+1
		print ' '
		print ""
		print ' '
		dumbAI(x)
	
def dumbAI(hi):
	global board
	global z
	global x
	global o
	global checkgame
	global currentuser
	
	finding = True
	d = random.randint(0,8)
	while finding:
		if board[d] != x and board[d] != o:
			board[d] = x
			print ' '
			finding = False
		else:
			dumbAI(x)
			finding = False
	checkgame = checkwin()
	if checkgame == True:
		print ' '
		showtheboard()
		return(goodgame())
		
	elif checkgame == False:
		showtheboard()
		z = z+1
		print ' '
		print ""
		print ' '
		SmartAI(o)

	


mode()













