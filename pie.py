import matplotlib.pyplot as plt
country = ['India','china','Japan','Australia', 'Russia']
pop = [1380004385 ,1439323776,126476461, 25499884, 145934462]
plt.pie(pop, labels=country, autopct='%1.1f%%', startangle=90,
 wedgeprops={"edgecolor":"1",'linewidth':1,
 'linestyle': 'solid'})
# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
# Display the graph onto the screen
plt.show()

