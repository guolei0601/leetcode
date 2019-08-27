<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-23
 * Time: 15:41
 */
class Solution {

    /**
     * @param Integer $n
     * @return String[]
     */
    function generateParenthesis($n) {

        if($n <=0) return [];
        $res = [];
        $num  = 0;
        while ($num < $n *2){
            $num++;
            //首次是0的情况
            if(empty($res)) {
                $res = ['('=>array(1,0)];//入左括号
                continue;
            }
            $new_res = [];
            foreach ($res as $key => $val){
                $left = $val[0];
                $right=$val[1];
                if($left < $n){$new_res[$key.'(']= array($left+1,$right);};
                if($left > $right){$new_res[$key.')'] = array($left,$right+1);}
            }
            $res = $new_res;
            unset($new_res);
        }
        return array_keys($res);
    }
}

$obj = new Solution();
$n = 3;
var_dump($obj->generateParenthesis($n));