<?php
include('Config.php');


$sql = "UPDATE command SET opened='1' WHERE valve=1";

$conn->query($sql);
  
        
?>
