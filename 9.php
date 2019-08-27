<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-05
 * Time: 21:35
 */
class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        return  $x == strrev($x) ?  true : false;
    }
}


$str = "12321";
$obj = new Solution();
var_dump($obj->isPalindrome($str));