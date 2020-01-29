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
  background-color: #69359c; /* Purple */
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
.title {
  color: #8810c4;
}

body {
  background-image: url("https://images.unsplash.com/photo-1496167117681-944f702be1f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1789&q=80");
  background-size: 100% 100%;
}
</style>


<html>
  <body>
    <center>
      <div class="divFrame">
        <h1 class="title"> budget.IO </h1>
        <form action="/transactions" method="get">
          <input type="submit" class="button" name="transaction" value="Transactions">
        </form>

       <form action="/categories" method="get">
         <input type="submit" class="button" name="category" value="Categories">
       </form>

      <form action="/overview" method="get">
        <input type="submit" class="button" name="overview" value="Overview">
      </form>
    </div>
  </body>
</html>