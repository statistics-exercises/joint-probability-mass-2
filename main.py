import matplotlib.pyplot as plt
import numpy as np 

def gen_sample( xvals, yvals, jpmass  ) : 
  # Your code to generate the pair of random variables goes here
  


# You shouldn't need to change any of the code from here onwards.  This will plot your graph 
# of how the two means change as you take more samples 
xvals, yvals = np.array([0,1,2]), np.array([1,2,4])
jpmass = np.array([[0.1,0.1,0],[0.2,0.1,0.1],[0,0.2,0.2]])
xsum, ysum, xax, xmeans, ymeans = 0, 0, np.zeros(100), np.zeros(100), np.zeros(100)
for i in range(100) : 
  xv, yv = gen_sample( xvals, yvals, jpmass )
  xsum, ysum = xsum + xv, ysum + yv 
  xax[i] = i+1 
  xmeans[i] = xsum / xax[i] 
  ymeans[i] = ysum / xax[i] 
  
plt.plot( xax, xmeans, 'ko' )
plt.plot( xax, ymeans, 'ro' )
plt.savefig("means.png")
