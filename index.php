<?php

############################################
### ライン通知用の設定
############################################
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

# vendorフォルダ配下のライブラリを自動で読込
require_once __DIR__ . '/vendor/autoload.php';

# CurlHTTPClientのインスタンス化
$httpClient = new \LINE\LINEBot\HTTPClient\CurlHTTPClient(getenv('CHANNEL_ACCESS_TOKEN'));
# LineBotのインスタンス化
$bot = new \LINE\LINEBot($httpClient, ['channelSecret' => getenv('CHANNEL_SECRET')]);

$signature = $_SERVER["HTTP_" . \LINE\LINEBot\Constant\HTTPHeader::LINE_SIGNATURE];
try {
  $events = $bot->parseEventRequest(file_get_contents('php://input'), $signature);
} catch(\LINE\LINEBot\Exception\InvalidSignatureException $e) {
  error_log("parseEventRequest failed. InvalidSignatureException => ".var_export($e, true));
} catch(\LINE\LINEBot\Exception\UnknownEventTypeException $e) {
  error_log("parseEventRequest failed. UnknownEventTypeException => ".var_export($e, true));
} catch(\LINE\LINEBot\Exception\UnknownMessageTypeException $e) {
  error_log("parseEventRequest failed. UnknownMessageTypeException => ".var_export($e, true));
} catch(\LINE\LINEBot\Exception\InvalidEventRequestException $e) {
  error_log("parseEventRequest failed. InvalidEventRequestException => ".var_export($e, true));
}

foreach ($events as $event) {
  if (!($event instanceof \LINE\LINEBot\Event\MessageEvent)) {
    error_log('Non message event has come');
    continue;
  }
  if (!($event instanceof \LINE\LINEBot\Event\MessageEvent\TextMessage)) {
    error_log('Non text message has come');
    continue;
  }
  ############################################
  ### リプライトークンを取得
  ############################################
  $token = $event->getReplyToken();
  ############################################
  ### 受信したテキストを取得
  ############################################
  $recv_text = $event->getText();
  $send_test = 'comming soon.';  # $recv_text;
  ############################################
  ### bot,replyText：テキストを送信する
  ### 第一引数：リプライトークン（取得から数十秒間しか使えない）
  ### 第二引数：送信するテキスト
  ############################################
  $bot->replyText($token, $send_test);
}

post_message("テスト投稿");

 ?>