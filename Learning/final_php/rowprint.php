<!DOCTYPE html>
<html>
<body>

<?php
$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "test_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//$sql = "SELECT * FROM student WHERE idstudent=10";
$sql1 = "SELECT * FROM student WHERE idstudent=10 and name='sachin'";
$result = $conn->query($sql1);
$row = mysqli_fetch_assoc($result);

//row printing

echo"$row[name]";

//foreach($row as $x => $x_value) 

//{
   // echo "Key=" . $x . ", Value=" . $x_value;
   // echo "<br>";
//}

$conn->close();
?> 

</body>
</html

