class Student: 

    # Constructor 

    def __init__(self, name, rollno, contactno, email): 

        self.name = name 

        self.rollno = rollno 

        self.contactno = contactno

        self.email = email

         

    # Function to create and append new student    

    def accept(self, Name, Rollno, contactno, email ): 

        # use  ' int(input()) ' method to take input from user 

        ob = Student(Name, Rollno, contactno, email) 

        ls.append(ob) 

  

    # Function to display student details      

    def display(self, ob): 

            print("Name   : ", ob.name) 

            print("RollNo : ", ob.rollno) 

            print("contactno: ", ob.contactno) 

            print("email: ", ob.email) 

            print("\n")     

         

    # Search Function     

    def search(self, rn): 

        for i in range(ls.__len__()): 

            if(ls[i].rollno == rn): 

                return i        

  

    # Delete Function                                   

    def delete(self, rn): 

        i = obj.search(rn)   

        del ls[i] 

  

    # Update Function    

    def update(self, rn, No): 

        i = obj.search(rn) 

        roll = No 

        ls[i].rollno = roll; 

         
# Create a list to add Students 

ls =[] 
# an object of Student class 

obj = Student('', 0, 0, 0) 

  

print("\nOperations used, ") 

print("\n1.Accept Student details\n2.Display Student Details\n" /

      / "3.Search Details of a Student\n4.Delete Details of Student" /

      / "\n5.Update Student Details\n6.Exit") 

  
# ch = int(input("Enter choice:")) 
# if(ch == 1): 

obj.accept("A", 1, 1234567890, poojithreddy@gmail.com) 

obj.accept("B", 2, 9000000000, poojithreddy2@gmail.com) 

obj.accept("C", 3, 8000000000, poojithreddy4@gmail.com) 

         
# elif(ch == 2): 

print("\n") 

print("\nList of Students\n") 

for i in range(ls.__len__()):     

    obj.display(ls[i]) 

             
# elif(ch == 3): 

print("\n Student Found, ") 

s = obj.search(2) 
obj.display(ls[s]) 

         
# elif(ch == 4): 

obj.delete(2) 

print(ls.__len__()) 

print("List after deletion") 

for i in range(ls.__len__()):     

    obj.display(ls[i]) 

             
# elif(ch == 5): 

obj.update(3, 2) 

print(ls.__len__()) 

print("List after updation") 

for i in range(ls.__len__()):     

    obj.display(ls[i]) 

             
# else: 

print("Thank You !") 
