<?php
/**
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-23
 * Time: 17:24
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
     * @param ListNode[] $lists
     * @return ListNode
     */
    function mergeKLists($lists) {
        if(empty($lists)) return null;
        $nums = [];
        //所有数据输入到数组
        foreach ($lists as $val){
            $cur = $val;
            while ($cur){
                $num = $cur->val;
                $cur = $cur->next;
                $nums[] = $num;
            }
        }
        //快排
        sort($nums);
        //创建新list
        $res = $l = new ListNode(0);
        foreach ($nums as $val){
            $new_l = new ListNode($val);
            $l->next = $new_l;
            $l = $l->next;
        }
        return $res->next;
    }
}