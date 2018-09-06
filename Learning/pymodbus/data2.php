<!DOCTYPE html>
<html>
<body>
<h1>SCANNER TEMPERATURE PAGE</h1>
<head>
        <title>SCANNER</title>
        <meta http-equiv="refresh" content="1" >
<style>
table
{
border-style:solid;
border-width:4px;
border-color:pink;
}
th
{
	border-style:solid;
border-width:4px;
border-color:green;
}
td
{
	border-style:solid;
border-width:4px;
border-color:green;
}
</style>
    </head>
<?php
$servername = "localhost"; //database address
$username = "root"; //database user
$password = "123456"; // database password
$dbname = "scanner"; //database name
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error); //communication fail thakle eta dekhabe
}
$sql = "SELECT * FROM temperature2 WHERE id=1"; //puro row ta select korechhi
$result = $conn->query($sql); //row ta buffer e gechhe
$row = mysqli_fetch_assoc($result); // buffer er mal ta ekhon row variable e esechhe 
$conn->close();

?> 
<table> 
<tr><th>CHANNEL DESCRIPTION</th><th>PROCESS VALUE</th><th>DEVIATION</th></tr>
<tr><th>CYLINDER TEMPERATURE 1</th><td> <?php echo $row['t1']; ?> </td></tr>
<tr><th>CYLINDER TEMPERATURE 2</th><td> <?php echo $row['t2']; ?> </td></tr>
<tr><th>CYLINDER TEMPERATURE 3</th><td> <?php echo $row['t3']; ?> </td></tr>
<tr><th>CYLINDER TEMPERATURE 4</th><td> <?php echo $row['t4']; ?> </td></tr>
<tr><th>CYLINDER TEMPERATURE 5</th><td> <?php echo $row['t5']; ?> </td></tr>
<tr><th>CYLINDER TEMPERATURE 6</th><td> <?php echo $row['t6']; ?> </td></tr>
<tr><th>TURBOCHARGER TEMP INLET 1</th><td> <?php echo $row['t7']; ?> </td><td> NOT APPLICABLE </td></tr>
<tr><th>TURBOCHARGER TEMP INLET 2</th><td> <?php echo $row['t8']; ?> </td><td> NOT APPLICABLE </td></tr>
<tr><th>TURBOCHARGER TEMP OUTLET</th><td> <?php echo $row['t9']; ?> </td><td> NOT APPLICABLE </td></tr>
<tr><th>GEARBOX LS SHAFT-DE BEARING</th><td> <?php echo $row['t10']; ?> </td><td> NOT APPLICABLE </td></tr>
<tr><th>GEARBOX LS SHAFT-NDE BEARING</th><td> <?php echo $row['t11']; ?> </td><td> NOT APPLICABLE </td></tr>
<tr><th>GEARBOX HS SHAFT-DE BEARING</th><td> <?php echo $row['t12']; ?> </td><td> NOT APPLICABLE </td></tr>
<tr><th>GEARBOX HS SHAFT-NDE BEARING</th><td> <?php echo $row['t13']; ?> </td><td> NOT APPLICABLE </td></tr>
<tr><th>PUMP DE-BEARING</th><td> <?php echo $row['t14']; ?> </td><td> NOT APPLICABLE </td></tr>
<tr><th>PUMP NDE-BEARING</th><td> <?php echo $row['t15']; ?> </td><td> NOT APPLICABLE </td></tr>

</table> 

</body>
</html
