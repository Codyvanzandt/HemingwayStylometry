import matplotlib.pylab as plt
import pandas

frequencyDF = pandas.read_csv("data/hemingway_and_turgenev_frequency.csv")

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('Word Frequencies', fontsize = 20)

targets = ["Turgenev's Works", "Hemingway's Prior Works", "The Sun Also Rises" ]
colors = ['#11CCCC', '#404040', '#FFB215']
for target, color in zip(targets,colors):
    indicesToKeep = frequencyDF['target'] == target
    ax.scatter(frequencyDF.loc[indicesToKeep, 'Principal Component 1']
               , frequencyDF.loc[indicesToKeep, 'Principal Component 2']
               , c = color
               , s = 50)

ax.legend(targets)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.show()
