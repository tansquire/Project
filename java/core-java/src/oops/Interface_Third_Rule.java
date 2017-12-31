package oops;


public class Interface_Third_Rule
{
    public static void main(String[] args) 
    {
//        AAA obj =new AAA();
//        obj.show();
//        
    }
    
}
interface Def3
{
    default void show()
    {
        System.out.println("def3");
    }
}
class Def4   //class has higher priority than interface
{
     void show()
    {
        System.out.println("def4");
    }
}
////class AAA extends Def4 implements Def3
//{
//    
//    
//}
