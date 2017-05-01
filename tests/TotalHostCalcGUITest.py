# Title:     Subnet Calculator: Total Host Count Calculator GUI Testing
# Date:      04-28-17


import unittest
from SubnetCalculator.TotalHostCalcGUI import TotalHostCalcGUI
from SubnetCalculator.TotalHostCalcGUI import exponent


class TotalHostCalcGUITest(unittest.TestCase):

    # Test exponent
    def test_exponent(self):
        self.assertEqual('2' + exponent('123'), '2¹²³')

    # Test clearing entries and learning steps
    def test_clear_and_reset(self):
        test_gui = TotalHostCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        test_gui.clear_and_reset()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test clearing entries and learning steps from separate button
    def test_clear_and_reset_calculate(self):
        test_gui = TotalHostCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test total host count calculator using cidr: get_count_from_cidr(self)
    def test_count_cidr(self):
        test_gui = TotalHostCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'CIDR Address: 152.2.136.0/26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), 'CIDR: 26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Host Bits: 32 - 26 = 6')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'),
                         'Total Host Count: 2⁶ = 64')

    # Test total host count calculator using netmask: get_count_from_netmask(self)
    def test_count_netmask(self):
        test_gui = TotalHostCalcGUI()
        test_gui.netmask_entry.insert(0, '255.255.255.192')
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'Netmask: 255.255.255.192')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'),
                         'Netmask Binary: 11111111.11111111.11111111.11000000')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Host Bits: 6')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'),
                         'Total Host Count: 2⁶ = 64')

    # Test total host count calculator using IP range: get_count_from_ip_range(self)
    def test_count_ip_range(self):
        test_gui = TotalHostCalcGUI()
        test_gui.ip_range_entry.insert(0, '152.2.136.1-152.2.136.62')
        test_gui.calculate3.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'),
                         'Assignable IP Range: 152.2.136.1-152.2.136.62')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'),
                         'Front: 10011000.00000010.10001000.00000001')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'),
                         ' Back: 10011000.00000010.10001000.00111110')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'),
                         'Comparison: 11111111.11111111.11111111.11000000')
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[8].cget('text'), 'Host Bits: 6')
        self.assertEqual(test_gui.learning_steps.winfo_children()[9].cget('text'), 'Step 5:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[10].cget('text'), 'Total Host Count: 2⁶ = 64')


if __name__ == '__main__':
    unittest.main()
