<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-05
 * Time: 19:02
 */
class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {

        $max = pow(2,31) -1;
        $min = -1 * pow(2,31);
        if($x > $max  or $x < $min)
            return 0;
        $res = "";
        $symbol = "";
        $str_new = $str = strval($x);
        $len = strlen($str);
        if($str[0] == '-'){
            $symbol = '-';
            $str_new = substr($str,1);
        }
        $rev_str = strrev($str_new);
        if($rev_str[0] == '0'){
            $rev_str = substr($rev_str,1);
        }
        $new_num = intval($symbol .$rev_str);
        if($new_num > $max or $new_num < $min){
            return 0;
        }
        return $new_num;
    }
}

$num = 120;
$obj = new Solution();
var_dump($obj->reverse($num));