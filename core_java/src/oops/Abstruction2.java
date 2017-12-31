
package oops;

public class Abstruction2 
{
    public static void main(String[] args) 
    {
       // Mobile obj=new Mobile();  //error: object cant be created
       // Mobile1 obj1=new Mobile1();  //error: object cant be created
        Mobile2 obj2=new Mobile2();  //It is possible to create object
        obj2.call();
        obj2.camera();
        
    }
    
}
abstract class Mobile
{
    public abstract void call();
    public abstract void sms();
    public abstract void camera();
}
abstract class Mobile1 extends Mobile
{
    public  void call()
    {
        System.out.println("call function created");
    }
    
    
}
 class Mobile2 extends Mobile1
{
    public  void sms()
    {
        System.out.println("sms function created");
    }
    public  void camera()
    {
        System.out.println("camera function created");
    }
    
    
}