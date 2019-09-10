import DoublyLinkedList

srt_lnk_lst = DoublyLinkedList()

def insert_sorted(srt_lnk_lst, elem):

    A = srt_lnk_lst.header.next

    # search through list
    while (A != srt_lnk_lst.trailer and A.data < elem.data):
        A = A.next

    temp = A.prev
    temp.next = elem
    elem.prev = temp
    elem.next = A
    A.prev = elem
