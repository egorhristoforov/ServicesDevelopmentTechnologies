<?php
function sum($a, $b) {
    return $a + $b;
}

function square($num) {
    return $num * $num;
}

ini_set("soap.wsdl_cache_enabled", "0");
$server = new SoapServer(
    "http://kappa.cs.karelia.ru/~hristofo/services/soap/sum.wsdl",
    array('soap_version' => SOAP_1_2)
);

$server->addFunction("sum");
$server->addFunction("square");
$server->handle();
?>