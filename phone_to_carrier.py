import re

def isPhone(text):
    if len(text) != 13:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 8):
            if not text[i].isdecimal():
                return False
        if text[8] != '-':
            return False
        for i in range(9, 13):
            if not text[i].isdecimal():
                return False
    return True


def carrier(key):
    telecom = {
        '20' : "SKT",      '21' : "LG U+",    '22' : "LG U+",    '23' : "LG U+",
        '24' : "LG U+",    '25' : "KT",       '26' : "KT",       '27' : "KT",
        '28' : "KT",       '29' : "KT",       '30' : "KT",       '31' : "SKT",
        '32' : "KT",       '33' : "KT",       '34' : "KT",       '35' : "SKT",
        '36' : "SKT",      '37' : "SKT",      '38' : "SKT",      '39' : "LG U+",
        '40' : "SKT",      '41' : "SKT",      '42' : "KT",       '43' : "KT",
        '44' : "KT",       '45' : "SKT",      '46' : "SKT",      '47' : "SKT",
        '48' : "SKT",      '49' : "SKT",      '50' : "SKT",      '51' : "KT",
        '52' : "SKT",      '53' : "SKT",      '54' : "SKT",      '55' : "LG U+",
        '56' : "LG U+",    '57' : "LG U+",    '58' : "LG U+",    '62' : "SKT",
        '63' : "SKT",      '64' : "SKT",      '65' : "KT",       '66' : "KT",
        '67' : "KT",       '68' : "KT",       '69' : "KT",       '70' : "SKT",
        '71' : "SKT",      '72' : "KT",       '73' : "KT",       '74' : "KT",
        '75' : "LG U+",    '76' : "LG U+",    '77' : "LG U+",    '78' : "LG U+",
        '79' : "LG U+",    '80' : "LG U+",    '81' : "LG U+",    '82' : "LG U+",
        '83' : "LG U+",    '84' : "LG U+",    '85' : "SKT",      '86' : "SKT",
        '87' : "SKT",      '88' : "SKT",      '89' : "SKT",      '90' : "SKT",
        '91' : "SKT",      '92' : "SKT",      '93' : "SKT",      '94' : "SKT",
        '95' : "KT",       '96' : "KT",       '97' : "KT",       '98' : "KT",
        '99' : "KT"
    }.get(key, "null")
    
    return telecom


def phone2carrier(phoneNumber):
    if isPhone(phoneNumber):
        print("입력된 전화번호: " + phoneNumber + "\n")
    else:
        print("전화번호를 확인하고 다시 입력해 주세요.\n")
        return "wrong number"

    phone = phoneNumber.split("-")
    
    if carrier(str(phone[1])[:2]) != "null":
        print("\n해당 전화번호는 " + carrier(str(phone[1])[:2]) + "로 가입된 전화번호입니다.\n")
        print("위 정보는 개통 기준 정보임으로 현재는 변경되었을 수도 있습니다.")
        return carrier(str(phone[1])[:2])
    else:
        print("\n해당 전화번호는 없는 번호 입니다")
        return "invalid";


phoneNumber = "010-2000-0000" # 010-****-**** 형식으로 입력

phone2carrier(phoneNumber)