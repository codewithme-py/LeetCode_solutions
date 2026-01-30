from solutions.remove_duplicates_from_sorted_list_0083 import ListNode, Solution


def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def test_delete_duplicates():
    sol = Solution()

    head1 = list_to_linked_list([1, 1, 2])
    result1 = sol.deleteDuplicates(head1)
    assert linked_list_to_list(result1) == [1, 2]

    head2 = list_to_linked_list([1, 1, 2, 3, 3])
    result2 = sol.deleteDuplicates(head2)
    assert linked_list_to_list(result2) == [1, 2, 3]

    assert sol.deleteDuplicates(None) is None

    head3 = ListNode(5)
    result3 = sol.deleteDuplicates(head3)
    assert linked_list_to_list(result3) == [5]

    head4 = list_to_linked_list([7, 7, 7, 7])
    result4 = sol.deleteDuplicates(head4)
    assert linked_list_to_list(result4) == [7]

    head5 = list_to_linked_list([1, 2, 3, 4])
    result5 = sol.deleteDuplicates(head5)
    assert linked_list_to_list(result5) == [1, 2, 3, 4]
