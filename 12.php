<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 13:49
 */
class Solution
{

    /**
     * @param Integer $num
     * @return String
     */
    function intToRoman($num)
    {
        $thousand = ['', 'M', 'MM', 'MMM'];
        $handred = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'];
        $ten = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'];
        $single = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'];
        $res = "";
        $num_str = "" . $num;
        $total_num = strlen($num_str);
        $t_num = 0;
        $h_num = 0;
        $te_num = 0;
        $s_num = 0;
        if ($total_num == 4) {
            $t_num = substr($num_str, 0, 1);
            $h_num = substr($num_str, 1, 1);
            $te_num = substr($num_str, 2, 1);
            $s_num = substr($num_str, 3, 1);
        } elseif ($total_num == 3) {
            $h_num = substr($num_str, 0, 1);
            $te_num = substr($num_str, 1, 1);
            $s_num = substr($num_str, 2, 1);
        } elseif ($total_num == 2) {
            $te_num = substr($num_str, 0, 1);
            $s_num = substr($num_str, 1, 1);

        } else {
            $s_num = substr($num_str, 0, 1);
        }
        return $thousand[$t_num] . $handred[$h_num] . $ten[$te_num] . $single[$s_num];
    }

    }
$obj = new Solution();
$num = 58;
var_dump($obj->intToRoman($num));