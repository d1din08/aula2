#pip install -r requerimentis.txt
#abri grafico regressao linearpipi
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

PATH="./dados/values.txt"
df=pd.read_csv(PATH)

data=df.values
x,y=data[:,0],data[:,1]

calc=x*2+3

plt.figure()
plt.plot(x,y, color="red", linewidth=3)
plt.plot(x,calc, color="blue")
# plt.boxplot(x,y, color="red")

plt.xticks(np.arange(1,8,0.5))
# plt.yticks(np.arange(1,8,0.5))

plt.title("projeto 01", fontdict={"weight":"bold"})

plt.xlabel("variavel X")
plt.ylabel("variavel Y")



plt.savefig("grafico_a.png")



