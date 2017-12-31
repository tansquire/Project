<!DOCTYPE html>
<html>

<head>
<style>


#animate {
    
    position: absolute;
    top: 0px;
    left: 0%;

}

#reading {
    
    position: absolute;
    top: 350px;
    left: 15%;
    text-align: center;
    color:blue
    
}
</style>

</head>

<body>


<?php
$servername = "localhost"; //database address
$username = "root";           //database user
$password = "123456";         // database password
$dbname = "test_db";          //database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error); //communication fail thakle eta dekhabe
}

$sql = "SELECT * FROM level WHERE Device=1";     //puro row ta select korechhi
$result = $conn->query($sql);                         //row ta buffer e gechhe
$row = mysqli_fetch_assoc($result);                   // buffer er mal ta ekhon row variable e esechhe 
$y=$row["Value"];  //row er modhye sudhu roll select 

$x = $y*7.5;

$conn->close();
?> 


<div id="animate">

<table width="150", border="1">    


<tr>
<td border="none", height="<?php $x =150-$x; echo $x;?>", bgcolor="#FFFFFF">  

	</td>
 </tr>
  <tr>
    <td border="none", height="<?php $y = 150-$x ;echo $y;?>", bgcolor="#008000"> </td>
  </tr>
</table> 


</div>


<div id="reading">
<table width="150", border="1">
<tr>
<td height="6",> <?php echo $row["Value"]; echo"    feet"?> </td>
</tr>
</table>

</div>

</body>
</html

