
package oops;


public class Constructor_Initialization
{
    public static void main(String[] args) 
    {
        Student1 Ram=new Student1();
        System.out.println("Total Marks="+Ram.total());
        Student1 Sam=new Student1(10,10);
        System.out.println("Total Marks="+Sam.total());
        
        
    }
    
    
}
class Student1
{
    
    int math;
    int phys; 
            
    
  
     Student1() 
    {
        math=36;
        phys=87;  
        System.out.println(math+phys);
    }
     Student1(int x, int y)  
    {
       math=x;
       phys=y; 
       System.out.println(math+phys);
    }
     
     public int total()
     {
         return(math+phys); //this function does not take any value, but returns.
     }
     
} 

