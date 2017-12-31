
package oops;


public class SuperKey2 
{
    public static void main(String[] args) 
    {
        B3 obj=new B3();  //If this obj is not created, nothing will be displayed
        obj.display();
        
    }
    
}
class A3
{
    int i=2;
    void show()
    {
        System.out.println("Inside parent class");
    }
}
class B3 extends A3
{
    int i=5;
    void show()
    {
        System.out.println("Inside child  class");
        
    }
    void display()  //super.i or super.show() cant be written inside main()
    {
        System.out.println(i);
        System.out.println(super.i);
        show();
        super.show();
    }
      
}

