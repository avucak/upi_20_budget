<style>
.divFrame {
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #F2F7FB;
  width: 310px;
  padding: 50px;
}
.button {
  background-color: #69359c; 
  width: 100;
  height: 40;
  border: none;
  color: white;
  padding: 2px 2px;
  margin: 5px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
}

.inputClass {
margin: 5px;
}
form{ display: inline-block; }

body {
  background-image: url("https://images.unsplash.com/photo-1496167117681-944f702be1f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1789&q=80");
  background-size: 100% 100%;
}
</style>

<script>
function selectCategory()
{
  var categories="{{categories}}";
  for (index = 0; index < categories.length; index++) {
    if(categories[index][0]=={{category}})    
    {
      document.getElementById("{{category}}").selected=true;
    }
  }
}
</script>


<html>
  <body onload="selectCategory()">
    <center>
    <div class="divFrame">
      <form method="post" action="/transactions/edit/{{trans_id}}">
        Transaction name: <input type="text" name="transactionName" value="{{name}}">
        <br>
        Category: <select name="transactionCategory" class="inputClass">
        % for cat in categories:
        <option value="{{cat[1]}}" id="{{cat[0]}}">{{cat[1]}}</option>
        % end
        </select>
        <br>
        Amount: <input class="inputClass" type="number" name="transactionAmount" step="0.01" value="{{amount}}">
        <br>
        Date: <input class="inputClass"  type="date" name="transactionDate" id="transactionDate" value="{{date}}">
        <br>
        Note: <br><textarea cols="30" rows="5" class="inputClass"  type="text" name="transactionNote">{{note}}</textarea>
        <br><br>
        <input type="submit" class="button" name="addTransaction" value="Save">
      </form>
      <form action="/transactions" method="get"><input type="submit" class="button" name="discardTransaction" value="Discard"></form>
    </div>
    </center>
  </body>
</html>