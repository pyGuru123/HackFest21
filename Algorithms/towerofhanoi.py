def towerOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
    if numberOfDisks:
        towerOfHanoi(numberOfDisks - 1, startPeg, 6 - startPeg - endPeg)
        print("Move disk %d from peg %d to peg %d" % (numberOfDisks, startPeg, endPeg))
        towerOfHanoi(numberOfDisks, 6 - startPeg - endPeg, endPeg)

towerOfHanoi(numberOfDisks=4)
