
package core;


public class If_Else
{
    public static void main(String[] args)
    {
        int a=34;
        int b=4;
        int c=13;
        if(a>b &&a>c)System.out.println("Max is a");
        else if(b>c)
        System.out.println("Max is b");
        else
        System.out.println("Max is c");
        if(a%2==0||b%2==0 ||c%2==0)
        System.out.println("At least one no is even");
        
    }
    
}
