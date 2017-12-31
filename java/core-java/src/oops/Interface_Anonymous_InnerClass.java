
package oops;


public class Interface_Anonymous_InnerClass //java 8 feature
{
    public static void main(String[] args) 
    {
        I3 obj =new I3() //First creat object, then define, then define method
       {
           public void show()  
           {
               System.out.println("HI");
           }
       };
        obj.show();
        
    }
    
}
interface I3
{
    void show();
}