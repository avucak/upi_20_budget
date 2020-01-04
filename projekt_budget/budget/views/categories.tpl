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
else {block.style.display="none";}
}

function Add(){
if (validation=="")
{block.style.display="block";}
}

function closeAdd(){

var block=document.getElementById("divAdd");
block.style.display="none";
document.getElementById("cname").value="";
document.getElementById("valid").innerHTML="";

}
function deleteClick(id)
{
document.getElementById(id).style.display="block";
}

function noClick(id){
document.getElementById(id).style.display="none";
}
</script>


<body>
<body bgcolor="#fffdd0">
<form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form> 
<input type="submit" class="button" name="add_category" value="Add category" onclick="showAdd()">
<div id="divAdd" style="display: {{disp}}">
<form method="post">
<input type="hidden" name="action" value="add">
  Category name: <input type="text" name="cname" id="cname" > <p style="color:red" id="valid"> {{validation}}</p> <br>
	<input type="submit" class="button" name="add_category" value="Add" onclick="Add()"> 	
</form>
<input type="submit" class="button" name="discard_category" value="Discard" onclick="closeAdd();">

</div>

<div class="panel panel-default">
% for cat in data:
<div class="panel-body" >{{cat[1]}} <input type="submit" class="button" style="width:50; height:25;" value="Edit"> <input type="submit" class="button" style="width:50; height:25;" value="Delete" onclick='deleteClick("div{{cat[0]}}")'> </div>
<div style="display:none" id="div{{cat[0]}}"> Are you sure you want to delete category {{cat[1]}}? 
<form method="post" >
<input type="hidden" name="action" value="delete">
<input type="hidden" name="categoryname" value={{cat[1]}}>
<input type="submit" class="button" style="width:50; height:25;"  value="Yes"> </form>
<input type="submit" class="button" style="width:50; height:25;" value="No" onclick="noClick('div{{cat[0]}}')"></div>
<br>
% end

</body>