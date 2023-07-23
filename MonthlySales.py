# Program description: this is a program to enter the total amount of sales for each month from Jan to Dec.

# Import libraries
from matplotlib import pyplot as plt
from matplotlib import style


# Graph
style.use('ggplot')

x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
y = []

for month in x:
    MonthlySales = float(input(f"Enter the monthly sales for {month}: $"))
    y.append(MonthlySales)

fig, ax = plt.subplots()

ax.bar(x, y, align='center')

ax.set_title('Total Sales JAN-DEC')
ax.set_ylabel('Monthly Sales ($)')
ax.set_xlabel('Month')

ax.set_xticks(x)
ax.set_xticklabels(("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"))

plt.show()
