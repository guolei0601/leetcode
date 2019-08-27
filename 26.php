<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-23
 * Time: 20:05
 */
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
        $pre = "";
        $total = 0;
        $len = count($nums);
        for($i=0;$i<$len;$i++){
            if($i==0){
                $pre = $nums[$i];
                $total++;
            }else{
                if($pre == $nums[$i]){
                    unset($nums[$i]);
                }else{
                    $pre = $nums[$i];
                    $total++;
                }
            }
        }
        return $total;
    }
}

$obj = new Solution();
$nums =[0,0,1,1,1,2,2,3,3,4,5];
var_dump($obj->removeDuplicates($nums));