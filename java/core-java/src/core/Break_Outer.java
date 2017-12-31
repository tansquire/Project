
package core;


public class Break_Outer
{
    public static void main(String[] args) 
           
    {
         int i,j;
         partha:
        for(i=0;i<5;i++)
        {
            for(j=0;j<5;j++)
            {
                if(i==2)
                break partha;
                System.out.print("*");
            }
            System.out.println("");
        }
    }
    
}
