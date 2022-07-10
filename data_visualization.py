"""
DECIS Data Scientist test

@author: wb545671
"""
"""""""""
Figure 1
"""""""""
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 15})
import matplotlib.ticker as mtick
from matplotlib.ticker import FormatStrFormatter

data1 = pd.read_csv('https://raw.githubusercontent.com/hwwbg/DECIS-DataScientist/main/datavisual.csv')
df1 = pd.DataFrame(data1)

fig, ax = plt.subplots(figsize =(16, 9))
ax.barh(df1['countrycode'], df1['diff'])
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)

ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

ax.invert_yaxis()

for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontweight ='bold',
             color ='grey')
 
ax.set_title(r'$\bf{Figure 1.}$ Possible difference in inflation rate between btm 20% and top 20% if food inflation grows twice faster', loc ='center', fontsize=18 )
plt.annotate('Source: Authors’ calculations using the database of MPOs for the 2022 Spring Meeting', 
             xy = (0, -0.1),
            xycoords='axes fraction',
            ha='left',
            va="center",
            fontsize=12)

plt.show()
"""""""""
Figure 2
"""""""""
data2 = pd.read_csv('https://raw.githubusercontent.com/hwwbg/DECIS-DataScientist/main/datavisual1.csv')
df2 = pd.DataFrame(data2)

fig, ax = plt.subplots(figsize=(16,9))
ax.set_title(r'$\bf{Figure 2.}$ Poverty trends in East and South Africa under three scenarios', fontsize=18,  loc ='center',)

ax.plot(df2['year'], df2['food>nonfood'],label='food>nonfood')
ax.plot(df2['year'], df2['food<nonfood'],label='food<nonfood')
ax.plot(df2['year'], df2['food=nonfood'],label='food=nonfood')
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))

for x,y in zip(df2['year'],df2['food>nonfood']):

    #label = "{:.1f}".format(y)
    label = str(round(y*100,2)) + '%' 

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x,y in zip(df2['year'],df2['food<nonfood']):

    #label = "{:.1f}".format(y)
    label = str(round(y*100,2)) + '%' 

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x,y in zip(df2['year'],df2['food=nonfood']):

    #label = "{:.1f}".format(y)
    label = str(round(y*100,2)) + '%' 

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15),ncol=3,frameon=False)    
plt.annotate('Source: Authors’ calculations using the database of MPOs for the 2022 Spring Meeting', 
             xy = (0, -0.2),
            xycoords='axes fraction',
            ha='left',
            va="center",
            fontsize=12)
ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
plt.show()
