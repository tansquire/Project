package oops;


public class Inharitance_SingleLevel 
{
    public static void main(String[] args)
    {

        
        AddSub obj1=new AddSub();
        obj1.x=2;
        obj1.y=3;
        obj1.sum();
        System.out.println(obj1.z);
        obj1.sub();
        System.out.println(obj1.z);
        
    }
    
}
class Add1
{
    int x,y,z;
    public void sum() 
    {
        z=x+y;
        
    }
    
}
class AddSub1 extends Add1
{

    
    public void sub() 
    {
        z=x-y;
        
    }
    
}
