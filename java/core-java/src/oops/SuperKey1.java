
package oops;


public class SuperKey1 
{
    public static void main(String[] args) 
    {
        A2 obj1=new A2();
        A2 obj2=new A2(5);
        B2 obj3=new B2();
        B2 obj4=new B2(5);
        
        
    }
    
}
class A2
{
    A2()
    {
        System.out.println("Inside class A2");
    }        
    A2(int i)
    {
        System.out.println("Inside class A2 parameter");
    }  
}
class B2 extends A2
{
    B2()
    {
        super();
        System.out.println("Inside class B2");
    }        
    B2(int i)
    {   
        super(i); //parent class parameter constructor will get called
        //super(); //parent class default constructor will get called
        System.out.println("Inside class B2 parameter");
    }  
    
}