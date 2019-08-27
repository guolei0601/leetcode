<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 16:57
 */
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function threeSum($nums) {
        $new_arr = [];
        $res = [];
        //构造哈希表
        foreach ($nums as $val){
            $new_arr[$val] = empty($new_arr[$val]) ? 1 : $new_arr[$val] + 1;
        }
        ksort($new_arr);
//        foreach ($new_arr as $v){
//            print_r($v ."\n");
//        }
        //var_dump($new_arr);
        //$a <= $b <= $c
        foreach ($new_arr as $key => $val){
            $a = $key;
            foreach($new_arr as $key_1 => $val_1){
                $b = $key_1;
                $c = 0 - $a - $b;
                //var_dump($a ."\t".$b."\t".$c);
                if(!empty($new_arr[$c]) &&  $a<=$b && $b <= $c){
                    if(($a == $c && $new_arr[$c] >= 2) || ($c == $b && $new_arr[$c] >= 2) || ($a == $b && $new_arr[$a] >=2) || ($a != $b && $b != $c)){
                        if($a == $b && $b == $c && $a == 0){
                            continue;
                        }else{
                            $cur = [$a,$b,$c];
                            $res[] = $cur;
                        }

                    }
                }
            }
        }
        if(!empty($new_arr['0']) && $new_arr['0'] >= 3) {$res[] = [0,0,0];}
        return $res;
    }
}

$obj = new Solution();
$arr = [1,1,-2];
var_dump($obj->threeSum($arr));

