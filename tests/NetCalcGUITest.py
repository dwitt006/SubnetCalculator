# Title:     Subnet Calculator: Network Address Calculator GUI Testing
# Date:      04-28-17


import unittest
from SubnetCalculator.NetCalcGUI import NetCalcGUI


class NetCalcGUITest(unittest.TestCase):

    # Test clearing entries and learning steps
    def test_clear_and_reset(self):
        test_gui = NetCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        test_gui.clear_and_reset()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test clearing entries and learning steps from separate button
    def test_clear_and_reset_calculate(self):
        test_gui = NetCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test network address calculator using CIDR address: get_net_from_cidr(self)
    def test_net_cidr(self):
        test_gui = NetCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'CIDR Address: 152.2.136.0/26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), 'Network Address: 152.2.136.0')

    # Test network address calculator using IP range: get_net_from_ip_range(self)
    def test_net_ip_range(self):
        test_gui = NetCalcGUI()
        test_gui.ip_range_entry.insert(0, '152.2.136.1-152.2.136.62')
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'),
                         'Assignable IP Range: 152.2.136.1-152.2.136.62')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), '(Front - 1): 152.2.136.1 - 1')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Network Address: 152.2.136.0')


if __name__ == '__main__':
    unittest.main()
