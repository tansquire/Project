
<?php

include('session.php');
if($opened_status==1)
echo "OPENED";
elseif($closed_status==1)
echo "CLOSED";
else
echo "INTERMEDIATE";
?>
