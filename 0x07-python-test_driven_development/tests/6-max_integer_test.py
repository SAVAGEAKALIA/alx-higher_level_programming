#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for max_integer([..])
    """

    def test_no_arg(self):
        """
        Test max_integer() with no arguments
        """
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """
        Test max_integer() with an empty list
        """
        self.assertEqual(max_integer([]), None)

    # Add other tests cases following a similar pattern

    def test_floats_large(self):
        """
        Test max_integer() with a list of large floats
        """
        self.assertEqual(
            max_integer(
                [0.36701449486981136, 0.22932193120425423, 17.269673745943177,
                 0.6021998063297004, 7.040663644666581, 0.318418153098476,
                 0.14782568486828354, 1.694150096609713, 0.523292479047324,
                 6.577278388003499, 0.03165696316739835,
                 0.9723205356754642, 1.0167973840532782,
                 0.17994528432150622, 0.34268959203149724,
                 0.8237893847200373, 6.564703466354198, 0.650943204479027,
                 1.8902940005294793, 7.691604865311827, 8.897302744173896,
                 1.0780411284398352, 1.6564018996809176,
                 0.7495378363397325, 0.6460418901123863,
                 0.29656944388569284, 1.2020859950744733,
                 2.695758513783994, 0.37293339285604976,
                 0.8540047898304736, 0.16021193325291794,
                 0.027891891117170508, 0.8464685760135892,
                 4.506719557284897, 2.0258041087808, 4.525163681550944,
                 1.3277284362225874, 3.042753010712081, 2.4201460936424986,
                 0.6254206993310946, 3.6037820704785766,
                 0.5843942753272469, 2.994055932449279, 0.5168645505697169,
                 0.014982685631661026, 0.02477737364433171,
                 0.47120480947220955, 2.5056796257122915,
                 1.3349487122618868, 0.08451917751917885,
                 1.0157082402123356, 29.496355326217376,
                 10.171800729369348, 1.1263544935158727,
                 0.47572929035550277, 3.712323073375754,
                 0.5742929278531704, 0.43940976988732966,
                 0.09537099783126887, 1.4936141049902174,
                 5.764320019082692, 4.322880498170903, 2.004237813008687,
                 0.5565243581024599, 4.302022962278392, 5.680293004785562,
                 2.178866303290743, 1.0390412554953965,
                 0.45132551361896317, 1.4643609109467473,
                 0.6904822043628014, 7.42850599670902, 0.8174242076055683,
                 0.6560986886071569, 0.6513016647379839, 0.7402037152516,
                 1.3480227709351067, 10.667222236398727,
                 1.1255361340134915, 0.3631658619504303,
                 0.8812949657884553, 1.1100323642668828,
                 5.0119643460188845, 2.8953551308720056,
                 2.5574324632368866, 9.169493642307119, 0.4175692708444569,
                 2.344748944605401, 1.1674261590629318, 0.6998588019912835,
                 0.42770576125452897, 1.7136005979522013,
                 8.877571036363525, 0.6825287480571863, 2.6834294650218338,
                 0.7504024417975861, 0.2762206358275793,
                 0.20607476376994402, 0.9497689034126077,
                 2.1498649449691807]), 29.496355326217376)

    def test_numeric_string(self):
        """
        Test max_integer() with a numeric string
        """
        self.assertEqual(max_integer("192834754"), "9")

    # Add more tests cases following a similar pattern
    def test_negatives(self):
        """A Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6105619, -854849, -562553, -3088955, -6711290, -4817844,
                 -1907189, -8110534, -6601769, -5837524, -4726702,
                 -8433749, -7251403, -5117635, -2979207, -1335257,
                 -6867266, -9073637, -6224732, -1080801, -1080228,
                 -6801278, -8351954, -1736432, -746131, -4376995,
                 -967891, -4663691, -71562, -7153670, -8038202,
                 -7893047, -9350883, -1132134, -3675971, -8495354,
                 -9158229, -9310087, -6319598, -8961209, -4906000,
                 -386471, -639929, -2676965, -6881679, -6258057,
                 -5490677, -1107298, -4199148, -5933601, -9917695,
                 -7759849, -7045734, -4885806, -9485075, -5119579,
                 -4147063, -7622811, -4671971, -5439539, -840414,
                 -3671742, -4400074, -3549343, -9146070, -6071672,
                 -7213213, -1307446, -3936098, -2415520, -9162654,
                 -6129976, -5791439, -3481890, -7828832, -6954726,
                 -5272933, -4952516, -6115545, -8333464, -7271456,
                 -4097027, -4342575, -8400559, -8235052, -4373818,
                 -8054214, -8565596, -639225, -2292452, -4269529,
                 -7202853, -6891036, -4379807, -7955196, -1536591,
                 -2839083, -2586661, -9941097, -3136620]), -71562)

        def test_numeric_string(self):
            """A Unittest for max_integer([..])"""
            self.assertEqual(max_integer("192834754"), "9")

        def test_string(self):
            """A Unittest for max_integer([..])"""
            self.assertEqual(max_integer("Holberton"), "t")

        def test_lists(self):
            """ A Unittest for max_integer([..])"""
            self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

        def test_str_list(self):
            """ A Unittest for max_integer([..])"""
            self.assertEqual(
                max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
                ["sic"])

        def test_dict(self):
            """THE Unittest for max_integer([..])"""
            with self.assertRaises(TypeError):
                max_integer([{20: 23, 14: 45}, {"a": "b"}])


if __name__ == '__main__':
    unittest.main()
