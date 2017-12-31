
package oops;


public class Interface1
{
    public static void main(String[] args) 
    {
        AI obj1=new AI();
        I obj2=new AI();
        obj1.show();
        obj1.display();
        obj2.show();
        //obj2.display();  error, cant be done
        //Same concept for abstract class also
        
        
    }
    
}
interface I
{
    void show();
}
class AI implements I
{
     public void show()
    {
        System.out.println("show");
    }
     void display()
    {
        System.out.println("diaplay");
    }
    
}