import matplotlib.pyplot as plt   #the plt is a shorten name that we created for easy reference.


# num_students = [38, 25, 32, 7]
# majors = ['CS', 'Mathematics', 'Engineering', 'Literature']
#
# line1 = plt.plot(majors, num_students)
#
# plt.show()


#Practice:
#Create two lists of your own and then plot them.


# stocks = ["F", "APPL", "TSLA", "OSG", "STI", "NKGN"]
# prices = [11.85, 216.67, 187.44, 8.48, 2.03, 1.29]
#
#
# fig, ax = plt.subplots()
# ax.set_title("Stocks and Prices")
# line2 = plt.plot(stocks, prices, 'x', color = 'orange')
# #'o' turns the line into dots
# plt.show()



#line1 = plt.plot(majors, num_students,
                 # color = 'green',
                 # linestyle = ':',
                 # marker = 's',
                 # linewidth = 5,
                 # )

#Exercise:

import matplotlib.pyplot as plt
from matplotlib import style

num_students = [38, 25, 32, 7]
num_women = [18, 18, 10, 5]
num_men = [20, 7, 22, 2]
majors = ['CS', 'Mathematics', 'Engineering', 'Literature']

style.use ('ggplot')
#print (style.available)

line1 = plt.plot(majors, num_students,
                 color = 'green',
                 linestyle = 'dashed',
                 marker = 's',
                 linewidth = 3,
                 label = 'Total Number'
                 )
line2 = plt.plot(majors, num_women,
                 color = 'red',
                 linestyle = '-',
                 marker = 'o',
                 linewidth = 2,
                 label = 'Women'
                 )

line3 = plt.plot(majors, num_men,
                 color = 'black',
                 linestyle = ':',
                 marker = 'v',
                 linewidth = 2,
                 label = 'Men'
                 )

plt.xlabel ('Majors')
plt.ylabel ("Number of students")
plt.title ('Majors vs Number of students')
plt.legend()
plt.show()