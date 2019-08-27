<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 23:43
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
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function mergeTwoLists($l1, $l2) {
        $res = $new_l = new ListNode(0);
        while($l1 && $l2){
            $v_1 = $l1->val;
            $v_2 = $l2->val;
            if($v_1 > $v_2){
                $cur = new ListNode($v_2);
                $new_l->next = $cur;
                $new_l = $new_l->next;
                $l2 = $l2->next;
            }else{
                $cur = new ListNode($v_1);
                $new_l->next = $cur;
                $new_l = $new_l->next;
                $l1 = $l1->next;
            }
        }
        while($l1){
            $num = $l1->val;
            $cur = new ListNode($num);
            $new_l->next = $cur;
            $new_l = $new_l->next;
            $l1 = $l1->next;
        }

        while ($l2){
            $num = $l2->val;
            $cur = new ListNode($num);
            $new_l->next = $cur;
            $new_l = $new_l->next;
            $l2 = $l2->next;
        }
        return $res->next;
    }
}