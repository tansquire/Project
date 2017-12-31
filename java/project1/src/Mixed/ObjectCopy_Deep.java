
package Mixed;


public class ObjectCopy_Deep
{
    public static void main(String[] args) 
    {
        A1 obj =new A1();
        obj.i=5;
        obj.j=6;
        A1 obj1 =new A1();
        obj1.i=500;
        obj1.j=600;
        System.out.println(obj);
        System.out.println(obj1);
        
        
    }
    
}
class A1
{
    int i;
    int j;

    @Override
    public String toString() {
        return "A{" + "i=" + i + ", j=" + j + '}';
    }
    
}