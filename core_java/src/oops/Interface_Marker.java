
package oops;

public class Interface_Marker 
{
    public static void main(String[] args)
    {
        Mark1 obj = new Mark1();
        if(obj instanceof Mark)
        System.out.println("Permission Given");
        else
        System.out.println("Not permitted");
        
    }
    
}
interface Mark  //no method inside
{
}
class Mark1 implements Mark  //output wil be not permitted, if not implemented
{
    void show()
    {
        System.out.println("Hi");
    }
}