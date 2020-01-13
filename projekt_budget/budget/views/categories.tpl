<style>
.divFrame{
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #fffdd0;
  width: 310px;
  padding: 50px;
  margin: 0 auto;
}
.button {
  background-color: #69359c;
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

function closeAddEdit(id,input,validation){

var block=document.getElementById(id);
block.style.display="none";
document.getElementById(input).value="";
document.getElementById(validation).innerHTML="";

}
function showDiv(id)
{
document.getElementById(id).style.display="block";
}

function hideDiv(id){
document.getElementById(id).style.display="none";
}

function showEdit(id){
if("{{editId}}"===id)
{
document.getElementById("div"+id+"Edit").style.display="block";
document.getElementById("valid"+id).style.display="block";
}
}

function showEdits(){
var categories="{{data}}";
for (index = 0; index < categories.length; ++index) {
    showEdit(categories[index][0]);
}
}


</script>

<html>
<body onload="showEdits()">
<div class="divFrame">
<form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form> 
<input type="button" class="button" name="addCategory" value="Add category" onclick="showAdd()">
<div id="divAdd" style="display: {{disp}}">
  <form method="post">
  <input type="hidden" name="action" value="add">
    Category name: <input type="text" name="cname" id="cname" > <p style="color:red" id="valid"> {{validation}}</p> <br>
	  <input type="submit" class="button" name="addCategory" value="Add">	
	  <input type="button" class="button" name="discardCategory" value="Discard" onclick="closeAddEdit('divAdd','cname','valid')">
  </form>
   
</div>

<div class="panel panel-default">
  % for cat in data:
  <br>
  <div class="panel-body" >{{cat[1]}} <input type="button" class="button" style="width:50; height:25;" value="Edit" onclick='showDiv("div{{cat[0]}}Edit")'>
    <input type="button" class="button" style="width:50; height:25;" value="Delete" onclick='showDiv("div{{cat[0]}}")'>
    <form method="post" >
    <input type="hidden" name="action" value="edit">
    <input type="hidden" name="oldName" value="{{cat[1]}}">
      <div style="display:none" id="div{{cat[0]}}Edit" onload="showEdit('{{cat[0]}}')"><br>Category name: <input type="text" name="nameEdit" id ="nameEdit" placeholder={{cat[1]}}> <br>
        <p style="color:red;display:none" id="valid{{cat[0]}}"> {{validationEdit}}</p> <br>
	<input type="submit" class="button" style="width:50; height:25;"  value="Save" > </form>
	<input type="button" class="button" style="width:50; height:25;" value="Discard" onclick="closeAddEdit('div{{cat[0]}}Edit','nameEdit','valid{{cat[0]}}')">
      </div>
    <div style="display:none" id="div{{cat[0]}}"> Are you sure you want to delete category {{cat[1]}}? 
      <form method="post" >
      <input type="hidden" name="action" value="delete">
      <input type="hidden" name="categoryname" value={{cat[1]}}>
      <input type="submit" class="button" style="width:50; height:25;"  value="Yes"> </form>
      <input type="button" class="button" style="width:50; height:25;" value="No" onclick="hideDiv('div{{cat[0]}}')">
    </div>
  </div>
  % end
</div>
</div>
</body>
</html>