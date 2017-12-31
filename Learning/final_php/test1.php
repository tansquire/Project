<?PHP
 
$a="hello";

 
?>
<script>
function echoHello(){
 alert("<?PHP hello(); ?>");
 }
</script>
 
<?PHP
FUNCTION hello(){
 GLOBAL $a;
 ECHO $a;
include("insert.php");

}
 
?>
 
<button onclick="echoHello()">Say Hello</button>
