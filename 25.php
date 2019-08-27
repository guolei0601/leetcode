<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-23
 * Time: 19:17
 */
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */
class Solution {

    /**
     * @param ListNode $head
     * @param Integer $k
     * @return ListNode
     */
    function reverseKGroup($head, $k) {
        if(empty($head)) return null;
        $l = $head;
        $res = $new_res = new ListNode(0);
        while (true){
            $cur = [];
            $cur_num = 0;
            while ($cur_num < $k && $l){
                $cur_num++;
                $num = $l->val;
                $l   = $l->next;
                $cur[] = $num;
            }
            if($cur_num == $k){
                for ($i=0;$i<$k;$i++){
                    $cur_val = array_pop($cur);
                    $node = new ListNode($cur_val);
                    $new_res->next = $node;
                    $new_res = $new_res->next;
                }
            }else{
                foreach ($cur as $val){
                    $node = new ListNode($val);
                    $new_res->next = $node;
                    $new_res = $new_res->next;
                }
                break;
            }

        }
        return $res->next;
    }
}