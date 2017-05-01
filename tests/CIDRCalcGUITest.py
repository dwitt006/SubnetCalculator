# Title:     Subnet Calculator: Broadcast Calculator GUI Testing
# Date:      04-28-17


import unittest
from SubnetCalculator.CIDRCalcGUI import CIDRCalcGUI


class CIDRCalcGUITest(unittest.TestCase):

    # Test clearing entries and learning steps
    def test_clear_and_reset(self):
        test_gui = CIDRCalcGUI()
        test_gui.net_address_entry.insert(0, '152.2.136.0')
        test_gui.netmask_entry.insert(0, '255.255.255.192')
        test_gui.calculate.invoke()
        test_gui.clear_and_reset()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.net_address_entry.get(), '')

    # Test clearing entries and learning steps from separate button
    def test_clear_and_reset_calculate(self):
        test_gui = CIDRCalcGUI()
        test_gui.net_address_entry2.insert(0, '152.2.136.0')
        test_gui.ip_range_entry.insert(0, '152.2.136.1-152.2.136.62')
        test_gui.calculate2.invoke()
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.net_address_entry2.get(), '')
    pass

    # Test CIDR address calculator using network address and netmask: get_cidr_from_netmask(self)
    def test_cidr_netmask(self):
        test_gui = CIDRCalcGUI()
        test_gui.net_address_entry.insert(0, '152.2.136.0')
        test_gui.netmask_entry.insert(0, '255.255.255.192')
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'Network Address: 152.2.136.0')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'NetMask: 255.255.255.192')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'),
                         'Netmask Binary: 11111111.11111111.11111111.11000000')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'), "(Count 0's from Step 2)")
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'), 'CIDR: 32 - 6 = 26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[8].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[9].cget('text'), 'CIDR Address: 152.2.136.0/26')

    # Test CIDR address calculator using network address and IP range: get_cidr_from_ip_range(self)
    def test_cidr_ip_range(self):
        test_gui = CIDRCalcGUI()
        test_gui.net_address_entry2.insert(0, '152.2.136.0')
        test_gui.ip_range_entry.insert(0, '152.2.136.1-152.2.136.62')
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'Network Address: 152.2.136.0')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'),
                         'Assignable IP Range: 152.2.136.1-152.2.136.62')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'),
                         'Front: 10011000.00000010.10001000.00000001')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'),
                         ' Back: 10011000.00000010.10001000.00111110')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'),
                         'Comparison: 11111111.11111111.11111111.11000000')
        self.assertEqual(test_gui.learning_steps.winfo_children()[8].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[9].cget('text'), 'CIDR: 26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[10].cget('text'), 'Step 5:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[11].cget('text'), 'CIDR Address: 152.2.136.0/26')


if __name__ == '__main__':
    unittest.main()
