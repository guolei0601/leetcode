<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 19:45
 */
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function threeSumClosest($nums, $target) {
        $res = [];
        $min = "";
        sort($nums);
        //var_dump($nums);
        //$a <= $b <= $c
        for($i = 0; $i < count($nums); $i++){
            $a = $nums[$i];
            $l = $i + 1;
            $r = count($nums) -1;
            while($l < $r){
                $now_sum = $nums[$i] + $nums[$r] + $nums[$l];
                //var_dump($nums[$i]."\t".$nums[$l]."\t".$nums[$r]);
                if($l < $r && (empty($min) || abs($now_sum - $target) < $min)){
                    $min = abs($now_sum - $target);
                    $res = [$nums[$i],$nums[$l],$nums[$r]];
                }
                if($nums[$l] + $nums[$r] + $a > $target){
                    $r--;
                }elseif($nums[$l] + $nums[$r] + $a < $target){
                    $l++;
                }elseif($nums[$l] + $nums[$r] + $a == $target){
                    return $target;
                }
            }
        }
        return $res[0] + $res[1] + $res[2];
    }
}

$obj = new Solution();
$arr = [-1,2,1,-4];
$target = 1;
var_dump($obj->threeSumClosest($arr,$target));