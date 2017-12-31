<?php
include('Config.php');


//$sql = "UPDATE command SET open='17' WHERE valve=1";

//$conn->query($sql);
  
        


        $sql1 = "SELECT * FROM command WHERE valve='1'"; 

	$result1 = $conn->query($sql1);
	$row1 = mysqli_fetch_assoc($result1);

        $x=$row1[open];
        echo$x;



?>
