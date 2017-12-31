
package core;
import java.util.Scanner;


public class UserInput 
{
    public static void main(String[] args) 
    {
       String s;
       int j;
       int i;
       Scanner obj=new Scanner(System.in);
       System.out.println("Enter any Number");
       s=obj.nextLine();
       j=Integer.parseInt(s);
       System.out.println(j);
       System.out.println("Enter any String");
       s=obj.nextLine();
       System.out.println(s);
       System.out.println("Enter any Number");
       i=obj.nextInt();
       System.out.println(i);
       
    }
    
}
