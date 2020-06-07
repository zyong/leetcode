import java.util.Set;

import javax.management.ListenerNotFoundException;
import javax.swing.event.ListDataEvent;

/*
 * @lc app=leetcode.cn id=25 lang=java
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode hair = new ListNode();
        hair.next = head;
        ListNode pre = hair;
        while (head != null) {
            ListNode tail = pre;
            for (int i=0; i<k; i++) {
                tail = tail.next;
                if (tail == null) {
                    return hair.next;
                }
            }
            ListNode next = tail.next;
            Pair<ListNode> result = reverse(head, tail);
            head = result.first;
            tail = result.second;
            pre.next = head;
            tail.next = next;
            // 下一轮从上一轮的尾部开始，同时上一轮尾部的下一个为新的头部
            pre = tail;
            head = tail.next;
        }
        return hair.next;

    }

    // 原始的头部元素要指向原来的尾部元素的下一个，
    // 1->2->3->4   2->1->3->4
    private Pair<ListNode> reverse(ListNode head, ListNode tail) {
        ListNode prev = tail.next;
        ListNode p = head;
        ListNode next = new ListNode();
        while (prev != tail) {
            next = p.next;
            p.next = prev;
            prev = p;
            p = next;
        }
        return new Pair(tail, head);
    }

    class Pair<T> {
        public T first;
        public T second;
        public Pair(T a, T b) {
            this.first = a;
            this.second = b;
        }
    }
}
// @lc code=end

