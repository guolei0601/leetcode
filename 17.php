<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 20:51
 */
class Solution {

    function letterCombinations($digits) {
        $res = [];
        if($digits == '') return [];
        var_dump(4);
        if(strlen($digits) == 1){
            $str = "";
            switch ($digits){
                case '2' : $str = 'a,b,c';break;
                case '3' : $str = 'd,e,f';break;
                case '4' : $str = 'g,h,i';break;
                case '5' : $str = 'j,k,l';break;
                case '6' : $str = 'm,n,o';break;
                case '7' : $str = 'p,q,r,s';break;
                case '8' : $str = 't,u,v';break;
                case '9' : $str = 'w,x,y,z';break;
            }
            return explode(',',$str);
        }else{
            $n = strlen($digits);
            $sub = substr($digits,0,1);
            $sub_o = substr($digits,1,$n -1);
            $sub_res = $this->letterCombinations($sub);
            $sub_res_o = $this->letterCombinations($sub_o);
            foreach ($sub_res as $v){
                foreach ($sub_res_o as $v_1){
                        $res[] = $v.$v_1;
                    }
                }
            return $res;
        }
    }
}

$obj = new Solution();
$str = "";
var_dump($obj->letterCombinations($str));