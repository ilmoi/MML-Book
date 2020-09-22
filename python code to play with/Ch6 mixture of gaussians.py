import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

##SIMPLIFIED VERSION - 50/50
#x dimensions
#g1_x = np.random.normal(loc=10,scale=1,size=10000)
#g2_x = np.random.normal(loc=0,scale=8.4,size=10000)
#
##their mixture in x dimension
#mixture_x = np.concatenate((g1_x,g2_x))
#bins = np.linspace(-50,50, 100)
#mixture_x_binned_for_mode = np.digitize(mixture_x, bins)-50
#fig, ax1 = plt.subplots()
#ax1.set(title="x dimension marginal")
#ax1.hist(mixture_x, bins=100)
#ax1.hist(mixture_x_binned_for_mode, bins=100)
#
##statistics for x dimension
#mode_x = stats.mode(mixture_x_binned_for_mode)[0] #need to bin first, otherwise most common value is useless
#mean_x = np.average(mixture_x)
#median_x = np.median(mixture_x)



##y dimensions
#g1_y = np.random.normal(loc=2,scale=1,size=10000)
#g2_y = np.random.normal(loc=0,scale=1.7,size=10000)
#
##their mixture in y dimension
#mixture_y = np.concatenate((g1_y,g2_y))
#bins = np.linspace(-50,50, 100)
#mixture_y_binned_for_mode = np.digitize(mixture_y, bins)-50
#fig, ax2 = plt.subplots()
#ax2.set(title="y dimension marginal")
#ax2.hist(mixture_y, bins=100)
#ax2.hist(mixture_y_binned_for_mode, bins=100)
#
##statistics for y dimension
#mode_y = stats.mode(mixture_y_binned_for_mode)[0] #need to bin first, otherwise most common value is useless
#mean_y = np.average(mixture_y)
#median_y = np.median(mixture_y)
#
#
###multivar
#x = np.concatenate((g1_x,g2_x)) #so I'm simplifying here - I'm sort of saying 50/50 each distribution, while in the exercise they actually had 40/60
#y = np.concatenate((g1_y,g2_y))
#
#fig, ax3 = plt.subplots()
#ax3.set(title="scatter in 2d")
#ax3.scatter(x,y) 
#
#fig, ax4 = plt.subplots()
#ax4.set(title="joint histogram")
#ax4.hist2d(x,y, bins=100)

#ACTUAL VERSION - 40/60
g1_x = np.random.normal(loc=10,scale=1,size=10000)
g2_x = np.random.normal(loc=0,scale=8.4,size=10000)
g1_y = np.random.normal(loc=2,scale=1,size=10000)
g2_y = np.random.normal(loc=0,scale=1.7,size=10000)

#mean_1_x = 10
#mean_2_x = 0
#var_1_x = 1
#var_2_x = 8.4
#mix_1_x = 0.4
#mix_2_x = 1- mix_1_x
#
#mixture_mean_x = mix_1_x*mean_1_x + mix_2_x*mean_2_x
#mixture_variance_x = (mix_1_x*var_1_x + mix_2_x*var_2_x) + ((mix_1_x*mean_1_x**2 + mix_2_x*mean_2_x**2) - (mix_1_x*mean_1_x + mix_2_x*mean_2_x)**2)

#BELOW IS WRONG, ASSUMES THE RESULT IS GAUSSIAN WHEN ITS NOT
#mixture_sampled_x = np.random.normal(loc=mixture_mean_x,scale=mixture_variance_x,size=10000)
#plt.hist(mixture_sampled_x)

#instead what you need to do is: 1)sample individually, 2)pick from each of distributions with probabilities p and q
x = np.zeros(10000)
indices = np.random.choice(2, size=10000, p=[0.4,0.6])
for i in range(len(indices)):
#    print(i)
#    print(indices[i])
#    print(g1_x[i])
    if indices[i] == 0:
        x[i] = g1_x[i]
#        print('done1')
    else:
        x[i] = g2_x[i]
#        print('done2')
plt.hist(x) #ok good so this works
# this is the answer to: a. Compute the marginal distributions for each dimension.

bins = np.linspace(-50,50, 100)
x_binned = np.digitize(x, bins)-50
mode_x = stats.mode(x_binned)[0] #works, 10, like expected
mean_x = np.average(x) #ok goood news is that this matches up with the mixture mean above
median_x = np.median(x) #yep I buy that median = 8
# this is the answer to b. Compute the mean, mode and median for each marginal distribution.

y = np.zeros(10000)
indices = np.random.choice(2, size=10000, p=[0.4,0.6])
for i in range(len(indices)):
    if indices[i] == 0:
        y[i] = g1_y[i]
    else:
        y[i] = g2_y[i]
plt.hist(y)
bins = np.linspace(-50,50, 100)
y_binned = np.digitize(y, bins)-50
mode_y = stats.mode(y_binned)[0] 
mean_y = np.average(y) 
median_y = np.median(y) 

mean_xy = [mean_x,mean_y]
mode_xy = [mode_x,mode_y]
# this is the answer to c. c. Compute the mean and mode for the two-dimensional distribution.
