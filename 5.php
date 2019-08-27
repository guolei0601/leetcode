<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-03-27
 * Time: 15:33
 */
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestPalindrome($s) {
        if(strlen($s) <= 1){
            return $s;
        }
        for($i = strlen($s);$i>=1;$i--){
            $j = 0;
            while(strlen(substr($s,$j,$i)) == $i){
                $cur_res = substr($s,$j,$i);
//                var_dump($cur_res);
                if($cur_res == strrev($cur_res)){
                    return $cur_res;
                }
                $j++;
            }
        }
    }

}

$obj = new Solution();
$s = "miycvxmqggnmmcwlmizfojwrurwhwygwfykyefxbgveixykdebenzitqnciigfjgrzzbtgeazyrbiirmejhdwcgjzwqolrturjlqpsgunuqerqjevbheblmbvgxyedxshswsokbhzapfuojgyfhctlaifrisgzqlczageirnukgnmnbwogknyyuynwsuwbumdmoqwxprykmazghcpmkdcjduepjmjdxrhvixxbfvhybjdpvwjbarmbqypsylgtzyuiqkexgvirzylydrhrmuwpmfkvqllqvekyojoacvyrzjevaupypfrdguhukzuqojolvycgpjaendfetkgtojepelhcltorueawwjpltehbbjrvznxhahtuaeuairvuklctuhcyzomwrrznrcqmovanxmiyilefybkbveesrxkmqrqkowyrimuejqtikcjfhizsmumajbqglxrvevexnleflocxoqgoyrzgqflwiknntdcykuvdcpzlakljidclhkllftxpinpvbngtexngdtntunzgahuvfnqjedcafzouopiixw";
var_dump($obj->longestPalindrome($s));
echo 111;