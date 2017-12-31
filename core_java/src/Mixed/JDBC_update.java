package Mixed;
import java.sql.*;
//For netbeans, right click on library->add library->mysql jdbc driver->add
//For eclips, you have to download the library(jar file) first
//and then follow the abobe steps.

public class JDBC_update //printing single element of any row
{
    public static void main(String[] args) throws Exception 
    {
        //Following things has to be updated into a new row
        int id=6;
        int id1=1;
        String tag="FLOW";
        String type="DO";
        String val="100";
        
        //connection and reristration
        String url="jdbc:mysql://10.21.160.201:3306/test";//test is db name
        String user="root";
        String pass="gowsalya";
        String Query="update scada set value = ? where id = ?";
        String Query1="update scada set value = ?, type= ? where id = ?";
        Class.forName("com.mysql.jdbc.Driver"); //registration
        
        Connection con=DriverManager.getConnection(url,user,pass);//connection
        PreparedStatement st=con.prepareStatement(Query);//
        //You have to use PreparedStatement for insertion
        st.setString(1, val);//(position of ?, value of id)
        st.setInt(2, id);
        int count=st.executeUpdate();//executeUpdate return an integer
        System.out.println("Nos of row affected="+""+count);
        
        PreparedStatement st1=con.prepareStatement(Query1);//
        //You have to use PreparedStatement for insertion
        st1.setString(1, val);//(position of ?, value of id)
        st1.setString(2, type);
        st1.setInt(3, id1); //third ? of query1 will be replaced by id1
        int count1=st1.executeUpdate();//executeUpdate return an integer
        System.out.println("Nos of row affected="+""+count1);
        
        st.close();
        con.close();
    }
    
}

