import matplotlib.pyplot as plt


manzanas = [1000,1,245,30]
nombres = ["finn","Juan","jose","Catalina"]
plt.pie(manzanas, labels=nombres, autopct="%0.1f %%")
colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
desfase = (0, 0, 0, 0.1)
plt.pie(manzanas, labels=nombres, autopct="%0.1f %%", colors=colores, explode=desfase)
plt.axis("equal")
plt.show()

plt.pie(manzanas, labels=nombres)
'''
fig, ax = plt.subplots()

frutis = ['apple','blueberry','cherry', 'orange', 'banana']
counts = [40, 100, 30, 55, 25]

ax.bar(frutis, counts, color="red")

ax.set_ylabel('cantidad de frutas')
ax.set_xlabel("frutas")
ax.set_title('stock frutas ')
'''

plt.show()
