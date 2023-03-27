
<?php
if (isset($_POST['submit'])) {
    $kecepatan = $_POST['kecepatan'];
    $ketepatan = $_POST['ketepatan'];
    $keramahan = $_POST['keramahan'];
    $kenyamanan = $_POST['kenyamanan'];
    $total = $kecepatan + $ketepatan + $keramahan + $kenyamanan;
    $rata = $total / 4;
    if ($rata >= 4) {
        $status = "Sangat Puas";
    } elseif ($rata >= 3) {
        $status = "Puas";
    } elseif ($rata >= 2) {
        $status = "Cukup Puas";
    } else {
        $status = "Tidak Puas";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Survey Kepuasan Pelanggan</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <h1 class="text-center">Survey Kepuasan Pelanggan</h1>
                <form action="" method="post">
                    <div class="form-group">
                        <label for="kecepatan">Kecepatan Pelayanan</label>
                        <select name="kecepatan" id="kecepatan" class="form-control">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="ketepatan">Ketepatan Pelayanan</label>
                        <select name="ketepatan" id="ketepatan" class="form-control">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="keramahan">Keramahan Pelayanan</label>
                        <select name="keramahan" id="keramahan" class="form-control">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="kenyamanan">Kenyamanan Pelayanan</label>
                        <select name="kenyamanan" id="kenyamanan" class="form-control">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <input type="submit" name="submit" value="Submit" class="btn btn-primary">
                    </div>
                </form>
                <?php if (isset($_POST['submit'])) { ?>
                    <div class="alert alert-success">
                        <p>Kecepatan Pelayanan : <?= $kecepatan ?></p>
                        <p>Ketepatan Pelayanan : <?= $ketepatan ?></p>
                        <p>Keramahan Pelayanan : <?= $keramahan ?></p>
                        <p>Kenyamanan Pelayanan : <?= $kenyamanan ?></p>
                        <p>Total : <?= $total ?></p>
                        <p>Rata-rata : <?= $rata ?></p>
                        <p>Status : <?= $status ?></p>
                    </div>
                <?php } ?>
            </div>
        </div>
    </div>
</body>
</html>
