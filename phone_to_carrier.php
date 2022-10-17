<?php

function phone2carrier($phoneNumber){
    $phonePattern = '/^(010)-[0-9]{4}-[0-9]{4}$/';

    if(preg_match($phonePattern, $phoneNumber, $match)){
        echo "입력된 전화번호 :  " . $phoneNumber . "\n";
    } else {
        echo "전화번호를 확인하고 다시 입력해 주세요.\n";
        return "wrong number";
    }

    $carrier = array(
        '20' => "SKT",      '21' => "LG U+",    '22' => "LG U+",    '23' => "LG U+",
        '24' => "LG U+",    '25' => "KT",       '26' => "KT",       '27' => "KT",
        '28' => "KT",       '29' => "KT",       '30' => "KT",       '31' => "SKT",
        '32' => "KT",       '33' => "KT",       '34' => "KT",       '35' => "SKT",
        '36' => "SKT",      '37' => "SKT",      '38' => "SKT",      '39' => "LG U+",
        '40' => "SKT",      '41' => "SKT",      '42' => "KT",       '43' => "KT",
        '44' => "KT",       '45' => "SKT",      '46' => "SKT",      '47' => "SKT",
        '48' => "SKT",      '49' => "SKT",      '50' => "SKT",      '51' => "KT",
        '52' => "SKT",      '53' => "SKT",      '54' => "SKT",      '55' => "LG U+",
        '56' => "LG U+",    '57' => "LG U+",    '58' => "LG U+",    '62' => "SKT",
        '63' => "SKT",      '64' => "SKT",      '65' => "KT",       '66' => "KT",
        '67' => "KT",       '68' => "KT",       '69' => "KT",       '70' => "SKT",
        '71' => "SKT",      '72' => "KT",       '73' => "KT",       '74' => "KT",
        '75' => "LG U+",    '76' => "LG U+",    '77' => "LG U+",    '78' => "LG U+",
        '79' => "LG U+",    '80' => "LG U+",    '81' => "LG U+",    '82' => "LG U+",
        '83' => "LG U+",    '84' => "LG U+",    '85' => "SKT",      '86' => "SKT",
        '87' => "SKT",      '88' => "SKT",      '89' => "SKT",      '90' => "SKT",
        '91' => "SKT",      '92' => "SKT",      '93' => "SKT",      '94' => "SKT",
        '95' => "KT",       '96' => "KT",       '97' => "KT",       '98' => "KT",
        '99' => "KT"
    );

    $phone = explode("-", $phoneNumber);
    
    if(array_key_exists(substr($phone[1], 0, 2), $carrier)){
        echo "\n해당 전화번호는 " . $carrier[substr($phone[1], 0, 2)] . "로 가입된 전화번호입니다.\n";
        echo "위 정보는 개통 기준 정보임으로 현재는 변경되었을 수도 있습니다.";
        return $carrier[substr($phone[1], 0, 2)];
    } else{
        echo "\n해당 전화번호는 없는 번호 입니다";
        return "invalid";
    }
}

$phoneNumber = "010-2000-0000"; // 010-****-**** 형식으로 입력

phone2carrier($phoneNumber);

?>