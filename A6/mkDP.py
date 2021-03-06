'''
  n  |    ways   | Rec #calls | Rectime(sec-s) | DP tabSize | DPtime(sec-s) |
-----------------------------------------------------------------------------
  200|   61984   |    64725   | 0.062173       |  1407      |  0.00146      |
-----------------------------------------------------------------------------
  400|	1554875  |   1593780  | 1.052454       |  2807      |  0.002925     |
-----------------------------------------------------------------------------
  600| 12256874  |  12472215  | 6.614477       |  4207      |  0.004517     |
-----------------------------------------------------------------------------
  800| 56505861  |  57272118  | 29.37985       |  5607      |  0.005628     |
-----------------------------------------------------------------------------
 1000| 190469796 | 192574217  | 98.20329       |  7007      |  0.008081     |
-----------------------------------------------------------------------------
			Coin Set: [1,2,5,10,25,50,100], Machine: HP-Z420

The execution time certainly increases as n increases for both mkDP and mkRec. 
For the recursive solution, this makes sense because the number of recursive calls 
increases as n increases, so the program will take longer to run. For the dynamic 
programming solution, the table size increases as n increases since the table 
is of size (# of coins)*(n+1). Therefore the program will take longer to run since it
needs to fill in more table entries. The recursive solution takes significantly
longer because it has to construct a tree and find the number of leaves. 
Because of the tree format, the program recalculates some subproblems more than 
once and has to run the recursive method multiple times to find the answer. 
The dynamic programming method, however, simply fills in a table based on previous 
information and only has to go through the method once. It doesn't re-solve subproblems
that have already been solved. 

'''

#! /usr/bin/python
import sys
import time

numOfWays = 0
tableSize = 0

# function to read in coin values
def readCoins(fnm):
	f = open(fnm)
	lst = []
	for line in f:
		l = line.strip().split(" ")
	for s in l:
		lst.append(int(s))
	return lst

# dp method
def makeChange(target, coins):
	global numOfWays
	global tableSize

	# get width and height
	width = len(coins)
	height = target+1

	# create and initialize table with zeros
	table = [[0]*width for x in range(height)]
	
	# go through table and set values dynamically
	for i in range(0, height):
		for j in range(0, width):
			# set first row values to 1 (one way to make change for 0)
			if(i==0):
				table[i][j] = 1
				#print "table at", i, j, "=", 1
			# set values for first coin column based on mod
			elif(j==0):
				if(i%coins[j]==0):
					table[i][j] = 1
					#print "table at", i, j, "=", 1
				#else:
					#print "table at", i, j, "=", table[i][j]
			# set values for coin value > row value
			elif(coins[j]>i):
				if((j-1) < 0):
					table[i][j] = 0
				else:
					table[i][j] = table[i][j-1]
				#print "table at", i, j, "=", table[i][j]
			# set all other tables values
			else:
				table[i][j] = table[i][j-1] + table[i-coins[j]][j]
				#print "table at", i, j, "=", table[i][j]
	
	numOfWays = table[height-1][width-1]
	tableSize = height*width

# main
if __name__ == "__main__":
	target = int(sys.argv[1])
	coins = readCoins(sys.argv[2])
	coins = sorted(coins)
	startTime = time.clock()
	makeChange(target, coins)
	endTime = time.clock() - startTime
	print "amount:", target, "coins:", coins, "ways:", numOfWays
	#print "time:", endTime
	#print "tableSize:", tableSize


