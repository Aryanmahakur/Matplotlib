import numpy as np
import matplotlib.pyplot as plt

#scatter plot
# x=np.random.rand(50)*100
# y=np.random.rand(50)*100
# plt.scatter(x,y,c="yellow",marker="o",s=105,alpha=0.5)
# plt.show()

#line plot
# years = [2005 + x for x in range(10)]
# weights = [10, 20, 30, 40, 15, 60, 70, 80, 90, 100]
# plt.plot(years, weights,c="yellow",marker="o",ms=10,ls="dashed",lw=2)
# plt.xlabel("Years")
# plt.ylabel("Weights")
# plt.title("Yearly Weight Progression")
# plt.show()

#bar plot
# x=["c++","c","java","python"]
# y=[10,20,10,40]
# plt.bar(x,y,color="yellow",align="center",width=0.5,edgecolor="red",lw=2)
# plt.show()

#histogram
# ages = np.random.normal(30, 5, 1000)
# # plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()], color="yellow", edgecolor="red", lw=2)
# # plt.show()
# plt.hist(ages, bins=10, color="yellow", edgecolor="red", lw=2,cumulative=True)
# plt.show()

#pie chart
# langs=["c++","c","java","python"]
# votes=[10,20,10,50]
# explode=[0,0,0,0.1]
# plt.pie(votes,labels=langs,explode=explode,autopct="%1.1f%%",shadow=True,pctdistance=5,colors=["yellow","red","green","blue"],startangle=90)
# plt.show()

#boxplot
# height=np.random.normal(172,8,300)
# plt.boxplot(height)
# plt.show()
# first=np.linspace(0,10,25)
# second=np.linspace(100,200,25)
# third=np.linspace(0,3000,25)
# fourth=np.linspace(0,400,25)
# data=np.concatenate((first,second,third,fourth))
# plt.boxplot(data)
# plt.show()

#customization
years=[2010,2011,2012,2014,2015]
income=[50,60,50,80,70]
income_ticks=list(range(50_81_2))
plt.plot(years,income,)
plt.title("income of a person(in usd)",fontsize=30,fontname="freeserif")
plt.xlabel("year")
plt.ylabel("income(in usd)")
plt.yticks(income_ticks,[f"{x}k USD" for x in income_ticks])
plt.show()