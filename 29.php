<?php
/**
 * 使用加法，超时。只能使用位移法 dividend = 2^n * divisor + left ，左移一位相当于乘以2
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-23
 * Time: 20:56
 */
class Solution {

    /**
     * @param Integer $dividend
     * @param Integer $divisor
     * @return Integer
     */
//    function divide($dividend, $divisor) {
//        $symbol = "";
//        if($divisor > 0 xor $dividend > 0){
//            $symbol = "-";
//        }
//        $dividend = abs($dividend);
//        $divisor  = abs($divisor);
//        $res = 0;
//        while ($dividend - $divisor >=0 ){
//            $res ++;
//            $dividend -= $divisor;
//        }
//        $res = intval($symbol.$res);
//        return $res > pow(2,31) -1 || $res < -1 * pow(2,31) ? pow(2,31) -1 : $res;
//    }
    function divide($dividend, $divisor) {
        $symbol = "";
        if($divisor > 0 xor $dividend > 0){
            $symbol = '-';
        }
        $dividend = abs($dividend);
        $divisor  = abs($divisor);
        $result = 0;
        while ($dividend >=$divisor){
            //$divisor_1 = $divisor<<1;
            $cur_res = 1;
            $divisor_1 = $divisor<<1;
            while ($dividend >= $divisor_1){
                $divisor_1 = $divisor_1<<1;
                $cur_res = $cur_res<<1;

            }

            $result += $cur_res;
            $divisor_1 = $divisor_1 >> 1;
            $dividend -=  $divisor_1;

        }
        $res = intval($symbol.$result);
        return $res > pow(2,31) -1 || $res < -1 * pow(2,31) ? pow(2,31) -1 : $res;
    }
}

$obj = new Solution();
$dividend = 120;
$divisor = 21;
var_dump($obj->divide($dividend,$divisor));