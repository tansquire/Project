package core;
import java.util.Scanner;

public class Exception4
{
    public static void main(String[] args) 
    {
        Scanner obj=new Scanner(System.in);
        System.out.println("Please enter j");
        int i=2;
        int j=obj.nextInt();
        int k=0;
        
        try
        {
            k=i+j;
            
            if(k<10)
            {
                throw new Exception();   //forcefull exception
            }
            System.out.println(k);
            
        }
        catch(Exception e)
        {
            System.out.println("Sum less than 10");
        }

        finally
        {
            obj.close(); //This is the rule of final block
            System.out.println("This is a common statement for both try and catch");
        }
    }
    
}
