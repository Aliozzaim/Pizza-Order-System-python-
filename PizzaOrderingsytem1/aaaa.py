# class pizza:
#   def __init__(self, name, cost):
#     self.name = name
#     self.cost = cost

#   def __str__(self):
#     return f"{self.name}({self.cost})"
#urunler = ['','Klasik','Margherita',"Pepperoni" ,'Gennaro']
#Available sauces...\n 5: Zeytin 5$ 6:Manta 3$ 7:Et :Misir 1$ 9:Keçi peyniri 5$ \n

#print(f"You have ordered a {p1}.")
 #      sepetim.append(p1)
# 11: Zeytin
# 12: Mantarlar
# 13: Keçi Peyniri
# 14: Et
# 15: Soğan
# 16: Mısır
# * Teşekkür ederiz!

sub_total = []
sepetim = [{}]
final_order = {}
customer_adress = {}





class Pizza:
    def get_description(self):
        return self.__class__.__name__
    def get_cost(self):
        return (self.__class__.cost , self.goster ) 
 
class Klasik(Pizza): 
 cost=87
 goster= (f"Klasik Pizza içindekiler: domates, mozarella, fesleğen {cost}TL")  
  

class Margherita(Pizza):
    cost=87
    goster= (f"Klasik içindekiler: domates, mozarella, fesleğen {cost}TL")  
  
class Pepperoni(Pizza):
   cost=62
   goster= (f"Klasik içindekiler: domates, mozarella, fesleğen {cost}TL")  
   
class Decorator(Pizza):
   def _init_(self,pizza):
      self.pizza=pizza
      def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)
   def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self) 
   
class Zeytin(Decorator): 
   cost=6
   def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)
        
class Mantar(Decorator):
   cost=8
   def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class Et(Decorator):
   cost=35
   def __init__(self, Pizza):
        Decorator.__init__(self, Pizza) 

class Mısır(Decorator):            
  cost=16
  def __init__(self, Pizza):
     Decorator.__init__(self, Pizza) 

class Keçipeyniri(Decorator):            
  cost=12
  def __init__(self, Pizza):
     Decorator.__init__(self, Pizza)             

  


class Gennaro(Pizza):
  cost=84
  goster= (f"Klasik içindekiler: domates, mozarella, fesleğen {cost}TL")  




while True:  
    
    get_order = (input(("\n Hi, welcome to our text based pizza ordering system-_=\n\n Currently our available products are Listed Below....\n\n1: Klasik  2: Margherita  3: Pepperoni  4: Gennaro \n\n  Which pizza would you like to order? Number(1/2/3/4)\n")))
    if  get_order == '1' :
        p1=Klasik.goster
        print(p1)
        yesorno = input(f"Do you confirm the order klasik Pizza (Y/N)")
   
    
    elif get_order == '2' :
        print(Margherita.goster)
       
    
    elif get_order == '3' :
      
        print(Pepperoni.goster)
    
       
    elif get_order == '4' :
        print(Gennaro.goster)

    else  : print(f"I am sorry, There is No {get_order}th Option.")
    break

