<!DOCTYPE html>
<html>

<head>
<style>

#area {
    
    position: absolute;
    top: 10px;
    left: 150px;
    text-align: center;
    font-size: 15px;
    background-color: #FFF8DC;
}

#animate {
    
    position: absolute;
    top: 40px;
    left: 150px;

}

#reading {
    
    position: absolute;
    top: 100px;
    left: 350px;
    text-align: center;
    font-size: 13px;
    color:blue
    
}
</style>

</head>

<body>


<?php
$servername = "10.21.160.201"; //database address
$username = "root";           //database user
$password = "gowsalya";         // database password
$dbname = "test";          //database name

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

<div id="area">Sump tank area </div>

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
<p> <font size="2">Water tank</font></p>
</div>


<div id="reading">
<table width="100", border="1">
<tr>
<td height="6",> <?php echo $row["Value"];?> </td>
</tr>
</table>
<p> <font size="2">Water level in feet</font></p>
</div>

</body>
</html

