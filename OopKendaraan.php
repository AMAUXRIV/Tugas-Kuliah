<?php
class Kendaraan {
  public $jenis;
  public $warna;
  public $merk;
  public $bahan_bakar;
  public $kapasitas;

  function __construct($jenis, $warna, $merk, $bahan_bakar, $kapasitas) {
    $this->jenis = $jenis;
    $this->warna = $warna;
    $this->merk = $merk;
    $this->bahan_bakar = $bahan_bakar;
    $this->kapasitas = $kapasitas;
  }

  function show_info() {
    echo "Jenis kendaraan: " . $this->jenis . ",";
    echo "Warna kendaraan: " . $this->warna . ",";
    echo "Merk kendaraan: " . $this->merk . ",";
    echo "Jenis bahan bakar: " . $this->bahan_bakar . ",";
    echo "Kapasitas tangki: " . $this->kapasitas . " liter<br>";
  }
}

// membuat objek kendaraan1
$kendaraan1 = new Kendaraan("Mobil", "Hitam", "Toyota", "Bensin", 50);

// menampilkan informasi kendaraan1
$kendaraan1->show_info();

// membuat objek kendaraan2
$kendaraan2 = new Kendaraan("Motor", "Merah", "Honda", "Premium", 10);

// menampilkan informasi kendaraan2
$kendaraan2->show_info();

?>