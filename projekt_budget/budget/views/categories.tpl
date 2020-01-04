<style>
.button {
  background-color: #69359c; /* Purple */
  width: 100;
  height: 40;
  border: none;
  color: white;
  padding: 2px 2px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  border: 1px solid black;
  border-color: #322a4f;
}
form{ display: inline-block; }
</style>

<script>
function showAdd(){
var block=document.getElementById("divAdd");
if(block.style.display ==="none")
{block.style.display="block";}
else
{block.style.display="none";}
}

function closeAdd(){
var block=document.getElementById("divAdd");
block.style.display="none";
document.getElementById("cname").value="";
}
</script>


<body>
<body bgcolor="#fffdd0">
<form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form> 
<input type="submit" class="button" name="add_category" value="Add category" onclick="showAdd()">
<div id="divAdd" style="display: none;">
<form method="post">
  Category name: <input type="text" name="cname" id="cname" ><br>
<input type="submit" class="button" name="add_category" value="Add" onclick="showAdd()"> 
</form>
<input type="submit" class="button" name="discard_category" value="Discard" onclick="closeAdd()">


</div>

<div class="panel panel-default">
% for cat in data:
<div class="panel-body" >{{cat[1]}} <button class="button" style="width:50; height:25;">Edit</button> <button class="button" style="width:50; height:25;">Delete</button> </div>
<br>
% end

</body>