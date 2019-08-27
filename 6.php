<?php
/**
 * leecode-5
 * 思路：创建n个数组，分别存储每行的字符，然后从第一个数组依次遍历输出结果
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-05
 * Time: 17:57
 */
class Solution {

    /**
     * @param String $s
     * @param Integer $numRows
     * @return String
     */
    function convert($s, $numRows) {
        $data = array();
        $result = "";
        $cur_line = 0 ;//记录当前该写入的行数
        $direction = 0 ;//0正向，1反向
        for($i = 0; $i < strlen($s);$i++){
            if($direction ==0){
                $data[$cur_line++][] = $s[$i];
            }else{
                $data[$cur_line--][] = $s[$i];
            }
            if($cur_line == -1){
                $direction = 0;
                $cur_line+=2;
            }elseif ($cur_line == $numRows){
                $direction = 1;
                $cur_line-=2;
            }
        }
        foreach ($data as $val){
            foreach ($val as $v){
                $result .= $v;
            }
        }
        return $result;
    }
}

$str = "LEETCODEISHIRING";
$obj = new Solution();
$obj->convert($str,4);
