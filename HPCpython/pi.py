from time import perf_counter

def calc_pi(num_steps):
      step = 1.0 / num_steps
      red_sum = 0.0
      for j in range(num_steps):
            x = ((j-1) - 0.5) * step
            red_sum += 4.0 / (1.0 + x * x)

      pi = step * red_sum
      return pi

if __name__ == "__main__":

      starttime = perf_counter()
      integral = calc_pi(100000000)
      endtime = perf_counter()

      print("Pi value is %e " % integral)
      print("Time spent: %.2f sec" % (endtime-starttime))