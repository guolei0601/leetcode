<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-24
 * Time: 11:43
 */
class Solution {

    /**
     * @param String $s
     * @param String[] $words
     * @return Integer[]
     */
    function findSubstring($s, $words) {
        if(empty($words)) return [];
        $res = [];
        $words_len = strlen($words[0]);
        $words_num  = count($words);
        for($i =0;$i <= strlen($s) - $words_len * $words_num;$i++){
            $new_words = $words;
            $m = $i;
            $n = 0;
            while (!empty($new_words)){
                $cur_word  = substr($s,$m,$words_len);
                $has_word  = array_keys($new_words,$cur_word);
                if (empty($has_word)){
                    break;
                }else{
                    unset($new_words[$has_word[0]]);
                    $m += $words_len;
                    $n++;
                }
            }
            if($n == $words_num){
                $res[] = $i;
            }
        }
        return $res;
    }
}
$obj = new Solution();
var_dump($obj->findSubstring("barfoothefoobarman",["foo","bar"]));