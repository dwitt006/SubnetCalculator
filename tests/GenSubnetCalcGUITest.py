# Title:     Subnet Calculator: General Subnet Calculator GUI Testing
# Date:      04-28-17


import unittest
from SubnetCalculator.GenSubnetCalcGUI import GenSubnetCalcGUI


class GenSubnetCalculatorGUITest(unittest.TestCase):

    # Test clear entries
    def test_clear_entries(self):
        test_gui = GenSubnetCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.netmask_entry.insert(0, '255.255.255.192')
        test_gui.network_entry.insert(0, '152.2.136.0')
        test_gui.broadcast_entry.insert(0, '152.2.136.63')
        test_gui.ip_range_entry.insert(0, '152.2.136.1-152.2.136.62')
        test_gui.total_host_entry.insert(0, '64')
        test_gui.assignable_host_entry.insert(0, '62')
        test_gui.clear_entries()
        self.assertEqual(test_gui.cidr_entry.get(), '')
        self.assertEqual(test_gui.netmask_entry.get(), '')
        self.assertEqual(test_gui.network_entry.get(), '')
        self.assertEqual(test_gui.broadcast_entry.get(), '')
        self.assertEqual(test_gui.ip_range_entry.get(), '')
        self.assertEqual(test_gui.total_host_entry.get(), '')
        self.assertEqual(test_gui.assignable_host_entry.get(), '')

    # Test clear entries and results
    def test_clear_results(self):
        test_gui = GenSubnetCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.cidr_entry.get(), '')
        self.assertEqual(test_gui.netmask_entry.get(), '')
        self.assertEqual(test_gui.network_entry.get(), '')
        self.assertEqual(test_gui.broadcast_entry.get(), '')
        self.assertEqual(test_gui.ip_range_entry.get(), '')
        self.assertEqual(test_gui.total_host_entry.get(), '')
        self.assertEqual(test_gui.assignable_host_entry.get(), '')

    # Test general calculation using CIDR Address
    def test_gen_calc_cidr(self):
        test_gui = GenSubnetCalcGUI()
        test_gui.cidr_entry.insert(0, '152.2.136.0/26')
        test_gui.calculate.invoke()
        # self.assertEqual(test_gui.cidr_entry.get(), '152.2.136.0/26')
        self.assertEqual(test_gui.netmask_entry.get(), '255.255.255.192')
        self.assertEqual(test_gui.network_entry.get(), '152.2.136.0')
        self.assertEqual(test_gui.broadcast_entry.get(), '152.2.136.63')
        self.assertEqual(test_gui.ip_range_entry.get(), '152.2.136.1-152.2.136.62')
        self.assertEqual(test_gui.total_host_entry.get(), '64')
        self.assertEqual(test_gui.assignable_host_entry.get(), '62')

    # Test general calculation using Network Address
    def test_gen_calc_network(self):
        test_gui = GenSubnetCalcGUI()
        test_gui.network_entry.insert(0, '152.2.136.0')
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.cidr_entry.get(), '')
        self.assertEqual(test_gui.netmask_entry.get(), '')
        # self.assertEqual(test_gui.network_entry.get(), '')
        self.assertEqual(test_gui.broadcast_entry.get(), '')
        self.assertEqual(test_gui.ip_range_entry.get(), '')
        self.assertEqual(test_gui.total_host_entry.get(), '')
        self.assertEqual(test_gui.assignable_host_entry.get(), '')

    # Test general calculation using Network Address
    def test_gen_Calc_netmask(self):
        test_gui = GenSubnetCalcGUI()
        test_gui.netmask_entry.insert(0, '255.255.255.192')
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.cidr_entry.get(), '')
        # self.assertEqual(test_gui.netmask_entry.get(), '255.255.255.192')
        self.assertEqual(test_gui.network_entry.get(), '')
        self.assertEqual(test_gui.broadcast_entry.get(), '')
        self.assertEqual(test_gui.ip_range_entry.get(), '')
        self.assertEqual(test_gui.total_host_entry.get(), '64')
        self.assertEqual(test_gui.assignable_host_entry.get(), '62')

    def test_gen_calc_total_host_count(self):
        test_gui = GenSubnetCalcGUI()
        test_gui.total_host_entry.insert(0, '64')
        test_gui.calculate.invoke()
        self.assertEqual(test_gui.cidr_entry.get(), '')
        self.assertEqual(test_gui.netmask_entry.get(), '')
        self.assertEqual(test_gui.network_entry.get(), '')
        self.assertEqual(test_gui.broadcast_entry.get(), '')
        self.assertEqual(test_gui.ip_range_entry.get(), '')
        # self.assertEqual(test_gui.total_host_entry.get(), '64')
        self.assertEqual(test_gui.assignable_host_entry.get(), '62')

if __name__ == '__main__':
    unittest.main()
