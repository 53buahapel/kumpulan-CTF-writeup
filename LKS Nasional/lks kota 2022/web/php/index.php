<?php
foreach($_REQUEST['envs'] as $key => $val) {
    putenv("{$key}={$val}");
}

var_dump($_REQUEST['envs']);
var_dump($_ENV);
system('bash -c "echo 1"');
?>

