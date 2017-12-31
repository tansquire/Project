
package Mixed;


public class ObjectCopy_Shallow
{
    public static void main(String[] args) 
    {
        A obj =new A();
        obj.i=5;
        obj.j=6;
        A obj1 =obj;
        obj.i=100;
        System.out.println(obj);
        System.out.println(obj1);
        
        
    }
    
}
class A
{
    int i;
    int j;

    @Override
    public String toString() {
        return "A{" + "i=" + i + ", j=" + j + '}';
    }
    
}