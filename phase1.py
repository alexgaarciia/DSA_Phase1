from slist import SList, SNode
import sys


class SList2(SList):
    def sumLastN(self, n):
        """This is a function that takes an integer n as input and returns the sum of the last n nodes of the calling
         list. If n<0, the function returns None. If the value of n is greater than the size of the list, the function
         returns the sum of all elements in the list."""

        # First off, several variables need to be defined in advance. Some of these are the variable "sum", that will
        # be the result of the sum; and "node", which will be used to go through the entire list.
        sum = 0
        node = self._head

        # Once the most important variables are defined, it is time to establish the conditions that the exercise is
        # asking for. Depending on the these conditions, certain actions will be performed. This exercise will be
        # developed in the following way: from the shortest and easiest case, to the longest and most difficult one.
        if n == 0:
            # This very first if-statement is used to return 0 in case the number of nodes to sum is 0.
            return 0
        elif n < 0:
            # Moving on with the exercise, it is vital to consider also the case in which a negative number is provided
            # by the user. In this case, None should be returned.
            return None
        elif n >= self._size:
            # Thirdly, in the case that the number of nodes to sum is higher than the size of the list, all of the
            # elements in the list should be added. For this, a while loop is used to go over the entire list. This
            # loop will stop once the node is None because this means that there will be no more nodes to add.
            while node:
                sum += node.elem
                node = node.next
        else:
            # Finally, the most important case of the ones exposed above is developed. This case corresponds to
            # when the number entered by the user is greater than 0 and less than the size of the list. As always,
            # several variales need to be defined. The counter variable "i" will be used for stopping at the last
            # node to add; and the variable "prev" (which is initially set to None) for reversing the list. More of
            # this will be explained in the portion of code from below.
            i = 0
            prev = None
            while node:
                # The initial thing that must be done is reversing the list. Why? What is the goal of performing such
                # operation? Easy! As the name of the function states "sumLastN", the main goal is to add the LAST
                # elements of the list. For this, the decision to reverse the list was taken so that there is an easier
                # access to the last nodes of the list.
                next = node.next
                node.next = prev
                prev = node
                node = next
            self._head = prev
            while i < n and prev:
                # This last while loop is used for the same as the one exposed in line 41, for adding all the elements.
                sum += prev.elem
                prev = prev.next
                i += 1

        # Finally, the sum is returned.
        return sum

    def insertMiddle(self, elem):
        """This is a function that inserts the element e in the middle of the calling list. If the size of the list is
         even, the new element should be inserted at position len(self)//2. If the size is odd, then the element should
         be inserted at position (len(self)+1)/2. If the list is empty, we simply add the element."""

        # First and foremost, several variables need to be defined in advance. Some of these are the variable "i" that
        # will be helpful for inserting the element in the loop from below; and "previous", which will be the previous
        # node to the one that is desired to be inserted.
        i = 0
        previous = self._head

        # For this exercise, several if-statements will be employed due to the exact purpose that several conditions
        # need to be checked.
        if self.isEmpty():
            # With this initial condition, it is checked if whether or not the list is empty, that is, if the size of
            # the list equals 0. In this case, two possibilites are presented. Either add the element the first or
            # the last one. It does not matter which one is applied, as the list is empty.
            self.addFirst(elem)
        else:
            # Finally, the crutial part of the exercise is developed. Here, several things are done. May we firstly pay
            # attention to the if-else statment presented from lines 82 to 85. This part decides where the element
            # should be introduced. If the size of the list is even, the new element should be inserted at position
            # len(self)//2. If the size is odd, then the element should be inserted at position (len(self)+1)/2.
            if (self._size % 2) == 0:
                index = self._size // 2
            else:
                index = (self._size + 1) // 2
            # Eventually, a while loop is used to get to the desired position.
            while i < index - 1:
                previous = previous.next
                i += 1
            # Once in the position, the element is created and introduced.
            newNode = SNode(elem)
            newNode.next = previous.next
            previous.next = newNode
            self._size += 1

    def insertList(self, inputList, start, end):
        """This is a function that takes as parameters an object of class SList2, inputList, and two integers, start
         and end. The function should remove all elements from the calling list between the start and end positions
         and insert the elements from the inputList instead."""

        # First and foremost, before performing any actions, it is vital to check that the conditions of the parameters
        # are satisfied so that no errors occur.
        # This is done using an if-statement that checks several points: firstly, that the "start" is not negative;
        # secondly, that the "start" is never greater than the "end", as it does not really make sense to begin in a
        # position that is after the "end"; and last but not least, that the "end" is not greater or equal than the
        # length of the list. This may be obvious but it is very important because if the "end" was to be greater
        # than the lenght of the list, it would not work, as the program would be trying to delete elements that do
        # not exist.
        if start < 0 or start > end or end >= len(self):
            return None

        # In case the pararmeters are correcly specified, several variables need to be specified.
        # Before explaining them, the main idea of the program will be described. First off, it is desired to arrive
        # to the positions that need to be deleted. However, these positions will not be deleted. The idea is that
        # the starting postition will be connected to the head of inputList. Once this is done, we will go
        # through the entire list connecting the elements and, once the last element is reached, it is connected to
        # the ending point.
        # Once the idea was exposed, it is time to describe the variables that will take part in the program. First off,
        # variables like "index_start" and "index_end" are defined to help us reach both starting and ending points;
        # then, "node" and "last_node" are specified so that we can connect them in the process of going through the list.
        index_start = 0
        index_end = 0
        node = self._head
        last_node = self._head
        while index_start < start - 1:
            # This initial while loop is used to arrive to the "start" position. It goes through the entire list and stops
            # once the element is reached.
            node = node.next
            index_start += 1
        while index_end < end + 1:
            # This while loop is used to arrive to the "end" position. It goes through the entire list and stops once the
            # element is reached.
            last_node = last_node.next
            index_end += 1

        # It is in this moment when we need to consider if whether or not we are in the beginning of the list or not.
        # In case we are (start==0), the head is directly switched to the one of inputList. If not, it is only needed
        # to indicate that the next element of the starting one is the head of this list.
        if start == 0:
            self._head = inputList._head
            node = self._head
        else:
            node.next = inputList._head

        # Once the conditions from above are checked, the most important thing to do is left, which is connecting
        # the list to the ending point. To do so, a simple while loop is used. It goes to the last element of the
        # list and states that the next one is last_node, which is the next element of the one that was deleted at
        # position end.
        while node.next != None:
            node = node.next
        node.next = last_node

    def reverseK(self, k):
        """This is a function that must invert the elements of the calling list in groups of k elements."""

        # As a must, before starting the exercise, several varibles need to be specified. The variables "prev" and
        # "current" are initialized as seen below to None and self._head because these will be used for important
        # processes like reversing the entire list or adding elements.
        prev = None
        current = self._head

        # The very first thing that needs to be checked is if whether or not the function is empty or if the specified
        # k is less or equal than 1. These cases are important because, as indicated in the exercise, in any of these
        # cases, no actions can be performed as it would not make sense to, for example, reverse an empty list.
        if self.isEmpty() or k <= 1:
            return None

        # However, another case is evaluated. In case the indicated k is greater than or equal to the size of the
        # calling list, then the entire list should be reversed. In order to do so, a while loop is used. Its
        # functionality is quite simple. The main goal is to go through the entire list, that is why it stops when
        # current is None, because this means that there are no more elements and, hence, there is nothing more to
        # reverse. While it goes through the list, the elements are reversed.
        elif k >= self._size:
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self._head = prev

        # Finally, here comes the most important part of the code, which is reversing our list in groups of k elements.
        # Several approaches can be considered. However, the approach exposed below will be based on the creation of
        # lists, making the task easier.
        else:
            final_list = SList2()
            # First off, the main idea of this part needs to be exposed. Because it is desired to reverse k groups,
            # we need to repeat the process of reversing as many times as groups there are in the list. That is,
            # if the size of the list is 8 and k=2, then the process needs to be repeated 4 times; if the size is 8
            # and k=3, the lowest case needs to be considered. Hence, there will be 2 groups of 3 nodes and another one
            # of 2.
            for i in range(self._size // k):
                # In this for loop, another list needs to be created ("aux"). This auxiliary list will help us when
                # reversing the elements in the subgroups. The first for loop is used to append the elements to the
                # auxiliary list. Once the first group is reversed, then it is time to introduce them in the final
                # list. Note that after the elements are reversed in the first loop, a varible is created to go
                # through the auxiliary list ("new_head").
                # Finally, a second range is used to introduce the elements to the final list. This for loop goes
                # through the entire aux list.
                aux = SList2()
                for i in range(k):
                    aux.addFirst(current.elem)
                    current = current.next
                new_head = aux._head
                for i in range(aux._size):
                    final_list.addLast(new_head.elem)
                    new_head = new_head.next
            # Finally, a last thing needs to be done. Being this probably one of the most important ones in the
            # exercise. In case that there is a pair not of the size of k (for example, if the size is 8 and k=3, there
            # will be 2 groups of 3 nodes and another one of 2), we need to reverse it. Hence, that is what is done in
            # the code from below.
            if current is not None:
                # If my current is not None, it means that there are still some more elements to reverse.
                aux = SList2()
                while current:
                    aux.addFirst(current.elem)
                    current = current.next
                new_head = aux._head
                for i in range(aux._size):
                    final_list.addLast(new_head.elem)
                    new_head = new_head.next
            # Finally, it is vital to indicate that my new head is the head of the final_list.
            self._head = final_list._head

    def maximumPair(self):
        """This is a function that returns the maximum value of the sum of equidistant elements in a list."""

        # As always, it is important to check if whether or not our list is empty or not, that is why it is the first
        # thing to check. If it is empty, it will return None and no actions will be perfomed.
        if self.isEmpty():
            return None

        # In case our list contains elements, several variables need to be declared so that the function can be
        # developed.
        # First off, the variable "current" is defined and is used in order to start at the head of the list.
        # Secondly, the varible "max" is declared to save the value of the maximum pair. A low value will be assigned,
        # such as -999, because it is very unlikely that the sum of equidistant elements will be lower than that
        # starting number.
        # Thirdly, a boolean operator ("cond") is also defined in order to finish the loop whenever we want.
        # Finally, the variables "cnt" and "size" are declared. The first one is used to know when is it needed to end
        # the iterations; and the other one is used to have a variable similiar to the size of the list but which can
        # vary to reach the nodes we are intered in.
        current = self._head
        max = -999
        cond = False
        cnt = 1
        size = self._size - 2
        while not cond:
            # Inside this while loop, the variable called "aux" is created. It will go through the whole list in order
            # to find the equidistant node of the current variable.
            aux = self._head
            for i in range(size + 1):
                # This very first loop allows to reach the equidistant element of the end part of the list.
                aux = aux.next
            # The size is reduced by 1 for the next iteration, which will be the next equidistant node because "current"
            # will be the next node from the beginning. Thus, aux will need to be the previous node from the end.
            # (Taking into consideration that aux always start at self._head).
            size -= 1
            # Now there are two possible cases. In the first one, the current node is not the same as the aux node,
            # so it is needed to sum one to the other.
            if aux != current:
                # The element of the current node plus the aux element is compared and it is analyzed if whether or not
                # it is bigger than the value of max.
                if (current.elem + aux.elem) > max:
                    max = current.elem + aux.elem
            # The other possible case is that aux == current. So this basically means that they are the same node,
            # so we just need to sum the value of one of them, not of both.
            else:
                if current.elem > max:
                    max = current.elem
            # Before finishing, two important cases are considered.
            # On the one hand,in the case the list size is odd, it will be needed to reach the middle of the list, so it
            # will be done when the "cnt" variable is equal to the floor division of the size of the list plus 1
            # (i.e. if the list size is 5, cnt needs to be equal to 5//2 + 1 = 3). In this way we will know that we are
            # in the middle of the list, so we can end the loop.
            # On the other hand, in the case the list size is even, when "cnt" is equal to the length of the list
            # divided by 2, we will know that we had summed all the equidistant nodes, so we can finish the loop.
            if (cnt == self._size // 2 + 1 and self._size % 2 != 0) or (cnt == self._size // 2 and self._size % 2 == 0):
                # To be able to finish the while loop, we change the status of our boolean variable.
                cond = True
            # In the case the previous condition is not fulfilled, we will go for the next node of current
            # and increase by one the value of cnt variable.
            else:
                current = current.next
                cnt += 1

        # Finally, the variable max is returned. This varible contains the biggest sum of the equidistant nodes.
        return max
