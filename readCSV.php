<?php
$csvFile = public_path('file.csv');

if (!File::exists($csvFile)) {
    die("File not found");
}

$file = fopen($csvFile, 'r');

while (!feof($file)) {
    $line = fgetcsv($file);
    if (!$line) {
        continue; // ignore blank lines
    }

    // Insert row into database
    DB::table('table_name')->insert([
        'column_1' => $line[0],
        'column_2' => $line[1],
        // ...
    ]);
}

fclose($file);
