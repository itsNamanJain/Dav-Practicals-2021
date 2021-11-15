import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris = pd.read_csv("iris.csv")
print(iris.shape)
print(iris.head(5))
iris.info()

# (a)


print("(a)",iris['variety'].value_counts())
sns.countplot(x='variety',data=iris)
plt.show()

# (b)

iris.plot(kind ="scatter",
          x ='sepal.width',
          y ='petal.width')
plt.show()

# (c)

sns.kdeplot(data=iris['petal.length'], shade=True)
plt.show()

# (d)

sns.set_style("ticks")
sns.pairplot(iris,hue = 'variety',diag_kind = "kde",kind = "scatter",palette = "husl")
plt.show()