<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-03-27
 * Time: 13:39
 */
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Float
     */
    function findMedianSortedArrays($nums1, $nums2) {
        $res = array();
        $total_1 = count($nums1);
        $total_2 = count($nums2);
        $total = $total_1 + $total_2;
        //定义3个变量，分别表示数组1，2比较到的位置，以及数组res存储到了哪个位置
        $nums1_pos = 0;
        $nums1_pos = 0;
        $nums2_pos = 0;
        while(true){
            while ($nums1[$nums1_pos] < $nums2[$nums2_pos]  && $nums1_pos < $total_1 ){
                $res[] = $nums1[$nums1_pos];
                $nums1_pos++;
            }
            //var_dump($nums1_pos);
            if($nums1_pos >= $total_1) break;
            while ($nums1[$nums1_pos] >= $nums2[$nums2_pos]  && $nums2_pos < $total_2  ){
                $res[] = $nums2[$nums2_pos];
                $nums2_pos++;

            }
            //var_dump($nums2_pos);
            if($nums2_pos >= $total_2) break;
        }


        //var_dump($nums2_pos);
        //exit;
        //var_dump($nums1_pos);
        //var_dump($nums2_pos);
        //如果有一方比较完了，另一个数组还没比较完，就直接赋值
        if($nums1_pos >= $total_1){
            for(;$nums2_pos<$total_2;$nums2_pos++){
                $res[] = $nums2[$nums2_pos];
            }
        }else{
            for(;$nums1_pos<$total_1;$nums1_pos++){
                $res[] = $nums1[$nums1_pos];
            }
        }

        //求中位数
        if($total % 2 == 0){
            return ($res[$total/2] + $res[$total/2 -1]) /2.0;
        }else{
            return $res[($total-1)/2]/1.0;
        }
    }

}

$nums1 = [1,3];

$nums2 = [2];

$obj = new Solution();

var_dump($obj->findMedianSortedArrays($nums1,$nums2));