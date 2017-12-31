
package oops;


public class This_Keyword 
{
    public static void main(String[] args) 
    {
        A4 obj=new A4(5);
        obj.show();
    }
    
}
class A4
{
    int i;
    A4(int i)
    {
        this.i=i;
    } 
    public void show()
    {
        System.out.println(i);
    }
}
