
package core;

public class Exeption1
{
    public static void main(String[] args) 
    {
        int i=5;
        int j=0;
        int k=0;
        try
        {
            k=i/j;
        }
        catch(ArithmeticException e)
        {
            System.out.println("Cant devide by 0");
        }
    }
    
}
