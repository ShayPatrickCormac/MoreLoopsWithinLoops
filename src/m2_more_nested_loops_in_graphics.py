"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Zijian Huang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    original_ulc_x = rectangle.get_upper_left_corner().x
    original_ulc_y = rectangle.get_upper_left_corner().y
    original_lrc_x = rectangle.get_lower_right_corner().x
    original_lrc_y = rectangle.get_lower_right_corner().y
    original_width = rectangle.get_width()
    original_height = rectangle.get_height()

    ulc_x = original_ulc_x
    ulc_y = original_ulc_y
    lrc_x = original_lrc_x
    lrc_y = original_lrc_y
    for k in range(n):
        for i in range(k + 1):
            new_rect = rg.Rectangle(rg.Point(ulc_x,ulc_y), rg.Point(lrc_x,lrc_y))
            new_rect.attach_to(window)
            window.render()
            ulc_x = ulc_x + original_width
            lrc_x = lrc_x + original_width
        ulc_y = ulc_y - original_height
        lrc_y = lrc_y - original_height
        ulc_x = original_ulc_x - (original_width / 2 * (k + 1))
        lrc_x = original_lrc_x - (original_width / 2 * (k + 1))



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
