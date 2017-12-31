<!DOCTYPE html>
<html>
<body>
<meta http-equiv="refresh" content = "2" /> 

<?php
$servername = "10.22.52.214";
$username = "root";
$password = "123456";
$dbname = "test_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT idstudent, name, roll FROM student";
$result = $conn->query($sql);
$sql1 = "SELECT roll FROM student WHERE idstudent=10 limit 1";
$result1 = mysql_query($sql1);
$value = mysql_fetch_object($result1);

echo "$value";



if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["idstudent"]. " - Name: " . $row["name"]. " " . $row["roll"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?> 




<table width="100", border="1">

<?php 

$z =10;
$x = $row[2]*$z;


?>
  
<tr>
<td border="none", height="<?php $x =200-$x; echo $x;?>", bgcolor="#FFFFFF">  

	</td>
 </tr>
  <tr>
    <td border="none", height="<?php $y = 200-$x ;echo $y;?>", bgcolor="#008000"> </td>
  </tr>
</table> 

<?php echo $result1;?>


</body>
</html

