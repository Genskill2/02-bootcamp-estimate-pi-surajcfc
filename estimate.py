import math
import unittest

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
    
import random

def wallis(n):
    x=1
    for i in range(1,n+1):
        x=x*4*pow(i,2)/(4*(pow(i,2)) - 1)
    return 2*x

def monte_carlo(n):
    sq=0	
    cir=0
    r=0
    for i in range(0,n):
        a=random.random()
        b=random.random()
        c=pow(pow(a,2)+pow(b,2),0.5)
        if(c<=1):
            cir+=1
            sq+=1
        else:
            sq+=1
    r=float(cir/sq)
    return 4*r

print("enter n for wallis")
n=int(input())
print(wallis((n)))
print("enter n for monte carlo")
n=int(input())
print(monte_carlo(n))    
