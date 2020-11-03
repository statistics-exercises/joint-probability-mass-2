import unittest
import scipy.stats
from main import *

class UnitTests(unittest.TestCase) :
      def test_mean(self) :
          xmean, xvar, ymean, yvar = 0, 0, 0, 0 
          for i in range(len(xvals)) : 
             for j in range(len(yvals)) : 
                 xmean = xmean + xvals[i]*jpmass[j,i]
                 xvar = xvar + xvals[i]*xvals[i]*jpmass[j,i]
                 ymean = ymean + yvals[j]*jpmass[j,i]
                 yvar = yvar + yvals[j]*yvals[j]*jpmass[j,i]

          exmean, eymean = 0, 0
          for i in range(100) :
              x, y = gen_sample( xvals, yvals, jpmass )
              exmean, eymean = exmean + x, eymean + y 

          xbar = np.sqrt( xvar / 100)*scipy.stats.norm.ppf((0.99+1)/2)
          self.assertTrue( np.abs( exmean/100 - xmean )<xbar, "Your function for generating samples does not appear to be working" )
          ybar = np.sqrt( yvar / 100)*scipy.stats.norm.ppf((0.99+1)/2)
          self.assertTrue( np.abs( eymean/100 - ymean )<ybar, "Your function for generating samples does not appear to be working" )
