
package core;


public class binary 
{
    public static void main(String[] args) 
    {
        int a=15;
        int b=16;
        boolean c =true;
        boolean d=!c;
        int e=a&b;
        int f=a|b;
        a=a>>2;   //right shift
        b=b<<2;   //left shift
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(f);
        
        
    }
    
}
