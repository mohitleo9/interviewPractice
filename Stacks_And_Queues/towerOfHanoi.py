def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)


def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)


def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks > 0:
        helperPeg = 6 - startPeg - endPeg

        hanoi(ndisks-1, startPeg, helperPeg)
        print "Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg)
        hanoi(ndisks-1, helperPeg, endPeg)

hanoi(ndisks=3)
# moveTower(1,"A","B","C")
