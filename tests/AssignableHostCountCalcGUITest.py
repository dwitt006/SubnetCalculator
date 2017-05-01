# Title:     Subnet Calculator: Assignable Host Count Calculator GUI Testing
# Date:      04-28-17


import unittest
from SubnetCalculator.AssignableHostCountCalcGUI import AssignHostCalcGUI
from SubnetCalculator.AssignableHostCountCalcGUI import exponent


class AssignHostCalcGUITest(unittest.TestCase):

    # Test exponent
    def test_exponent(self):
        self.assertEqual('2' + exponent('123'), '2¹²³')

    # Test clearing entries and learning steps
    def test_clear_and_reset(self):
        test_gui = AssignHostCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate2.invoke()
        test_gui.clear_and_reset()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test clearing entries and learning steps from separate button
    def test_clear_and_reset_calculate(self):
        test_gui = AssignHostCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate2.invoke()
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children(), [])
        self.assertEqual(test_gui.cidr_entry.get(), '')

    # Test assignable host count calculator using total host count: get_count_from_total(self)
    def test_count_total(self):
        test_gui = AssignHostCalcGUI()
        test_gui.total_entry.insert(0, '64')
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'Assignable Host Count: 64 - 2 = 62')

    # Test assignable host count calculator using cidr: get_count_from_cidr(self)
    def test_count_cidr(self):
        test_gui = AssignHostCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate2.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'CIDR Address: 152.2.136.0/26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'), 'CIDR: 26')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Host Bits: 32 - 26 = 6')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'),
                         'Assignable Host Count: ( 2⁶ ) - 2 = 62')

    # Test assignable host count calculator using netmask: get_count_from_netmask(self)
    def test_count_netmask(self):
        test_gui = AssignHostCalcGUI()
        test_gui.netmask_entry.insert(0, '255.255.255.192')
        test_gui.calculate3.invoke()
        self.assertEqual(test_gui.learning_steps.winfo_children()[0].cget('text'), 'Step 1:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[1].cget('text'), 'Netmask: 255.255.255.192')
        self.assertEqual(test_gui.learning_steps.winfo_children()[2].cget('text'), 'Step 2:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[3].cget('text'),
                         'Netmask Binary: 11111111.11111111.11111111.11000000')
        self.assertEqual(test_gui.learning_steps.winfo_children()[4].cget('text'), 'Step 3:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[5].cget('text'), 'Host Bits: 6')
        self.assertEqual(test_gui.learning_steps.winfo_children()[6].cget('text'), 'Step 4:')
        self.assertEqual(test_gui.learning_steps.winfo_children()[7].cget('text'),
                         'Assignable Host Count: ( 2⁶ ) - 2 = 62')

    # Test assignable host count calculator using IP range: get_count_from_ip_range(self)
    def test_count_ip_range(self):
        test_gui = AssignHostCalcGUI()
        test_gui.ip_range_entry.insert(0, '152.2.136.1-152.2.136.62')
        test_gui.calculate4.invoke()
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
        self.assertEqual(test_gui.learning_steps.winfo_children()[10].cget('text'),
                         'Assignable Host Count: ( 2⁶ ) - 2 = 62')


if __name__ == '__main__':
    unittest.main()
