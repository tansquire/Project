
package oops;


public class Polymotphism_method_Overloading 
{
    public static void main(String[] args) 
    {
        Overloading obj=new Overloading();
        obj.Poly();
        obj.Poly(6);
        obj.Poly(0);
        
        
    }
    
}
class Overloading  //same function name, same class, diff parameter
{
    public void Poly(int i)
    {
        System.out.println("Inside Poly Int");
    }
    public void Poly(float i)
    {
        System.out.println("Inside Poly float");
    }
    public void Poly()
    {
        System.out.println("Inside Poly empty");
    }
}