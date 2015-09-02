<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style>
      body {
        padding: 60px 0px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Get Your Race Stats</h1>
      <form role="form" method="post" action="/plot">
        <table>
            <td>
              <h3>Race Id</h3>
              <div class="form-group" "col-md-2">
                <input type="string" name="ID" class="form-control" placeholder="Race ID">
              </div>
              <h3>Name</h3>
              <div class="form-group" "col-md-2">
                <input type="string" name="NAME" class="form-control" placeholder="Your Name">
              </div>
            </td>
          </tr>
        </table>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
    </div>
    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
