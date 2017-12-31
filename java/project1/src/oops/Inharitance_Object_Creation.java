
package oops;


public class Inharitance_Object_Creation 
{
    public static void main(String[] args) 
    {
        A1 obj1=new A1();
        //A1 obj2=new A1(5);
        //A1 obj3=new B1(); //parent default cons will also be called
        //A1 obj4=new B1(5); //parent default cons will also be called
        
    }
    
}
class A1
{
     A1()
     {
         System.out.println("Inside parent default constructor");
     }
     
     A1(int x)
     {
         System.out.println("Inside parent parameter constructor");
     }
}
class B1 extends A1
{
    B1()
     {
         System.out.println("Inside child default constructor");
     }
     
     B1(int x)
     {
         System.out.println("Inside child parameter constructor");
     }
}
