# Title:     Subnet Calculator: Broadcast Calculator GUI Testing
# Date:      04-28-17


import unittest
from SubnetCalculator.BroadcastCalcGUI import BroadcastCalcGUI


class BroadcastCalcGUITest(unittest.TestCase):

    # Test clearing entries and learning steps
    def test_clear_and_reset(self):
        test_gui = BroadcastCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        test_gui.clear_and_reset()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test clearing entries and learning steps from separate button
    def test_clear_and_reset_calculate(self):
        test_gui = BroadcastCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test broadcast calculator using CIDR address: get_broadcast_from_cidr(self)
    def test_broadcast_cidr(self):
        test_gui = BroadcastCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'CIDR Address: 152.2.136.0/26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), 'CIDR: 26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'), 'Host Bits: 32 - 26 = 6')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'),
                         'Network Binary: 10011000.00000010.10001000.00000000')
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[8].cget('text'),
                         'Broadcast Binary: 10011000.00000010.10001000.00111111')
        self.assertEqual(test_gui.learning_steps.winfo_children()[9].cget('text'), 'Step 5:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[10].cget('text'), 'Broadcast Address: 152.2.136.63')

    # Test broadcast calculator using IP range: get_broadcast_from_ip_range(self)
    def test_broadcast_ip_range(self):
        test_gui = BroadcastCalcGUI()
        test_gui.ip_range_entry.insert(0, '152.2.136.1-152.2.136.62')
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'),
                         'Assignable IP Range: 152.2.136.1-152.2.136.62')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), '(Back + 1): 152.2.136.62 + 1')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Broadcast Address: 152.2.136.63')


if __name__ == '__main__':
    unittest.main()
