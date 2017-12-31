package Mixed;

public class ObjectCopy_clonning //remember this program
{
    public static void main(String[] args) throws CloneNotSupportedException
    {
        A2 obj =new A2();
        obj.i=5;
        obj.j=6;
        A2 obj1 =(A2) obj.clone();
        obj1.i=100;
        System.out.println(obj);
        System.out.println(obj1);
        
        
    }
    
}
class A2 implements Cloneable //by default extends Object
{
    int i;
    int j;

    @Override   //right click->insert code->toString
    public String toString() {
        return "A2{" + "i=" + i + ", j=" + j + '}';
    }
    @Override //As the method clone in Object class is private, we cant access.
    //so we will override that
    public Object clone() throws CloneNotSupportedException
    // return type of this function should be Object
    {
        return super.clone();  //call clone method of Object class
    }
    
}