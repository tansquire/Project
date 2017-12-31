package oops;


public class Interface_Override
{
    public static void main(String[] args) 
    {
        A6 obj =new A6();
        obj.show();
        
        
    }
    
}
interface Def1
{
    default void show()
    {
        System.out.println("def1");
    }
}
interface Def2
{
    default void show()
    {
        System.out.println("def2");
    }
}
class A6 implements Def1,Def2
{
    public void show()
    {
        System.out.println("override");
    }
    
}
