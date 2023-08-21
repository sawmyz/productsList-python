import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="" ,
  database="productslist"

)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price VARCHAR(255))")

# def info() :
#     name = input("send productName :")
#     price = input("send productsPrice :") 
#     return name , price

def add_product(name , price) :

      sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
      val = (name, price)
      mycursor.execute(sql, val)
      mydb.commit()
      print("add seccesfully :")

def remove_product(name) :
      sql = "DELETE FROM products WHERE name = %s"
      val = (name,)
      mycursor.execute(sql, val)
      mydb.commit()


def show_product() :
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM products")
    myresult = mycursor.fetchall()
    for final in myresult :
      print (final)


def update_product(new_name ,new_price,name) :

    sql = "UPDATE products SET name = %s , price = %s WHERE name = %s"
    val = (new_name,new_price, name)
    mycursor.execute(sql, val)

    mydb.commit()

while True :
    print ("1.Add")
    print ("2.Remove")
    print ("3.Show")
    print ("4.Change")    

    choice = int(input("choose a numbr for resume :"))
# add product
    if choice == 1 :
    #   name , price = info() 
      name = input("send productName :")
      price = input("send price :")
      add_product(name , price)
      print("added succesfully")
#remove product
    elif choice == 2:
      name = input("send productName :")
      remove_product(name)
      print("removed seccesfully :")
#show all products
    elif choice == 3 :
      show_product()
#update name and price
    elif choice == 4 :
        name = input("send productName :")
        new_name = input("send NEW  productName :")
        new_price = input("send NEW  price :")

        update_product(new_name,new_price , name)

        print("updated seccesfully :")


    else :
      pass
