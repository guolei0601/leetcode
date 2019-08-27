<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-03-25
 * Time: 12:41
 */
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring_1($s) {
        $res = array();
        $total = 0;
        for ($i=0;$i<strlen($s);$i++){
            $char = $s[$i];
            //如果array里面有了，就重新给array赋值，并更新总长度

            for($j = 0 ;$j< count($res);$j++){
                if($res[$j] == $char){
                    break;
                }
            }
            if($j < count($res)){
                if(count($res) > $total){
                    $total = count($res);
                }
                //注意这里不是unset，而是重新给数组赋值为从上一次重复到这一次的值
                $res_new = array();
                for($k=$j+1;$k<count($res);$k++){
                    $res_new[] = $res[$k];
                }
                unset($res);
                $res = $res_new;
            }
            $res[] = $char;
        }
        //末尾那次没进行计算，需要加上
        if(count($res) > $total){
            $total = count($res);
        }
        return $total;
    }



    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring_2($s) {
        $res = "";
        $total = 0;
        for ($i=0;$i<strlen($s);$i++){
            $char = $s[$i];
            $pos  = strpos($res,$char);
            //字符串中有，则计算当前总长度，并重新定义字符串
            if($pos!== false){
                $cur_total = strlen($res);
                $res   = substr($res,$pos +1) .$char;
            }else {
                //如果字符串没有，则加到字符串末尾
                $res .= $char;
            }
            $total = $cur_total > $total ? $cur_total:$total;
        }

        return $total > strlen($res) ? $total: strlen($res);
    }


    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s) {
        $res = "";
        $total = 0;
        for ($i=0;$i<strlen($s);$i++){
            //字符串中有，则计算当前总长度，并重新定义字符串
            $res =  strpos($res,$s[$i]) === false ? $res.$s[$i] : substr($res,strpos($res,$s[$i]) +1) . $s[$i];
            $total = strlen($res) > $total ? strlen($res) : $total;
        }
        return $total > strlen($res) ? $total: strlen($res);
    }
}

$obj = new Solution();
var_dump($obj->lengthOfLongestSubstring(" "));