<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-05
 * Time: 20:00
 */
class Solution {

    /**
     * @param String $str
     * @return Integer
     */
    function myAtoi($str) {
        //$str = str_replace(' ','',$str);
        $start = 0;
        $flag = false;
        for ($m = 0;$m < strlen($str);$m++){
            if($str[$m] != ' '){
                $start = $m;
                $flag = true;
                break;
            }
        }
        if($flag == false) return 0;
        $str = substr($str,$start);

        $len = strlen($str);
        $first = "";
        if(in_array($str[0],['-','+','0','1','2','3','4','5','6','7','8','9'])){
            $first = $str[0];
        }elseif($str[0] != " "){
            return 0;
        }
        $str_num = "";
        for ($i=1;$i<$len;$i++){
            if(in_array($str[$i],['0','1','2','3','4','5','6','7','8','9'])){
                $str_num .= $str[$i];
            }else{
                break;
            }
        }
        $str_num = str_replace(' ','',$first . $str_num);
        if(strlen($str_num) == 0){
            return 0;
        }elseif(strlen($str_num) == 1 && ($str_num == '-' || $str_num == '+')){
            return 0;
        }else{
            $is_num = false;
            $symbol = "";
            if($str_num[0] == '-'){
                $symbol = '-';
                $str_num = substr($str_num,1);
            }elseif ($str_num[0] == '+'){
                $str_num = substr($str_num,1);
            }

            $num_len = strlen($str_num);
            for($j=0;$j<$num_len;$j++){
                if($num_len[$j] != '0'){
                    $is_num = true;
                    break;
                }
            }
            if(!$is_num){
                return 0;
            }else{
                $result =  intval($symbol.substr($str_num,$j));
                if($result > pow(2,31) -1 or $result < -1 * pow(2,31)){
                    if($result > 0) return pow(2,31) -1;
                    else return -1 * pow(2,31);
                }else{
                    return $result;
                }
            }
        }
    }
}

$str = " 42 ";
$str = "   -42";
//$str = "4193 with words";
//$str = "words and 987";
//$str = "-91283472332";
$obj = new Solution();
var_dump($obj->myAtoi($str));