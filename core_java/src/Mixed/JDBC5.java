
package Mixed;
import java.sql.*;
//For netbeans, right click on library->add library->mysql jdbc driver->add
//For eclips, you have to download the library(jar file) first
//and then follow the abobe steps.

public class JDBC5 //printing whole table
{
    public static void main(String[] args) throws Exception 
    {
        
        String url="jdbc:mysql://10.21.160.201:3306/test";//test is db name
        String user="root";
        String pass="gowsalya";
        String Query="select * from scada";
        Class.forName("com.mysql.jdbc.Driver"); //registration
        
        Connection con=DriverManager.getConnection(url,user,pass);//connection
        Statement st=con.createStatement();//create statement to execute query
        ResultSet rs=st.executeQuery(Query);
        
        while(rs.next())
        {
        String s=rs.getString(1)+rs.getString(2)+rs.getString(3)+rs.getString(4);
        System.out.print(s);//printing in row format
        //System.out.println(s);//Disable above line, and enable this line
        //This is for printing in table format
        }
        st.close();
        con.close();
    }
    
}
