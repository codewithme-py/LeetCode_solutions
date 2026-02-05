import pytest

from solutions.add_two_numbers_0002 import ListNode, Solution


def create_linked_list(values: list[int]) -> ListNode | None:
    """Create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_values(head: ListNode | None) -> list[int]:
    """Convert a linked list to a list of values."""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


@pytest.mark.parametrize('l1_vals, l2_vals, expected_vals', [
    ([2,4,3], [5,6,4], [7,0,8]),
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
])
def test_solution(l1_vals, l2_vals, expected_vals):
    """Test the addTwoNumbers method with various inputs."""
    sol = Solution()
    l1 = create_linked_list(l1_vals)
    l2 = create_linked_list(l2_vals)
    result = sol.addTwoNumbers(l1, l2)
    assert linked_list_to_values(result) == expected_vals
