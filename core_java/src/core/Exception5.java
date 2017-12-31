package core;

import java.util.Scanner;

public class Exception5 {

    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a number");
        int i = input.nextInt();
        try 
        {
            if (i < 10) 
            {
                throw new MyException();
            }

        } 
        catch (MyException e) 
        {
            System.out.println("HI");
        }

    }
}

class MyException extends Exception 
{

    void MyException(String s) 
    {
        //super(s);
    }
}
