<?php
/**
 * 基本思路：
 * A               |              B
 * A[0]...A[i-1]   |  A[i]...A[m-1]
 * B[0]...B[j-1]   |  B[j]...B[n-1]
 * 其中 i + j  = m-i + n-i + 1 （默认右边多1）
 * 其中 A[i-1] <= B[j]  && A[i] >= B[j-1]
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-01
 * Time: 22:28
 */
class Solution{


    function findMedianSortedArrays($nums1, $nums2) {
        $total_1 = count($nums1);
        $total_2 = count($nums2);
        //把长数组赋值给A
        if($total_1 < $total_2){
            $arr_A = $nums1;
            $arr_B = $nums2;
            $total_A = $total_1;
            $total_B = $total_2;
        }else{
            $arr_A = $nums2;
            $arr_B = $nums1;
            $total_A = $total_2;
            $total_B = $total_1;
        }
        $min_pos = 0;
        $max_pos = $total_A;
        $half = intval(($total_A + $total_B + 1 )/2);
        //exit;
        while($min_pos <= $max_pos){
            $i = intval(($min_pos + $max_pos) / 2) ;//从中间开始查
            $j =  $half - $i ;
            if( $i < $max_pos  &&  $arr_B[$j-1] > $arr_A[$i] ){
                $min_pos = $i + 1 ;
            }elseif($i > $min_pos  && $arr_A[$i-1] > $arr_B[$j]  ){
                $max_pos = $i - 1 ;
            }else{
                //找到了正确的位置，这时候需要考虑一下临界条件
                $max_left = 0.0;
                if($i == 0 ){ $max_left = $arr_B[$j -1];}
                elseif ($j == 0 ){$max_left = $arr_A[$i -1];}
                else{
                    $min_A = isset($arr_A[$i-1]) ?  $arr_A[$i-1] :0;
                    $min_B = isset($arr_B[$j -1]) ?  $arr_B[$j-1] : 0;
                    $max_left = max($min_A,$min_B);
                }
                //var_dump($max_left);
                if(($total_2 + $total_1)% 2 == 1){return $max_left;}

                $min_right = 0.0;
                if($i == $total_A && $j >=0 ){$min_right = $arr_B[$j];}
                elseif($j == $total_B && $i < $total_A){$min_right = $arr_A[$i];}
                else{$min_right = min($arr_A[$i],$arr_B[$j]);}
                //var_dump($min_right);
                return ($max_left + $min_right)/2.0;
            }
        }
        return 0.0;

    }

}

$obj = new Solution();
$res = $obj->findMedianSortedArrays([],[2]);
var_dump($res);