package oops;


public class Inharitance_Multilevel 
{
    public static void main(String[] args)
    {

        
        Mul obj=new Mul();
        obj.x=2;
        obj.y=3;
        obj.sum();
        System.out.println(obj.z);
        obj.sub();
        System.out.println(obj.z);
        obj.multi();
        System.out.println(obj.z);
        
    }
    
}
class Add2
{
    int x,y,z;
    public void sum() 
    {
        z=x+y;
        
    }
    
}
class AddSub2 extends Add1
{

    
     public void sub() 
    {
        z=x-y;
        
    }
    
}
class Mul extends AddSub2
{

    
    public void multi() 
    {
        z=x*y;
        
    }
    
}