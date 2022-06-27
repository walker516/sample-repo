import matplotlib.pyplot as plt
labels = ['steady', 'not-steady', 'maintenance']
group = [0.5, 0.45, 0.05]
details = [35, 5, 5, 5, 45, 5]
# Create colors
a, b, c=[plt.cm.YlOrRd, plt.cm.gray, plt.cm.binary]
textprops = {'fontsize':10,'color':'black'}
 
bigger = plt.pie(group, labels=labels, colors=[a(0.6), b(0.6), c(0.6)],
                 startangle=90, frame=True, )
smaller = plt.pie(details,  autopct='%.1f%%', pctdistance =0.85,
                  colors=[a(0.5), a(0.4), a(0.3), a(0.2), b(0.6), c(0.6)], radius=0.9,
                  startangle=90, labeldistance=0.7, textprops =textprops)
centre_circle = plt.Circle((0, 0), 0.4, color='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
        
plt.axis('equal')
plt.tight_layout()

plt.show()
