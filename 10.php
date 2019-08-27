<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-19
 * Time: 17:13
 */
class Solution {

    /**
     * @param String $s
     * @param String $p
     * @return Boolean
     */
    function isMatch($s, $p) {
        if(empty($p)) return empty($s);
        if(strlen($p) ==1) return (strlen($s) == 1 && ($s == $p || $p == '.'));
        if($p[1] != '*'){
            if(empty($s)) return false;
            return ($s[0] == $p[0] || $p[0] == '.') && $this->isMatch(substr($s,1),substr($p,1));
        }
        while(!empty($s) && ($s[0] == $p[0] || $p[0] == '.')){
            if($this->isMatch($s,substr($p,2))) return true;
            $s = substr($s,1);
        }
        return $this->isMatch($s,substr($p,2));
    }

}


$s = "mississippi";
$p = "mis*is*ip*.";

$obj = new Solution();
var_dump($obj->isMatch($s,$p));
