import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as mc

conobj=mc.connect(host="localhost",user="root",password="Rapolu@2007",database="task7")
curobj=conobj.cursor()

curobj.execute("create table IF NOT EXISTS sales(product varchar(30),quantity int,price decimal(10,2));")


#inserting data into table,making it comment to avoid adding duplicate data again and again
'''
data = [("Laptop", 5, 60000),("Mouse", 20, 500),("Keyboard", 15, 1000),("Monitor", 8, 12000),("Headphones", 10, 1500)]
curobj.executemany("INSERT INTO sales(product,quantity,price) VALUES (%s, %s, %s)", data)
conobj.commit()
'''

query="select product,sum(quantity) as TotalQuantity,sum(quantity*price) as Revenue from sales group by product;"
curobj.execute(query)

result=curobj.fetchall()

columns=["product","TotalQuantity","Revenue"]
df=pd.DataFrame(result,columns=columns)

print("sales summary:")
print(df)

plt.bar(df['product'], df['Revenue'], color='skyblue')
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.title("Revenue by Product (from MySQL)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

curobj.close()
conobj.close()
