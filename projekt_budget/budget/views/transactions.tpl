<style>
div2 {
  resize: both;
  overflow: auto;
  background-color: #8b72be;
  padding: 50 px;
}
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
function showFilter(){
  var block=document.getElementById("divFilter");
  if(block.style.display === "none")
  { block.style.display="inline-block"; }
  else
  { block.style.display="none"; }
  document.getElementById("formFilter").reset();  <!--Treba li rest biti samo na Remove-->
}

function showDiv(id){
  document.getElementById(id).style.display="block";
}

function hideDiv(id){
  document.getElementById(id).style.display="none";
}

var catChecked={{categoriesChecked}};
function check(){
  if(catChecked ==="[]")
  {
	catChecked=[];
  }
 var kategorije="{{categories}}";
  console.log("broj el u categories checked je "+{{categoriesChecked}}.length);
  console.log("broj el u categories checked je "+catChecked.length);
  if(catChecked.length > 0){
    document.getElementById("checkboxAll").checked = catChecked[0] == 1;
    for (index = 0; index < kategorije.length; index++) {
      document.getElementById(""+kategorije[index][1]+"").checked = catChecked[index+1] == 1;
    }
  }

}

function checkChecked(){
if ({{sum(categoriesChecked)}}>0){
document.getElementById("divFilter").style.display="block";
var i;
if ({{categoriesChecked}}[0]==1) { 
for (i = 1; i < {{categoriesChecked}}.length; i++) {document.getElementById(i).checked=true;}}
for (i = 1; i < {{categoriesChecked}}.length; i++) {
if ({{categoriesChecked}}[i]==1) { document.getElementById(i).checked=true;}
}}}
</script>



<body onload="checkChecked()">
  <div class="divFrame">
    <form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form>

    <form action="/transactions/add" method="get"> <input type="submit" class="button" name="add_transaction" value="Add transaction"></form>
    <input type="button" class="button" name="filter_transaction" value="Filter transactions" onclick="showFilter()"></form>
    <form action="/sort" method="get"> <input type="submit" class="button" name="sort_transaction" value="Sort transactions">
      <select>
        <option value="lowest">Lowest amount first</option>
        <option value="highest">Highest amount first</option>
        <option value="oldest">Oldest transaction first</option>
        <option value="newest">Newest transaction first</option>
      </select>
    </form>
    <div id="divFilter" style="display: none;">
      <form id="formFilter" method="post">
	<input type="hidden" name="action" value="filter">
        <label><input type="checkbox" name="checkboxAll" id="checkboxAll" value="all">All</label>
        % for cat in categories:
          <label><input type="checkbox" name="{{cat[1]}}" id="{{cat[0]}}" value="{{cat[0]}}">{{cat[1]}}</label>
        % end
        <br> Min: <input type="number" name="minAmount" step="0.01" value={{minAmount}}>
        <br> Max: <input type="number" name="maxAmount" step="0.01" value={{maxAmount}}>
        <br> Start date: <input type="date" name="minDate" value={{minDate}}>
        <br> End date: <input type="date" name="maxDate" value={{maxDate}}>
        <input type="submit" class="button" name="applyFilter" value="Apply">
      </form>
      <form action="/transactions" method="get">
        <input type="submit" class="button" name="removeFilter" value="Remove">
      </form>
    </div>

    <br>
    <hr>
    <br>
    <input type="month" value="2019-12">

    <div class="panel panel-default">
      % for trans in transactions:
        <div class="panel-body" id="trans{{trans[0]}}">{{trans[0]}}  {{trans[1]}}  {{trans[3]}}  
          <form action="/transactions/edit/{{trans[0]}}" method="get">
            <input type="submit" class="button" style="width:50; height:25;" value="Edit">
          </form>
          <input type="button" class="button" style="width:50; height:25;" value="Delete" onclick='showDiv("div{{trans[0]}}Delete")'>
          <div style="display:none" id="div{{trans[0]}}Delete"> Are you sure you want to delete transaction {{trans[1]}}? 
            <form method="post" >
              <input type="hidden" name="action" value="delete"> <!--Trenutno ne treba, ali ako bude jos post metoda ce trebati-->
              <input type="hidden" name="transactionId" value="{{trans[0]}}">
              <input type="submit" class="button" style="width:50; height:25;"  value="Yes"> 
            </form>
            <input type="button" class="button" style="width:50; height:25;" value="No" onclick="hideDiv('div{{trans[0]}}Delete')">
          </div>
        </div>
      % end
    </div> 
  </div>
</body>