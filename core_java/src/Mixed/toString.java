
package Mixed;

public class toString 
       
{
    public static void main(String[] args)
    {
        Test obj=new Test(5,"Partha");
        System.out.println(obj);
        
    }
    
    
   
}
class Test
{
    int i;
    String s;

    public Test(int i, String s) //right click->insert code->constructor
    {
        this.i = i;
        this.s = s;
    }

    @Override
    public String toString() //right click->insert code->toString
    {
        return "Test{" + "i=" + i + ", s=" + s + '}';
    }
    
    
}