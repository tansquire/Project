
package core;


public class Loop 
{
    public static void main(String[] args)
    {
        int i,j,k;
        for(i=0;i<10;i++)
        System.out.println(i);
        
      j=0;
      while(j<10)
      {
          System.out.println(j);
          j++;
      }
      
      k=0;
      do
      {
          System.out.println(k);
          k++;
      }while(k<10);    //In do-while loop 1st statement is executed, then checking.
        
    }
    
}
