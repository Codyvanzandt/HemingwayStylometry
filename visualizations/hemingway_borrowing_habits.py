import xml_utilities
import pandas
import datetime
import collections
import matplotlib.pylab as plt
import seaborn as sns


###################################################
# Creating a series of borrowing events per month #
###################################################
hemingwayDF = xml_utilities.makeBorrowingDataFrame("data/hemingway.tei.xml")

hemingwayDF = hemingwayDF[ (hemingwayDF.Title != str()) & hemingwayDF["DateBorrowed"].notnull() ]

hemingwayDF.reset_index().set_index('DateBorrowed')
hemingwayDF.set_index('DateBorrowed')

borrowedByMonth = hemingwayDF['DateBorrowed'].groupby(hemingwayDF.DateBorrowed.dt.to_period("M")).agg('count')

#########################################################################
# Adding missing months, cutting out the very sparse years from 1929-33 #
#########################################################################

startDate = "1925-10"
endDate = "1928-04"
borrowedByMonth = borrowedByMonth.loc[startDate : endDate]
idx = pandas.date_range(startDate, endDate, freq='M').to_period('m')
borrowedByMonth = borrowedByMonth.reindex(idx, fill_value=0)
borrowedByMonth.index = borrowedByMonth.index.strftime('%b%y')

######################################
# Creating and formatting a bar plot #
######################################

fig = sns.barplot(x=borrowedByMonth.index, y=borrowedByMonth.values, color="#11CCCC")

fig.set_title("Hemingway: Books Borrowed from Shakespeare and Company", fontsize=16)
fig.set(ylabel='Amount')

fig.set_xticklabels(fig.get_xticklabels(), rotation=90)

fig.spines['left'].set_position(("outward", 20))

fig.spines['right'].set_visible(False)
fig.spines['top'].set_visible(False)
fig.spines['left'].set_visible(False)
fig.spines['bottom'].set_visible(False)

fig.tick_params(axis=u'x', which=u'both',length=0)

fig.annotate("Data source: mep.princeton.edu", (0,0), (-112, -40), xycoords='axes fraction', textcoords='offset points', va='top')

plt.show()
