def gradientDescent(F, dF):
    w = 0
    numIters = 100
    eta = 0.01  # step size
    for t in range(numIters):
        value = F(w)
        gradient = dF(w)
        print "t = %s, w = %s, F(w) = %s, dF(w) = %s" % (t, w, value, gradient)
        w = w - eta * gradient
    return w

#################

points = [(2, 4), (4, 2)]
def F(w):
    #return (w - 5)**2
    return sum((x*w - y)**2 for x, y in points)

def dF(w):
    #return 2 * (w - 5) * 1
    return sum(2 * (x*w - y) * x for x, y in points)

gradientDescent(F, dF)
