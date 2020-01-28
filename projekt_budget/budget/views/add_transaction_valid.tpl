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
document.getElementById("{{category}}").selected=true;
}
</script>


<html>
  <body onload="selectCategory()">
    <center>
    <div class="divFrame">
      <form method="post">
        Transaction name: <input type="text" name="transactionName" value="{{name}}">
	<p style="color:red">{{ validation.get("name", "") }} </p>
        <br>
        Category: <select name="transactionCategory" class="inputClass">
        % for cat in categories:
            <option value="{{cat[1]}}" id="{{cat[1]}}">{{cat[1]}}</option>
        % end
        </select>
	<p style="color:red">{{ validation.get("category", "") }} </p>
        <br>
        Amount: <input class="inputClass" type="number" name="transactionAmount" value="{{amount}}">
	<p style="color:red">{{ validation.get("amount", "") }} </p>
        <br>
        Date: <input class="inputClass"  type="date" name="transactionDate" id="transactionDate" value="{{date}}">
	<p style="color:red">{{ validation.get("date", "") }} </p>
        <br>
        Note: <br><textarea cols="30" rows="5" class="inputClass"  type="text" name="transactionNote">{{note}}</textarea>
        <br><br>
	% if add=="True":
        <input type="submit" class="button" name="addTransaction" value="Add">
	% else:
	<input type="submit" class="button" name="editTransaction" value="Save">
	% end
      </form>
      <form action="/transactions" method="get">
	<input type="submit" class="button" name="discardTransaction" value="Discard">
      </form>
    </div>
    </center>
  </body>
</html>