
package Mixed;
import java.util.Scanner;

public class String_Operation 
{
    public static void main(String[] args)
    {
        String s1,s2,s3;
        Scanner obj=new Scanner(System.in);
        System.out.println("Enter an string");
        s1=obj.nextLine();
        System.out.println("Enter another string");
        s2=obj.nextLine();
        s3=s1.concat(s2);
        System.out.println(s3);
        s3=s1+s2;
        System.out.println(s3);
        s3=s1+" "+s2;
        System.out.println(s3);
        System.out.println("Length of s1 and s2 are "+s1.length()+" "+s2.length());
        s1=s1.toUpperCase();
        System.out.println(s1);  
        s2=s2.toLowerCase();
        System.out.println(s2);  
        
        
        
    }
    
}
