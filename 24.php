<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-23
 * Time: 17:37
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
     * @return ListNode
     */
    function swapPairs($head) {
        $res = $new_res = new ListNode(0);
        $cur = $head;
        while($cur && $cur->next){
            $num_1 = $cur->val;
            $num_2 = $cur->next->val;
            $cur = $cur->next->next;
            $new_res->next = new ListNode($num_2);
            $new_res->next->next = new ListNode($num_1);
            $new_res = $new_res->next->next;
        }
        if($cur){
            $num_3 = $cur->val;
            $new_res->next = new ListNode($num_3);
        }
        return $res->next;
    }
}