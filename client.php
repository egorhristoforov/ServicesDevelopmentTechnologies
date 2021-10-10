<?php

ini_set("soap.wsdl_cache_enabled", "0");
$client = new SoapClient("http://kappa.cs.karelia.ru/~hristofo/services/soap/sum.wsdl");

while (true) {
    $a = (double)readline("First number: ");
    $b = (double)readline("Second number: ");

    $squareA = $client->square($a);
    $squareB = $client->square($b);

    $sum = $client->sum($squareA, $squareB);

    echo "Sum of squares: ", $sum, "\n";
}

?>
