<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 15:43
 */
class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        $comm = "";
        if(empty($strs)){
            return "";
        }
        else{
            $comm = $strs[0];
        }
        foreach ($strs as $val){
            //var_dump($comm);
            $comm = $this->_getSubChars($comm,$val);
        }

        return $comm;
    }

    function _getSubChars($str_1,$str_2){
        $len = 0;
        for($i=0;$i< strlen($str_1);$i++){
            //var_dump($str_1[$i]);
            if($str_1[$i] != $str_2[$i]){
                break;
            }
            ++$len;
            //var_dump($len);
        }
        return substr($str_1,0,$len);
    }
}

$obj = new Solution();
$num = ["flower","flow","flight"];
var_dump($obj->longestCommonPrefix($num));