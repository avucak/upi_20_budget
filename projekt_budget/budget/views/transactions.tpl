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
  { block.style.display="block"; }
  else
  { block.style.display="none"; }
}

function showDiv(id){
  document.getElementById(id).style.display="block";
}

function hideDiv(id){
  document.getElementById(id).style.display="none";
}

</script>



<body>
  <div class="divFrame">
    <form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form>

    <form action="/transactions/add" method="get"> <input type="submit" class="button" name="add_transaction" value="Add transaction"></form>
    <form action="/filter" method="get"><input type="submit" class="button" name="filter_transaction" value="Filter transactions" onclick="showFilter()"></form>
    <form action="/sort" method="get"> <input type="submit" class="button" name="sort_transaction" value="Sort transactions">
      <select>
        <option value="lowest">Lowest amount first</option>
        <option value="highest">Highest amount first</option>
        <option value="oldest">Oldest transaction first</option>
        <option value="newest">Newest transaction first</option>
      </select>
    </form>
    <div id="divFilter" style="display: none;">
      <input type="checkbox" name="food">All<input type="checkbox" name="food">Food <input type="checkbox" name="food">Rent <input type="checkbox" name="food">Clothes
      <br> Min:<input type="text">   Max:<input type="text">
      <br>Start date: <input type="date" value="2018-12-01">   End date:<input type="date" value="2018-12-31">
      <input type="submit" class="button" name="applyFilter" value="Apply">
      <input type="submit" class="button" name="removeFilter" value="Remove">
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