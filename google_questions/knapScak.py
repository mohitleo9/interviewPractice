
def knapSack(objects, w, prices):
    if w <=0:
        return 0

    if len(objects) == 1 :
        if w - prices[objects[0]] > 0:
            return prices[objects[0]]
        else:
            return 0

    sol = {}
    for i in objects:
        if w - prices[i] > 0:
            sol[i] = prices[i] + knapSack([j for j in objects if j != i], w - i, prices)

    return max(sol.values())

def main():
    objects = [2,4,6]
    w = 12
    prices = {
            2:6,
            4:5,
            6:20
            }

    print knapSack(objects, 12, prices)

main()


