from DoublyLinkedList import *
def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2): 
    def merge_sublists(srt_sublist1,srt_sublist2):
        result = DoublyLinkedList()
        if srt_sublist1 is not None and srt_sublist2is not None:
            if srt_sublist1.data < srt_sublist2.data:
                result.add_last(srt_sublist1.data)
                return merge_sublists(srt_sublist1.next, srt_sublist2)
            else:
                result.add_last(srt_sublist2.data)
                return merge_sublists(srt_sublist1, srt_sublist2.next)
        elif a is not None:
            result.add_last(srt_sublist1.data)
            return merge_sublists(srt_sublist1.next, srt_sublist2)
        elif srt_sublist2 is not None:
            result.add_last(srt_sublist2.data)
            return merge_sublists(srt_sublist1, srt_sublist2.next)
        return result
    return merge_sublists(srt_lnk_lst1.first_node(), srt_lnk_lst2.first_node())



