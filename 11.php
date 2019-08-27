<?php
/**
 * 暴力求解 n^2 超时，用另一种o(n)的方式求解
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 11:11
 */
class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
//    function maxArea($height) {
//        $res = 0;
//        for($i=0;$i<count($height);$i++){
//            for($j = $i+1; $j<count($height);$j++){
//                $res = max ( min($height[$i],$height[$j]) * ($j - $i),$res);
//            }
//        }
//        return $res;
//    }

    function maxArea($height){
        $m = 0;
        $total = count($height);
        $n = $total - 1;
        $res = 0;
        while ($m < $n){
            $left = $height[$m];
            $right = $height[$n];
            if($left < $right){
                $res =  max (($n - $m) * $left ,$res);
                $m ++ ;
            }else{
                $res =  max (($n - $m) * $right,$res);
                $n --;
            }
        }
        return $res;
    }
}

$arr = [1,8,6,2,5,4,8,3,7];
$obj = new Solution();
var_dump($obj->maxArea($arr));
