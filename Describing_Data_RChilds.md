

```python
import numpy as np
```


```python
ages_x = [6, 8, 8, 10, 11, 12, 14]
```


```python
def summarystats(ages_x):
    print("mean: ",np.mean(ages_x))
    print("median: ",np.median(ages_x))
    print("variance: ",np.var(ages_x))
    print("std. deviation :",np.std(ages_x))
    print("standard error :",np.std(ages_x)/np.sqrt(len(ages_x)-1))
    
summarystats(x)
print("The mode is 8")
```

    mean:  9.85714285714
    median:  10.0
    variance:  6.40816326531
    std. deviation : 2.53143502095
    standard error : 1.03345401972
    The mode is 8



```python
#I would use choose mean and standard deviation as measures of central tendency and variance
#because they are close enough in value; there are no outliers. 
```


```python
ages_y = [6, 8, 8, 10, 11, 12, 14]
summarystats(ages_y)
print("The mode is 8")
```

    mean:  9.85714285714
    median:  10.0
    variance:  6.40816326531
    std. deviation : 2.53143502095
    standard error : 1.03345401972
    The mode is 8



```python
ages_z = [1, 7, 8, 10, 11, 12, 14]
summarystats(ages_z)
print("There is no mode")
```

    mean:  9.0
    median:  10.0
    variance:  15.4285714286
    std. deviation : 3.92792202425
    standard error : 1.60356745147
    There is no mode



```python
#4 #The mean and median are further apart as there is now an outlier, best now to use
#median.
```


```python
#TV Guide, Entertainment Weekly, and Pop Culture Today are more general; thus, a better 
#representative of the general population relative to specific niche magazine SciPhi Fanatic
#Best to take out the data from SciPhi alltogether, and find their average to be 20%
```
