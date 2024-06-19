import matplotlib.pyplot as plt
from matplotlib import style


num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

style.use ('ggplot')
#print (style.available)

fig1 = plt.figure('My Figure') #Title your figure

#create a subplot comprising of 3 rows, 2 columns and this is the first subplot in this grid
plt.subplot(3,2,1)
plt.plot(majors, num_students,
                 color = 'green',
                 linestyle = 'dashed',
                 marker = 's',
                 linewidth = 3,
                 label = 'Total'
                 )
plt.legend()
plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.title ('Majors vs Number of students')
#create a subplot comprising of 3 rows, 1 column and this is the second subplot
plt.subplot(322)
plt.plot(majors, num_women,
                 color = 'red',
                 linestyle = '-',
                 marker = 'o',
                 linewidth = 2,
                 label = 'Women'
                 )

plt.xlabel ('Majors')
plt.ylabel ("Female students")
#plt.title ('Majors vs Number of women')
plt.legend()

#create a subplot comprising of 3 rows, 1 column and this is the third subplot
plt.subplot(3,2,3)
plt.plot(majors, num_men,
                 color = 'yellow',
                 linestyle = '-',
                 marker = 'v',
                 linewidth = 2,
                 label = 'Men'
                 )
plt.legend()
plt.xlabel ('Majors')
plt.ylabel ("Male students")

plt.subplot(3,2,4)
plt.plot(majors, num_men,
                 color = 'blue',
                 linestyle = '-',
                 marker = 'o',
                 linewidth = 2,
                 label = 'Men'
                 )
plt.legend()
plt.xlabel ('Majors')
plt.ylabel ("Male students")


plt.subplot(3,2,5)
plt.plot(majors, num_women,
                 color = 'cyan',
                 linestyle = '-',
                 marker = 'D',
                 linewidth = 2,
                 label = 'Women'
                 )

plt.xlabel ('Majors')
plt.ylabel ("Female students")
plt.legend()


plt.subplot(3,2,6)
plt.plot(majors, num_students,
                 color = 'orange',
                 linestyle = '-',
                 marker = 'd',
                 linewidth = 3,
                 label = 'Total'
                 )
plt.legend()
plt.xlabel ('Majors')
plt.ylabel ("Number of students")
#plt.title ('Majors vs Number of students')

plt.show()




Now using numpy library:

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

x = np.arange(len(majors))
print (x)

style.use ('ggplot')

plt.bar(x, num_students, label = 'total')
plt.bar(x, num_men, label = 'men')
plt.bar(x, num_women, label = 'women')

#horizontal bar chart
plt.barh(x, num_students, label = 'total')
plt.barh(x, num_women, label = 'women')


plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.xticks(x, majors)
plt.title ('Majors vs Number of students')
plt.legend()
plt.show()



#Unstacked barchart

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

x = np.arange(len(majors))

style.use ('ggplot')
#by default matplotlib.pyplot has a width of 0.8
width = .25
#yerr = (38 25 32 7)

plt.bar(x, num_students, width,  label = 'total' )

for i in x:
    plt.annotate( str(num_students[i]) ,  (x[i],num_students[i]) )


plt.bar(x+.25, num_men, width, label = 'men')
plt.bar(x+.5, num_women, width, label = 'women')

plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.xticks(x+.25, majors)
plt.title ('Majors vs Number of students')
plt.legend()
plt.show()

