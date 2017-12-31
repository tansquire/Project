package oops;


public class Abstruction1 
{
    public static void main(String[] args) 
    {
        Phone obj1=new Andriod1();
        Iphone1 obj2=new Iphone1();
        show(obj1);
        show(obj2);  //one function show is enough to accept both object
        //Now all objects have same types, i.e. parents types phone.
        
        
    }
    public static void show(Phone object)
    {
        object.ShowConfig();
    }
    
    
    
    
}
class Andriod1 extends Phone
{
    public void ShowConfig()
    {
        System.out.println("Andriod feature");
    }
}
class Iphone1 extends Phone
{
    public void ShowConfig()  
    {
        System.out.println("Iphone feature");
    }
}
abstract class Phone
{
    public abstract void ShowConfig();
    
}