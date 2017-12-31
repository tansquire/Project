package Mixed;
import java.sql.*;
//For netbeans, right click on library->add library->mysql jdbc driver->add
//For eclips, you have to download the library(jar file) first
//and then follow the abobe steps.

public class JDBC_insert //printing single element of any row
{
    public static void main(String[] args) throws Exception 
    {
        //Following things has to be inserted into a new row
        int id=6;
        String tag="FLOW";
        String type="AI";
        String val="59";
        
        String url="jdbc:mysql://10.21.160.201:3306/test";//test is db name
        String user="root";
        String pass="gowsalya";
        String Query="insert into scada values(?,?,?,?)";
        Class.forName("com.mysql.jdbc.Driver"); //registration
        
        Connection con=DriverManager.getConnection(url,user,pass);//connection
        PreparedStatement st=con.prepareStatement(Query);//
        //You have to use PreparedStatement for insertion
        st.setInt(1, id);//(position of ?, value of id)
        st.setString(2, tag);
        st.setString(3, type);//3rd ? will be replaced by AI(type=AI)
        st.setString(4, val);
        int count=st.executeUpdate();//executeUpdate return an integer
        System.out.println("Nos of row affected="+""+count);
        st.close();
        con.close();
    }
    
}

