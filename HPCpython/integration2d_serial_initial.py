import math
import sys
from time import perf_counter

# grid size
n = 10000

if __name__ == "__main__":

      starttime = perf_counter()

      global integral;
      # interval size (same for X and Y)
      h = math.pi / float(n)
      # cummulative variable
      mysum = 0.0

      # regular integration in the X axis
      for i in range(n):
         x = h * (i + 0.5)
         # regular integration in the Y axis
         for j in range(n):
            y = h * (j + 0.5)
            mysum += math.sin(x + y)

      integral = h**2 * mysum

      print("Integral value is %e, Error is %e" % (integral, abs(integral - 0.0)))
      endtime = perf_counter()

      print("Time spent: %.2f sec" % (endtime-starttime))