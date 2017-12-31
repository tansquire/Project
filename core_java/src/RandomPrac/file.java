/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package RandomPrac;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;


/**
 *
 * @author piklu
 */
public class file 
{
    public static void main(String[] args) throws Exception
    {
        File f=new File("demo1.txt"); //creat file in main package core
        
        //write to the file
        OutputStream fout = new FileOutputStream(f);
        DataOutputStream dout = new DataOutputStream(fout);
        dout.writeUTF("Hi How are you?");
        
        //read the file
        InputStream fin = new FileInputStream(f);
        DataInputStream din = new DataInputStream(fin);
        String s=din.readUTF();
        
        //just printing
        System.out.println(s);
    }
    
}
