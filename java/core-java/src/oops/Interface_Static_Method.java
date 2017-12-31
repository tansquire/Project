
package oops;


public class Interface_Static_Method
{
    public static void main(String[] args) 
    {
        Test.dis();
        
    }
    
}
interface Test   //new java 8 feature
{
     static void dis()
    {
        System.out.println("Hi");
    }
}