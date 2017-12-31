
package core;


public class String_Split 
{
    
    public static void main(String[] args) 
    {
        String a="Anil,Bijay,Chandan";
        String b[]=a.split(",");
        System.out.println(b[1]);
        for(String val:b)
        System.out.println(val);
    }
}
