
package oops;


public class Interface_Defination_Inside 
{
    public static void main(String[] args) 
    {
        A5 obj =new A5();
        obj.show();
        
        
    }
    
}
interface Def
{
    default void show()
    {
        System.out.println("HI");  //new java 8 feature
    }
}
class A5 implements Def
{
}