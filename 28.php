<?php
/**
 * 该题太初级~
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-23
 * Time: 20:43
 */
class Solution {

    /**
     * @param String $haystack
     * @param String $needle
     * @return Integer
     */
    function strStr($haystack, $needle) {
        if( $needle == "") return 0;
        $res = strpos($haystack,$needle);
        return  $res === false ? -1 : $res ;
    }
}