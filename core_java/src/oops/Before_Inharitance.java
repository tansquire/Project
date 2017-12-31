
package oops;


public class Before_Inharitance 
{
    public static void main(String[] args)
    {
        Add obj=new Add();
        obj.x=2;
        obj.y=3;
        obj.sum();
        System.out.println(obj.z);
        
        AddSub obj1=new AddSub();
        obj1.x=2;
        obj1.y=3;
        obj1.sub();
        System.out.println(obj1.z);
        
    }
    
}
class Add
{
    int x,y,z;
    public void sum() 
    {
        z=x+y;
        
    }
    
}
class AddSub
{
    int x,y,z;
    public void sum() 
    {
        z=x+y;
        
    }
    
    public void sub() 
    {
        z=x-y;
        
    }
    
}
