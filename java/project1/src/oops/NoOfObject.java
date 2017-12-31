
package oops;

public class NoOfObject 
{
    public static void main(String[] args)
    {
        
            A obj1=new A();
            A obj2=new A();
            A obj3=new A();
            A obj4=new A();
            System.out.println(A.i);
            System.out.println(obj4.j);
            
        
    }
    
}
class A
{
    int j =0;
    static int i=0;//If static is not given, ans=1
    A()           //If static is not given, for each object i=0
    {             //If static is given, i is a permanent class member
        i++;
        j++;
    }
    
}