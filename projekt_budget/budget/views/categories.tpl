<style>
.divFrame{
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #F2F7FB;
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

.buttonSmaller {
  background-color: #69359c; /* Purple */
  width: 50;
  height: 25;
  border: none;
  color: white;
  padding: 2px 2px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  border: 1px solid black;
  border-color: #322a4f;
  font-family: "Times New Roman", Times, serif;
}

.warning {
  display: none;
  color: red;
}

form { 
  display: inline-block; 
}

body {
  background-image: url("https://images.unsplash.com/photo-1496167117681-944f702be1f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1789&q=80");
  background-size: 100% 100%;
}
</style>

<script>
function showAdd(){
  var block=document.getElementById("divAdd");
  if(block.style.display ==="none")
  { block.style.display="block"; }
  else 
  { block.style.display="none"; }
}

function closeAddEdit(id,input,validation){
  var block=document.getElementById(id);
  block.style.display="none";
  document.getElementById(input).value="";
  document.getElementById(validation).innerHTML="";
}

function showDiv(id){
  document.getElementById(id).style.display="block";
}

function hideDiv(id){
  document.getElementById(id).style.display="none";
}

function closeDelete(id){
  hideDiv("div"+id);
  hideDiv("warning"+id); 
}

function showEdit(id){
  if("{{editId}}"===id)
  {
    document.getElementById("div"+id+"Edit").style.display="block";
    document.getElementById("valid"+id).style.display="block";
  }
}

function showWarning(id){
   if("{{deleteWarning}}" == id){
    document.getElementById("warning"+id).style.display="block";
    document.getElementById("div"+id).style.display="block";
  }
}

function showEditsAndWarning(){
  var categories="{{data}}";
  for (index = 0; index < categories.length; index++) {
    showEdit(categories[index][0]);
    showWarning(categories[index][0]);
  }
}


</script>

<html>
  <body onload="showEditsAndWarning()">
    <div class="divFrame">
      <form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form> 
      <input type="button" class="button" name="addCategory" value="Add category" onclick="showAdd()">
      <div id="divAdd" style="display: {{disp}}">
        <form action="/categories" method="post">
          <input type="hidden" name="action" value="add">
          Category name: <input type="text" name="cname" id="cname" > <p style="color:red" id="valid"> {{validation}}</p> <br>
	  <input type="submit" class="button" name="addCategory" value="Add">	
	  <input type="button" class="button" name="discardCategory" value="Discard" onclick="closeAddEdit('divAdd','cname','valid')">
        </form>
      </div>

    <div class="panel panel-default">
      % for cat in data:
      <br>
      <div class="panel-body">
        <table align="center">
	  <tr>
		<td style="width:100px"> <p>{{cat[1]}}</p> </td>
		<td> <input type="button" class="buttonSmaller" value="Edit" onclick='showDiv("div{{cat[0]}}Edit")'> </td>
		<td> <input type="button" class="buttonSmaller" value="Delete" onclick='showDiv("div{{cat[0]}}")'> </td>
	  </tr>
        </table>
  
        <form action="/categories" method="post" >
          <input type="hidden" name="action" value="edit">
          <input type="hidden" name="oldName" value="{{cat[1]}}">
          <div style="display:none" id="div{{cat[0]}}Edit" onload="showEdit('{{cat[0]}}')"><br>Category name: <input type="text" name="nameEdit" id ="nameEdit" placeholder="{{cat[1]}}"> <br>
            <p style="color:red;display:none" id="valid{{cat[0]}}"> {{validationEdit}}</p> <br>
	    <input type="submit" class="buttonSmaller"  value="Save" > </form>
	    <input type="button" class="buttonSmaller" value="Discard" onclick="closeAddEdit('div{{cat[0]}}Edit','nameEdit','valid{{cat[0]}}')">
          </div>
          <div style="display:none" id="div{{cat[0]}}"> Are you sure you want to delete category {{cat[1]}}? 
            <form action="/categories" method="post" >
              <input type="hidden" name="action" value="delete">
              <input type="hidden" name="categoryname" value="{{cat[1]}}">
              <input type="submit" class="buttonSmaller"  value="Yes">
            </form>
            <input type="button" class="buttonSmaller" value="No" onclick="closeDelete('{{cat[0]}}')">
            <p class="warning" id="warning{{cat[0]}}">There are transactions with this category, can't be deleted.</p>
          </div>
        </div>
        % end
      </div>
    </div>
  </body>
</html>