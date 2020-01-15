<style>
.divFrame {
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #fffdd0;
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
</style>

<script>

</script>


<html>
<body>
<center>
<div class="divFrame">
Transaction name: <input type="text" name="transactionName">
<br>
Category: <select class="inputClass" >
% for cat in categories:
  <option value="{{cat[1]}}">{{cat[1]}}</option>
  % end
</select>
<br>
Amount: <input class="inputClass" type="number" name="transactionAmount">
<br>
Date: <input class="inputClass"  type="date" name="transactionDate" id="transactionDate">
<br>
Note: <input class="inputClass"  type="text" style="height:50px" name="TransactionNote">
<br>
<br>

<form method="post"><input type="submit" class="button" name="addTransaction" value="Add"></form>
<form action=".." method="get"><input type="button" class="button" name="discardTransaction" value="Discard">
</div>
</center>
</body>
</html>