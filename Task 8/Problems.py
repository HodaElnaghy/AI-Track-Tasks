import numpy as np
#Task 1
L=np.eye(3)*9
print("Task One: ",L)

# task 2

a=np.arange(2,33,2)
a=np.reshape(a,(-1,4))
print(a)

#another solution
#a=np.empty((0,4),int)
#for i in range (0,32,8):
#    a=np.append(a,np.array([[i+2,i+4,i+6,i+8]]),axis=0)
mean_value=np.mean(a)
std_value= np.std(a)
minimum= int(mean_value-0.5*std_value)
maximum=int(mean_value+ 0.5*std_value)

F=np.extract((a>minimum),a)
F=np.extract((F<maximum),F)



print("Filtered: ",F)

#Task 3

y=np.zeros([9,9],int)
print("Task 3: ",y)


#Task 4
h=np.ones((4,4),int)
f=np.array([0,1,2,3])
h=f+h
print("Task 4: ",h)






