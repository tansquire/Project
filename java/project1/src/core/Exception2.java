
package core;
import java.util.Scanner;

public class Exception2
{
    public static void main(String[] args) 
    {
        Scanner obj=new Scanner(System.in);
        System.out.println("Please enter j");
        int i=2000;
        int j=obj.nextInt();
        int k=0;
        int a[]={1,2,3};
        try
        {
            k=i/j;
            System.out.println(k);
            for(int x=0;x<=3;x++)
            System.out.println(a[x]);
        }
        catch(ArithmeticException e)
        {
            System.out.println("Cant devide by 0");
        }
//        catch(ArrayIndexOutOfBoundsException e)
//        {
//            System.out.println("Index out of bound");
//        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
    
}
