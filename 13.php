<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 14:27
 */
class Solution {

    /**
     * @param Integer $num
     * @return String
     */
    function romanToInt($s) {
        $res = 0;
        $all = ['1'=>'I','2'=>'II','3'=>'III','4'=>'IV','5'=>'V','6'=>'VI','7'=>'VII','8'=>'VIII','9'=>'IX',
                '10'=>'X','20'=>'XX','30'=>'XXX','40'=>'XL','50'=>'L','60'=>'LX','70'=>'LXX','80'=>'LXXX','90'=>'XC',
                '100'=>'C','200'=>'CC','300'=>'CCC','400'=>'CD','500'=>'D','600'=>'DC','700'=>'DCC','800'=>'DCCC','900'=>'CM',
            '1000'=>'M','2000'=>'MM','3000'=>'MMM'
        ];
        $res = "";
        while (!empty($s)){
            $res += $this->_getCurNum($s,$all);
        }
        return $res;
    }

    function _getCurNum(&$s,$all){
        //var_dump($all);
        $res = "";
        $one_c = substr($s,0,1);
        $two_c = substr($s,0,2);
        $three_c = substr($s,0,3);
        $four_c  = substr($s,0,4);
        if(in_array($four_c,$all)){
            $s = substr($s,4);
            $res =  array_search($four_c,$all);
        }elseif(in_array($three_c,$all)){
            $s = substr($s,3);
            $res =  array_search($three_c,$all);
        }elseif(in_array($two_c,$all)){
            $s = substr($s,2);
            $res =  array_search($two_c,$all);
        }else{
            $s = substr($s,1);
            $res =  array_search($one_c,$all);
        }
        return intval($res);
    }
}

$obj = new Solution();
$num = 'MCMXCIV';
var_dump($obj->romanToInt($num));