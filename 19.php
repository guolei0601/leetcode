<?php
/**注意创建新的头指针
 * Created by PhpStorm.
 * User: guolei09
 * Date: 2019-04-22
 * Time: 22:29
 */

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */

 class ListNode {
     public $val = 0;
     public $next = null;
     function __construct($val) {
         $this->val = $val;
     }
 }

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
     * @param Integer $n
     * @return ListNode
     */
    function removeNthFromEnd($head, $n) {
        $first_pointer = $head;
        $second_pointer = $head;
        $res = $new = new ListNode(0);
        $new->next = $second_pointer;
        $new = $new->next;
        for ($i=0;$i<$n-1;$i++){
            $first_pointer = $first_pointer->next;
        }
        if($first_pointer->next == null) {return $second_pointer->next; }
        while ($first_pointer->next){
            $first_pointer = $first_pointer->next;
            if($first_pointer->next == null){
                $second_pointer = $second_pointer->next->next;
            }else{
                $second_pointer = $second_pointer->next;
            }
            $new->next = $second_pointer;
            $new  = $new->next;
        }
        return $res->next;
    }
}