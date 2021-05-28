<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">


  <title>OK</title>
</head>

<body>
  <div class="container">
    <div class="row">
      <h1> FLASK WEB</h1>
    </div>
    <br>
    <br>

    <div class="row">

      <div class="col">
        <h3>Daftar Rumah Sakit Rujukan COVID-19</h3>
        <hr>
        <table class="table table-dark ">
          <thead>
            <tr>
              <th>No</th>
              <th>Nama Rumah Sakit</th>
              <th>Alamat</th>
              <th>Kota</th>
              <th>Provinsi</th>
              <th>Nomer Telepon</th>
            </tr>
          </thead>
          <tbody>
            {% for nama_rs in rsud %}
            <tr>

              <td scope="row">{{loop.index}}</td>
              <td>{{ nama_rs['name'] }}</td>
              <td>{{ nama_rs['address']}}</td>
              <td>{{ nama_rs['region']}}</td>
              <td>{{ nama_rs['province']}}</td>
              <td class="bg-success">{{ nama_rs['phone']}}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>

    </div>
  </div>




  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4"
    crossorigin="anonymous"></script>

</body>

</html>