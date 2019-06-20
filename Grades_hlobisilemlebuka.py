
import numpy as np

number = float(input("Please enter a score between 0.00 and 1.0: " ))
if number == None:
    if number not in np.arange(0.0,1.0,0.1):
        raise Exception("input must not be null/must be in range( 0.00 - 1.00)")
  

elif number >= 0.9:
    print("A")
elif number >= 0.8:
    print("B")
elif number >= 0.7:
    print("C")
elif number >= 0.6:
    print("D")
elif number >= 0.5:
    print("E")
else:
    print("F")
    

    

        