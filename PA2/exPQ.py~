#! /usr/bin/python
import sys

# heaps here are 1 based, so read puts None in 0th element
def readNums(fnm):
   f = open(fnm)
   lst = [None]
   for line in f:
      l = line.strip().split(" ")
      for s in l:
        lst.append(int(s))
   return lst

# heaps here are 1 based
def parent(i): return i/2
def left(i): return 2*i
def right(i): return 2*i+1

# so for their length element 0 does not count
def hLen(A): return len(A)-1

def heapify(A, i, n): 
	"""
	Build a Min Heap at i
	n is the number of elements in the heap
	A[i] is "almost a heap" (except root i), 
	Make A[i] a heap 
	"""
	minVal = i
	l = left(i)
	r = right(i)
	if l <= n and A[l] < A[i]:
		minVal = l
	if r <= n and A[r] < A[minVal]:
		minVal = r
	if minVal != i:
		A = swap(A,i,minVal)
		heapify(A,minVal,n)

# build a Min heap A from an unsorted array
def buildHeap(A): 
	size = hLen(A)
	for x in range(size//2,0,-1):
		heapify(A,x,size)  

def heapExtractMin(A):
	root = A[1]
	A[1] = A[hLen(A)]
	A.pop(hLen(A))
	heapify(A, 1, hLen(A))
	return root,A

def heapInsert(A,v):
	A.append(int(v))
	currIndex = len(A) - 1
	par = parent(currIndex)
	while par >= 1 and A[currIndex] < A[par]:
		A = swap(A,par,currIndex)
		currIndex = par
		par = parent(par)
	return A

# swap elements x and y in array A
def swap(A,x,y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp
	return A

if __name__ == "__main__":
   db = len(sys.argv)>2
   A  = readNums(sys.argv[1])
   if db: print "Input:", A[1:]
   buildHeap(A)
   min,A = heapExtractMin(A)
   print "min", min
   A = heapInsert(A,0)
   min,A = heapExtractMin(A)
   print "min", min
   min,A = heapExtractMin(A)
   print "min", min


