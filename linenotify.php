<?php
define('LINE_API_URL'  ,"https://notify-api.line.me/api/notify");
define('LINE_API_TOKEN','y25oS46iZL/s6n3L6OJNMquaRufs1JvRoxK4W3wTB6c2EOw1lvaRExbWpqqRyJmc0NxYGjGDwHga1RYeYZTevwyz4tQm0kd1Lh+SkQMVoTtH5cm/lpxQLy87o3LOxAogsqEret6PXBAb0l+sLjCNrAdB04t89/1O/w1cDnyilFU=');

function post_message($message){

    $data = array(
                        "message" => $message
                     );
    $data = http_build_query($data, "", "&");

    $options = array(
        'http'=>array(
            'method'=>'POST',
            'header'=>"Authorization: Bearer " . LINE_API_TOKEN . "\r\n"
                      . "Content-Type: application/x-www-form-urlencoded\r\n"
                      . "Content-Length: ".strlen($data)  . "\r\n" ,
            'content' => $data
        )
    );
    $context = stream_context_create($options);
    $resultJson = file_get_contents(LINE_API_URL,FALSE,$context );
    $resutlArray = json_decode($resultJson,TRUE);
    if( $resutlArray['status'] != 200)  {
        return false;
    }
    return true;
}


post_message("ÉeÉXÉgìäçe");
