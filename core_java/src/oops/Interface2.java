package oops;


public class Interface2
{
    public static void main(String[] args) 
    {
        AI1 obj1=new AI1();
        obj1.show();
        obj1.display();
        obj1.hello();
        
        
    }
    
}
interface I1
{
    void show();
}
interface I2
{
    void display();
}
class AI1 implements I1,I2  //Like multiple inharitance
{
     public void show()
    {
        System.out.println("show");
    }
     public void display()
    {
        System.out.println("diaplay");
    }
     public void hello()
    {
        System.out.println("hello");
    }
    
}
