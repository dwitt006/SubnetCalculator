# Title:     Subnet Calculator: Subnet Calculator Testing
# Date:      04-24-17


import unittest
from SubnetCalculator.SubnetCalculator import Subnet


class SubnetCalculatorTest(unittest.TestCase):

    """Test calculation of individual variables"""
    # Test Calculate CIDR
    def test_calculate_cidr_from_netmask(self):
        test_subnet = Subnet()
        test_subnet.network_address = '152.2.136.0'
        test_subnet.netmask = '255.255.255.192'
        test_subnet.calculate_cidr_from_netmask()
        self.assertEqual(test_subnet.cidr_address, '152.2.136.0/26')

    def test_calculate_cidr_from_ip_range(self):
        test_subnet = Subnet()
        test_subnet.network_address = '152.2.136.0'
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        test_subnet.calculate_cidr_from_ip_range()
        self.assertEqual(test_subnet.cidr_address, '152.2.136.0/26')

    # Test Calculate Netmask
    def test_calculate_netmask_from_cidr(self):
        test_subnet = Subnet()
        test_subnet.cidr_address = '152.2.136.0/26'
        test_subnet.calculate_netmask_from_cidr()
        self.assertEqual(test_subnet.netmask, '255.255.255.192')

    def test_calculate_netmask_from_ip_range(self):
        test_subnet = Subnet()
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        test_subnet.calculate_netmask_from_ip_range()
        self.assertEqual(test_subnet.netmask, '255.255.255.192')

    # Test Calculate Network Address
    def test_calculate_network_address_from_cidr(self):
        test_subnet = Subnet()
        test_subnet.cidr_address = '152.2.136.0/26'
        test_subnet.calculate_network_address_from_cidr()
        self.assertEqual(test_subnet.network_address, '152.2.136.0')

    def test_calculate_network_address_from_ip_range(self):
        test_subnet = Subnet()
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        test_subnet.calculate_network_address_from_ip_range()
        self.assertEqual(test_subnet.network_address, '152.2.136.0')

    # Test Calculate Broadcast Address
    def test_calculate_broadcast_address_from_cidr(self):
        test_subnet = Subnet()
        test_subnet.cidr_address = '152.2.136.0/26'
        test_subnet.calculate_broadcast_address_from_cidr()
        self.assertEqual(test_subnet.broadcast_address, '152.2.136.63')

    def test_calculate_broadcast_address_from_ip_range(self):
        test_subnet = Subnet()
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        test_subnet.calculate_broadcast_address_from_ip_range()
        self.assertEqual(test_subnet.broadcast_address, '152.2.136.63')

    # Test Calculate Assignable IP Range
    def test_calculate_ip_range_from_cidr(self):
        test_subnet = Subnet()
        test_subnet.cidr_address = '152.2.136.0/26'
        test_subnet.calculate_ip_range_from_cidr()
        self.assertEqual(test_subnet.ip_range, '152.2.136.1-152.2.136.62')

    def test_calculate_ip_range_from_network_broadcast(self):
        test_subnet = Subnet()
        test_subnet.network_address = '152.2.136.0'
        test_subnet.broadcast_address = '152.2.136.63'
        test_subnet.calculate_ip_range_from_network_broadcast()
        self.assertEqual(test_subnet.ip_range, '152.2.136.1-152.2.136.62')

    # Test Calculate ToTal Host Count
    def test_calculate_total_host_count_from_cidr(self):
        test_subnet = Subnet()
        test_subnet.cidr_address = '152.2.136.0/26'
        test_subnet.calculate_total_host_count_from_cidr()
        self.assertEqual(test_subnet.total_host_count, 64)

    def test_calculate_total_host_count_from_netmask(self):
        test_subnet = Subnet()
        test_subnet.netmask = '255.255.255.192'
        test_subnet.calculate_total_host_count_from_netmask()
        self.assertEqual(test_subnet.total_host_count, 64)

    def test_calculate_total_host_count_from_ip_range(self):
        test_subnet = Subnet()
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        test_subnet.calculate_total_host_count_from_ip_range()
        self.assertEqual(test_subnet.total_host_count, 64)

    # Test Calculate Assignable Host Count
    def test_calculate_assignable_host_count(self):
        test_subnet = Subnet()
        test_subnet.total_host_count = 64
        test_subnet.calculate_assignable_host_count()
        self.assertEqual(test_subnet.assignable_host_count, 62)

    def test_calculate_assignable_host_count_from_cidr(self):
        test_subnet = Subnet()
        test_subnet.cidr_address = '152.2.136.0/26'
        test_subnet.calculate_assignable_host_count_from_cidr()
        self.assertEqual(test_subnet.assignable_host_count, 62)

    def test_calculate_assignable_host_count_from_netmask(self):
        test_subnet = Subnet()
        test_subnet.netmask = '255.255.255.192'
        test_subnet.calculate_assignable_host_count_from_netmask()
        self.assertEqual(test_subnet.assignable_host_count, 62)

    def test_calculate_assignable_host_count_from_ip_range(self):
        test_subnet = Subnet()
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        test_subnet.calculate_assignable_host_count_from_ip_range()
        self.assertEqual(test_subnet.assignable_host_count, 62)

    '''Test variable verifications'''
    # Test Verify Variables: None
    def test_verify_variables_none(self):
        test_subnet = Subnet()
        self.assertFalse(test_subnet.verify_variable_use())
        self.assertFalse(test_subnet.verify_variables())

    # Test Verify Variables: CIDR
    def test_verify_variables_cidr(self):
        test_subnet = Subnet()
        test_subnet.cidr_address = 0
        self.assertFalse(test_subnet.verify_cidr_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.cidr_address = 'THIS IS A TEST'
        self.assertFalse(test_subnet.verify_cidr_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.cidr_address = '152.2.136.0'
        self.assertFalse(test_subnet.verify_cidr_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.cidr_address = '152.2.136.0/'
        self.assertFalse(test_subnet.verify_cidr_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.cidr_address = '152.2.136.0//'
        self.assertFalse(test_subnet.verify_cidr_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.cidr_address = '152.2.136.0/Test'
        self.assertFalse(test_subnet.verify_cidr_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.cidr_address = '152.2.136.0/26/'
        self.assertFalse(test_subnet.verify_cidr_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.cidr_address = '152.2.136.0/26'
        self.assertTrue(test_subnet.verify_cidr_address())
        self.assertTrue(test_subnet.verify_variables())

    # Test Verify Variables: Netmask
    def test_verify_variables_netmask(self):
        test_subnet = Subnet()
        test_subnet.netmask = 0
        self.assertFalse(test_subnet.verify_netmask())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.netmask = 'THIS IS A TEST'
        self.assertFalse(test_subnet.verify_netmask())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.netmask = '152.2.136.0'
        self.assertFalse(test_subnet.verify_netmask())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.netmask = '255.255.255.192'
        self.assertTrue(test_subnet.verify_netmask())
        self.assertTrue(test_subnet.verify_variables())

    # Test Verify Variables: Network Address
    def test_verify_variables_network_address(self):
        test_subnet = Subnet()
        test_subnet.network_address = 0
        self.assertFalse(test_subnet.verify_network_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.network_address = 'THIS IS A TEST'
        self.assertFalse(test_subnet.verify_network_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.network_address = '152.2.136.0/26'
        self.assertFalse(test_subnet.verify_network_address())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.network_address = '152.2.136.0'
        self.assertTrue(test_subnet.verify_network_address())
        self.assertTrue(test_subnet.verify_variables())

    # Test Verify Variables: Broadcast Address
    def test_verify_variables_broadcast(self):
        test_subnet = Subnet()
        test_subnet.broadcast_address = 0
        self.assertFalse(test_subnet.verify_broadcast())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.broadcast_address = 'THIS IS A TEST'
        self.assertFalse(test_subnet.verify_broadcast())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.broadcast_address = '152.2.136.0/26'
        self.assertFalse(test_subnet.verify_broadcast())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.broadcast_address = '152.2.136.63'
        self.assertTrue(test_subnet.verify_broadcast())
        self.assertTrue(test_subnet.verify_variables())

    # Test Verify Variables: IP Range
    def test_verify_variables_ip_range(self):
        test_subnet = Subnet()
        test_subnet.ip_range = 0
        self.assertFalse(test_subnet.verify_ip_range())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.ip_range = 'THIS IS A TEST'
        self.assertFalse(test_subnet.verify_ip_range())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.ip_range = '152.2.136.0/26'
        self.assertFalse(test_subnet.verify_ip_range())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.ip_range = '152.2.136.63'
        self.assertFalse(test_subnet.verify_ip_range())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.ip_range = '152.2.136.0-'
        self.assertFalse(test_subnet.verify_ip_range())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.ip_range = '152.2.136.0-152.2.136.0'
        self.assertFalse(test_subnet.verify_ip_range())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.ip_range = '152.2.136.62-152.2.136.1'
        self.assertFalse(test_subnet.verify_ip_range())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        self.assertTrue(test_subnet.verify_ip_range())
        self.assertTrue(test_subnet.verify_variables())

    # Test Verify Variables: Total Host Count
    def test_verify_variables_total_host_count(self):
        test_subnet = Subnet()
        test_subnet.total_host_count = 'THIS IS A TEST'
        self.assertFalse(test_subnet.verify_total_host_count())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.total_host_count = '123'
        self.assertFalse(test_subnet.verify_total_host_count())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.total_host_count = '64'
        self.assertTrue(test_subnet.verify_total_host_count())
        self.assertTrue(test_subnet.verify_variables())

    # Test Verify Variables: Assignable Host Count
    def test_verify_variables_assignable_host_count(self):
        test_subnet = Subnet()
        test_subnet.assignable_host_count = 'THIS IS A TEST'
        self.assertFalse(test_subnet.verify_assignable_host_count())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.assignable_host_count = '123'
        self.assertFalse(test_subnet.verify_assignable_host_count())
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.assignable_host_count = '62'
        self.assertTrue(test_subnet.verify_assignable_host_count())
        self.assertTrue(test_subnet.verify_variables())

    # Test Verify Variables: Multiple Variables
    def test_verify_variables_multiple(self):
        test_subnet = Subnet()
        test_subnet.network_address = 'THIS IS A TEST'
        test_subnet.ip_range = 'THIS IS A TEST'
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.network_address = '152.2.136.0'
        test_subnet.ip_range = 'THIS IS A TEST'
        self.assertFalse(test_subnet.verify_variables())
        test_subnet.network_address = '152.2.136.0'
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        self.assertTrue(test_subnet.verify_variables())

    '''Test calculate every variable from select individual variables'''
    # Test General Calculation: CIDR
    def test_general_calculation_cidr(self):
        test_subnet = Subnet()
        test_subnet.cidr_address = '152.2.136.0/26'
        test_subnet.general_calculation()
        # self.assertEqual(test_subnet.cidr_address, '152.2.136.0/26')
        self.assertEqual(test_subnet.netmask, '255.255.255.192')
        self.assertEqual(test_subnet.network_address, '152.2.136.0')
        self.assertEqual(test_subnet.broadcast_address, '152.2.136.63')
        self.assertEqual(test_subnet.ip_range, '152.2.136.1-152.2.136.62')
        self.assertEqual(test_subnet.total_host_count, 64)
        self.assertEqual(test_subnet.assignable_host_count, 62)

    # Test General Calculation: Network Address & Netmask
    def test_general_calculation_network_netmask(self):
        test_subnet = Subnet()
        test_subnet.network_address = '152.2.136.0'
        test_subnet.netmask = '255.255.255.192'
        test_subnet.general_calculation()
        self.assertEqual(test_subnet.cidr_address, '152.2.136.0/26')
        # self.assertEqual(test_subnet.netmask, '255.255.255.192')
        # self.assertEqual(test_subnet.network_address, '152.2.136.0')
        self.assertEqual(test_subnet.broadcast_address, '152.2.136.63')
        self.assertEqual(test_subnet.ip_range, '152.2.136.1-152.2.136.62')
        self.assertEqual(test_subnet.total_host_count, 64)
        self.assertEqual(test_subnet.assignable_host_count, 62)

    # Test General Calculation: Network Address & Assignable IP Range
    def test_general_calculation_network_ip_range(self):
        test_subnet = Subnet()
        test_subnet.network_address = '152.2.136.0'
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        test_subnet.general_calculation()
        self.assertEqual(test_subnet.cidr_address, '152.2.136.0/26')
        self.assertEqual(test_subnet.netmask, '255.255.255.192')
        # self.assertEqual(test_subnet.network_address, '152.2.136.0')
        self.assertEqual(test_subnet.broadcast_address, '152.2.136.63')
        # self.assertEqual(test_subnet.ip_range, '152.2.136.1-152.2.136.62')
        self.assertEqual(test_subnet.total_host_count, 64)
        self.assertEqual(test_subnet.assignable_host_count, 62)

    # Test General Calculation: Assignable IP Range
    def test_general_calculation_ip_range(self):
        test_subnet = Subnet()
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        test_subnet.general_calculation()
        self.assertEqual(test_subnet.cidr_address, '152.2.136.0/26')
        self.assertEqual(test_subnet.netmask, '255.255.255.192')
        self.assertEqual(test_subnet.network_address, '152.2.136.0')
        self.assertEqual(test_subnet.broadcast_address, '152.2.136.63')
        # self.assertEqual(test_subnet.ip_range, '152.2.136.1-152.2.136.62')
        self.assertEqual(test_subnet.total_host_count, 64)
        self.assertEqual(test_subnet.assignable_host_count, 62)

    # Test General Calculation: Network Address & Broadcast Address
    def test_general_calculation_network_broadcast(self):
        test_subnet = Subnet()
        test_subnet.network_address = '152.2.136.0'
        test_subnet.broadcast_address = '152.2.136.63'
        test_subnet.general_calculation()
        self.assertEqual(test_subnet.cidr_address, '152.2.136.0/26')
        self.assertEqual(test_subnet.netmask, '255.255.255.192')
        # self.assertEqual(test_subnet.network_address, '152.2.136.0')
        # self.assertEqual(test_subnet.broadcast_address, '152.2.136.63')
        self.assertEqual(test_subnet.ip_range, '152.2.136.1-152.2.136.62')
        self.assertEqual(test_subnet.total_host_count, 64)
        self.assertEqual(test_subnet.assignable_host_count, 62)

    # Test Reset Variables
    def test_reset_variables(self):
        test_subnet = Subnet()
        test_subnet.cidr_address = '152.2.136.0/26'
        test_subnet.network_address = '152.2.136.0'
        test_subnet.netmask = '255.255.255.192'
        test_subnet.broadcast_address = '152.2.136.63'
        test_subnet.ip_range = '152.2.136.1-152.2.136.62'
        test_subnet.reset_variables()
        self.assertEqual(test_subnet.cidr_address, '')
        self.assertEqual(test_subnet.netmask, '')
        self.assertEqual(test_subnet.network_address, '')
        self.assertEqual(test_subnet.broadcast_address, '')
        self.assertEqual(test_subnet.ip_range, '')
        pass

if __name__ == '__main__':
    unittest.main()
