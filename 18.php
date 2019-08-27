<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 21:36
 */
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[][]
     */
    function fourSum($nums, $target) {
        $res = [];
        sort($nums);
        //var_dump($nums);
        //exit;
        $in = [];
        for ($i = 0;$i<count($nums);$i++){
            for ($j =$i+1;$j < count($nums);$j++){
                $l = $j + 1;
                $r = count($nums) - 1;
                while ($l < $r){
                    if($nums[$i] + $nums[$j] + $nums[$l] + $nums[$r] == $target){
                        if(!in_array($nums[$i] . $nums[$j].$nums[$l] . $nums[$r],$in)){
                            $res[]= [$nums[$i] , $nums[$j] , $nums[$l] , $nums[$r]];
                            $in[] = $nums[$i] . $nums[$j].$nums[$l] . $nums[$r];
                            //var_dump($in);
                            //exit;
                        }
                        $r--;
                        $l++;
                    }elseif($nums[$i] + $nums[$j] + $nums[$l] + $nums[$r] > $target){
                        $r--;
                    }else{
                        $l++;
                    }
                }
            }
        }
        return $res;
    }
}

$obj = new Solution();
$arr = [0,0,0,0];
$target = 0;
var_dump($obj->fourSum($arr,$target));