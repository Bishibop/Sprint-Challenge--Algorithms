"""
Thoughts:

    We're doing this sorting *in place*. No variables holding pointers
    or other arrays.

    We don't have arr[n] in O(1) time. Access is linear. The robot
    can only march up the list one element at a time. Reminicent of
    sorting a linked list (with no 'head' or 'tail' pointers).

    The light can be used to track the direction the robot should move...

    Question? When do I change direction? After a we hit the edge or
    swap values that might merit a change in direction?

    Also, you can't tell which item is None, only that one of the items is.

    Different options
        Change direction on edge
        Change direction on swap, depending on direction

    HOW DO WE KNOW WHEN THE LIST IS SORTED!!!!
    When you're at the top edge and and the None is there with you.

    Bubble sort, but on the way up you swap the None. This will force
    the robot to do n**2 passes, but you can tell when the algo is done.

    Can you move it up twice? Since technically, you're doing a pass on
    the way down...

    OFF means going UP

    What if we incremented it going down too? Get the real number of
    iterations? Since we're doing a sort of bouncing bubble sort.

        This would change the terminal condition. Would work if we just
        never put it in the last position. Just brought it right back and
        let the correct up terminal condition take it.

Logic: a sort of bi-directional bubble sort

    Use the light to indicate going UP or DOWN.
    If going UP, swap None and when value in list greater than in hand
    If going DOWN, only swap if value is less than in hand
        If you encounter a None while going DOWN, swap it one position
        UP, but only if it's not going to be in the last position. That
        would break the original terminating condition. In this case, just
        bring it back to it's original position. This means we're on the
        last iteration, and it will be picked up on the next pass UP.
    Toggle the light when you hit an edge
    Stop when you reach the last position and detect a None. Do not swap.

    This method uses the location of the None as an implicit iteration
    counter. We 'increment' it once every pass up the list.

"""


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    # WORKING STRETCH VERSION
    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        while True:

            # Going down
            if self.light_is_on():

                # Swaping logic
                if self.compare_item() is None:
                    self.swap_item()
                    self.move_right()
                    if self.can_move_right():
                        self.swap_item()
                    else:
                        pass
                    self.move_left()
                    self.swap_item()
                elif self.compare_item() == 1:
                    self.swap_item()
                elif self.compare_item() == 0:
                    # Don't swap
                    pass
                else:  # self.compare_item() == -1:
                    # Don't swap
                    pass

                # Moving DOWN logic
                if self.move_left():
                    # We can move left. We're done with this iteration.
                    pass
                else:
                    # We can't move left. Flip the light to start moving up.
                    self.set_light_off()

            # Going up
            else:

                # Swaping logic
                if self.compare_item() is None:
                    if self.can_move_right():
                        self.swap_item()
                    # Terminal cond: moving up, see a None, can't move right
                    # Don't swap. None can never be in the last position
                    else:
                        return
                elif self.compare_item() == 1:
                    # Don't swap
                    pass
                elif self.compare_item() == 0:
                    # Don't swap
                    pass
                else:  # self.compare_item() == -1:
                    self.swap_item()

                # Moving UP logic
                if self.move_right():
                    # We can move right. We're done with this iteration.
                    pass
                else:
                    # We can't move right. Flip the light to start moving down.
                    self.set_light_on()


    # WORKING NON-STRETCH VERSION
    #  def sort(self):
    #      """
    #      Sort the robot's list.
    #      """
    #      # Fill this out
    #      while True:
    #
    #          # Going down
    #          if self.light_is_on():
    #              # Swaping logic
    #              if self.compare_item() is None:
    #                  # Don't pick it up. None only goes UP.
    #                  pass
    #              elif self.compare_item() == 1:
    #                  self.swap_item()
    #              elif self.compare_item() == 0:
    #                  # Don't swap
    #                  pass
    #              else:  # self.compare_item() == -1:
    #                  # Don't swap
    #                  pass
    #
    #              # Moving DOWN logic
    #              if self.move_left():
    #                  # We can move left. We're done with this iteration.
    #                  pass
    #              else:
    #                  # We can't move left. Flip the light to start moving up.
    #                  self.set_light_off()
    #          # Going up
    #          else:
    #              # Swaping logic
    #              if self.compare_item() is None:
    #                  if self.can_move_right():
    #                      self.swap_item()
    #                  # Terminal cond: moving up, see a None, can't move right
    #                  # Don't swap. None can never be in the last position
    #                  else:
    #                      return
    #              elif self.compare_item() == 1:
    #                  # Don't swap
    #                  pass
    #              elif self.compare_item() == 0:
    #                  # Don't swap
    #                  pass
    #              else:  # self.compare_item() == -1:
    #                  self.swap_item()
    #
    #              # Moving UP logic
    #              if self.move_right():
    #                  # We can move right. We're done with this iteration.
    #                  pass
    #              else:
    #                  # We can't move right. Flip the light to start moving down.
    #                  self.set_light_on()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
