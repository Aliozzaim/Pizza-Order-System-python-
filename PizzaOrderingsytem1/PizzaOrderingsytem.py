
urunler = ['','Klasik','Margherita',"Pepperoni" ,'Gennaro']
sepetim = [ {   }   
                                          ]
sub_total = []
final_order = {}
customer_adress = {}

class pizza:
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost

  def __str__(self):
    return f"{self.name}({self.cost})"

while True:  
    print("\n Hi, welcome to our text based pizza ordering system-_=\n\n Currently our available products are Listed Below....\n\n1: Klasik 10$ 2: Margherita 15$ 3: Pepperoni 20$ 4: Gennaro 25$\n\n Available sauces...\n 5: Zeytin 5$ 6:Manta 3$ 7:Et :Misir 1$ 9:Keçi peyniri 5$ \n Which pizza would you like to order? Number(1/2/3/4)\n")
    
    get_order = int (input())
    if  get_order == 1 :
       
       p1 = pizza(urunler[get_order] ,10)
       print(f"You have ordered a {p1}.")
       sepetim.append(p1)
    elif get_order == 2 :
       
       p2 = pizza(urunler[get_order] ,20)

       print(f"You have ordered a {p2}.")
       sepetim.append(p2)
    
    elif get_order == 3 :
       
       p3 = pizza(urunler[get_order] ,20)
       print(f"You have ordered a {p3}.")
       sepetim.append(p3)
    
    elif get_order == 4 :
       
       p4 = pizza(urunler[get_order] ,20)
       print(f"You have ordered a {p4}.")
       sepetim.append(p4)
       

    else  : print(f"I am sorry, There is No {get_order}th Option.")


