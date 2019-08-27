<?php
/**
 * 用堆栈的方式，遇到右括号就出栈，左括号就进栈
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 23:33
 */
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $cur_arr = [];
        for($i=0;$i<strlen($s);$i++){
            if(in_array($s[$i],['(','{','['])){
                $cur_arr[] = $s[$i];
            }else{
                $char = array_pop($cur_arr);
                switch ($s[$i]){
                    case ')':  if($char != '(') return false ; break;
                    case ']':  if($char != '[') return false ; break;
                    case '}':  if($char != '{') return false ; break;
                }
            }
        }
        if(!empty($cur_arr)) return false;
        return true;
    }
}
