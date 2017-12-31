
package oops;


public class Before_Abstruction 
{
    public static void main(String[] args) 
    {
        Andriod obj1=new Andriod();
        Iphone obj2=new Iphone();
        showA(obj1);
       // show(obj2); error becoz showA can receive Iphone object
        showI(obj2); //After creation of ShowI function, obj2 can be passed.
        
        
    }
    public static void showA(Andriod object)
    {
        object.ShowConfig();
    }
    
    public static void showI(Iphone object) //created to accept Iphone object
    {
        object.ShowConfig();
    }
    
    
}
class Andriod
{
    public void ShowConfig()
    {
        System.out.println("Andriod feature");
    }
}
class Iphone
{
    public void ShowConfig()  
    {
        System.out.println("Iphone feature");
    }
}