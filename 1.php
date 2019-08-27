<?php
/**
 * @param integet[] $nums
 * @param Integer[] $target
 * @return Integer[]
 */
function twoSum($nums ,$target){
    $res = array();
    for($i=0;$i<count($nums);$i++){
        for($j=$i+1;$j<count($nums);$j++){
            if($nums[$i] + $nums[$j] == $target){
                $res[] = $i;
                $res[] = $j;
                break 2;
            }
        }
    }
    return $res;
}

$nums = array(2,7,11,15);
$target = 9 ;
print_r(twoSum($nums,$target));