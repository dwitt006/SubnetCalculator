# Title:     Subnet Calculator: IP Range Calculator GUI Testing
# Date:      04-28-17


import unittest
from SubnetCalculator.IPRangeCalcGUI import IPRangeCalcGUI


class IPRangeCalcGUITest(unittest.TestCase):

    # Test clearing entries and learning steps
    def test_clear_and_reset(self):
        test_gui = IPRangeCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        test_gui.clear_and_reset()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test clearing entries and learning steps from separate button
    def test_clear_and_reset_calculate(self):
        test_gui = IPRangeCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test IP range calculator using CIDR address: get_ip_range_from_cidr(self)
    def test_ip_range_cidr(self):
        test_gui = IPRangeCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'CIDR Address: 152.2.136.0/26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), 'Front: 152.2.136.0 + 1')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'CIDR: 26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'), 'Host Bits: 32 - 26 = 6')
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[8].cget('text'),
                         'Network Binary: 10011000000000101000100000000000')
        self.assertEqual(test_gui.learning_steps.winfo_children()[9].cget('text'), 'Step 5:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[10].cget('text'),
                         'Back Binary (Broadcast - 1): 10011000.00000010.10001000.00111110')
        self.assertEqual(test_gui.learning_steps.winfo_children()[11].cget('text'), 'Step 6:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[12].cget('text'),
                         'Assignable IP Range: 152.2.136.1-152.2.136.62')

    # Test IP range calculator using network address and broadcast address: get_ip_range_from_network_broadcast(self)
    def test_ip_range_network_broadcast(self):
        test_gui = IPRangeCalcGUI()
        test_gui.network_entry.insert(0, '152.2.136.0')
        test_gui.broadcast_entry.insert(0, '152.2.136.63')
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'Network Address: 152.2.136.0')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Broadcast Address: 152.2.136.63')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'), 'Front: 152.2.136.0 + 1')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'), 'Back: 152.2.136.63 - 1')
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[8].cget('text'),
                         'Assignable IP Range: 152.2.136.1-152.2.136.62')


if __name__ == '__main__':
    unittest.main()
