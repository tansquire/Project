
package Mixed;

public class Object_Creation 
{
    public static void main(String[] args) throws Exception
    {
        Class x=Class.forName("Mixed.AA");
        AA obj=(AA)x.newInstance();
        obj.show();
        
    }
    
}
class AA
{
    public void show()
    {
        System.out.println("in AA");
    }
}


