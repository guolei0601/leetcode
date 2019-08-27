<?php
/**
 * 使用常见的双指针法解决 $i，$j分别是慢指针和快指针
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-23
 * Time: 20:26
 */
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val) {
        $i = 0;
        for($j=0;$j<count($nums);$j++){
            if($nums[$j] != $val){
                $nums[$i++] = $nums[$j];
            }
        }
        //注意返回的是$i，而不是count($nums)
        return $i;
    }
}