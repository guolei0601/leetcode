<?php
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
    function addTwoNumbers($l1, $l2) {

        //分别获取num1 和 num2 的值
        $l1_new = $l1;
        $l2_new = $l2;
        //进位，默认是0
        $add = 0;
        $cur_num = 0;
        $res = null;
        if($l1_new->next == null && $l2_new->next == null){
            $a1 = $l1_new->val;
            $a2 = $l2_new->val;
            if($a1 + $a2 >= 10){
                $cur_num = $a1 + $a2 - 10;
                $add = 1;
                $res = new ListNode($cur_num);
            }else{
                $cur_num = $a1 + $a2;
                $add = 0;
                $res= new ListNode($cur_num);
            }
            $cur =$res;
        }else{
            //print_r(111);
            while($l1_new or $l2_new){

                //获取l1
                if(empty($l1_new)){
                    $a1 = 0;
                }else{

                    $a1 = $l1_new->val;
                    $l1_new = $l1_new->next;
                }
                //var_dump($a1);

                //获取l2
                if(empty($l2_new)){
                    $a2 = 0;
                }else{

                    $a2 = $l2_new->val;
                    $l2_new = $l2_new->next;
                }

                //var_dump($a2);
                if($a1 + $a2 + $add >= 10){
                    $cur_num = $a1 + $a2 + $add - 10;
                    $add = 1;
                }else{
                    $cur_num = $a1 + $a2 + $add;
                    $add = 0;
                }

                //var_dump($cur_num);

                $node =  new ListNode($cur_num);
                if(empty($res)){
                    $cur = $res = $node;
                }else{
                    $cur->next =  $node;
                    $cur = $cur->next;
                }
            }
        }

        //最后一个节点
        if($add == 1){
            $cur->next = new ListNode(1);
        }
        return $res;
    }

}



class ListNode{
    public $val = 0;
    public $next = null;
    function __construct($val)
    {
        $this->val = $val;
    }
}

#$a = array(3,4,5);
#$b = array(4,7,8);
$a = new ListNode(5);
//$a->next = new ListNode(4);
//$a->next->next = new ListNode(3);
$b = new ListNode(5);
//$b->next = new ListNode(6);
//$b->next->next = new ListNode(4);

$so = new Solution();
$res = $so->addTwoNumbers($a,$b);
var_dump($res->val);
while ($res->next){
    $res = $res->next;
    var_dump($res->val);
}

