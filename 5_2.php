<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-03
 * Time: 17:39
 */
<?php
/**使用动态规划方法求解最长回文串
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-03
 * Time: 10:55
 */

class Solution {

    /**
     * @param String $s
     * @return String
     */
    function longestPalindrome($s) {
        $total = strlen($s);
        if($total == 0){
            return "";
        }else{
            $data = array();//记录每个子串是否是回文串,不是就不赋值，是就赋值
            $res  = "";//记录结果的左右位置
            $left = 0;
            $max_len = 0;
            //获取长度为i的子字符串的最长子串
            for($i=0;$i<=$total;$i++){
                for($j=0;$)
                $this->subPalindrome($s,$data,$left,$max_len,$total,$i);
            }
        }
        //print_r()
        return substr($s,$left,$max_len);
        //return [$left,$max_len];
    }

    function subPalindrome($s,&$data,&$left,&$max_len,$total,$num){
        //是1则直接返回
        if($num == 1){
            for($m=0;$m<$total;$m++){
                $data[$m][$m] = true;
            }
        }
        //是2则判断左右是否相等
        elseif ($num == 2){
            for($m =0;$m+1<$total;$m++){
                if($s[$m] == $s[$m+1]){
                    $data[$m][$m+1] = true;
                    $max_len = 2;
                    $left = $m;
                }
            }
        }
        //其他则判断左+1,右-1判断是否回文，然后左右各加1个字符串判断是否回文
        else{
            for($m = 0; $m + $num -1 < $total;$m ++){
                if($data[$m+1][$m+$num-2] && $s[$m] == $s[$m+$num-1]){
                    $data[$m][$m+$num-1] = true;
                    $max_len = $num;
                    $left = $m;
                }
            }
        }
    }

}

$obj = new Solution();
$s = "miycvxmqggnmmcwlmizfojwrurwhwygwfykyefxbgveixykdebenzitqnciigfjgrzzbtgeazyrbiirmejhdwcgjzwqolrturjlqpsgunuqerqjevbheblmbvgxyedxshswsokbhzapfuojgyfhctlaifrisgzqlczageirnukgnmnbwogknyyuynwsuwbumdmoqwxprykmazghcpmkdcjduepjmjdxrhvixxbfvhybjdpvwjbarmbqypsylgtzyuiqkexgvirzylydrhrmuwpmfkvqllqvekyojoacvyrzjevaupypfrdguhukzuqojolvycgpjaendfetkgtojepelhcltorueawwjpltehbbjrvznxhahtuaeuairvuklctuhcyzomwrrznrcqmovanxmiyilefybkbveesrxkmqrqkowyrimuejqtikcjfhizsmumajbqglxrvevexnleflocxoqgoyrzgqflwiknntdcykuvdcpzlakljidclhkllftxpinpvbngtexngdtntunzgahuvfnqjedcafzouopiixw";
//$s ="ab";
$s = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee";
var_dump($obj->longestPalindrome($s));
echo 111;