# Title:     Subnet Calculator
# Date:      03-25-17
""" Creates subnet variables to visually represent the steps used in the process. For actual implementation of 
networking within Python coding, it is recommended to use module ipaddress"""

import re
import ipaddress


class Subnet:
    def __init__(self):
        self.cidr_address = ''
        self.netmask = ''
        self.network_address = ''
        self.broadcast_address = ''
        self.ip_range = ''
        self.total_host_count = ''
        self.assignable_host_count = ''

        self.cidr_address_steps = ()
        self.netmask_steps = ()
        self.network_address_steps = ()
        self.broadcast_address_steps = ()
        self.ip_range_steps = ()
        self.total_host_count_steps = ()
        self.assignable_host_count_steps = ()

    """ CIDR ADDRESS """
    # Calculates CIDR from the Netmask and network address
    def calculate_cidr_from_netmask(self):
        netmask_binary = ''.join(['{0:08b}'.format(int(bits)) for bits in self.netmask.split('.')])
        host_bits = netmask_binary.count('0')
        self.cidr_address = '{}/{}'.format(self.network_address, (32-host_bits))

        step1 = {'Netmask Binary': '.'.join(['{0:08b}'.format(int(bits)) for bits in self.netmask.split('.')])}
        step2 = {'CIDR': '32 - {} = {}'.format(host_bits, 32-host_bits)}
        self.cidr_address_steps = (step1, step2)

    # Calculates CIDR from network address and assignable IP range
    def calculate_cidr_from_ip_range(self):
        ip_range = self.ip_range.split('-')
        front = int(''.join(['{0:08b}'.format(int(bits)) for bits in ip_range[0].split('.')]), 2)
        back = int(''.join(['{0:08b}'.format(int(bits)) for bits in ip_range[1].split('.')]), 2)
        host_bits = len(bin(front ^ back)[2:])
        cidr = (32-host_bits)
        self.cidr_address = '{}/{}'.format(self.network_address, cidr)

        step1 = {'Front': '.'.join(['{0:08b}'.format(int(bits)) for bits in ip_range[0].split('.')]),
                 'Back': '.'.join(['{0:08b}'.format(int(bits)) for bits in ip_range[1].split('.')])}
        step2 = {'Comparison': '.'.join([byte for byte in re.findall('........', ('1'*cidr+'0'*host_bits))])}
        step3 = {'CIDR': cidr}
        self.cidr_address_steps = (step1, step2, step3)

    """ NETMASK """
    # Calculates Netmask from CIDR address
    def calculate_netmask_from_cidr(self):
        network = int(self.cidr_address.split('/')[1])
        host = 32 - network
        netmask = ('1' * network) + ('0' * host)
        self.netmask = '.'.join([str(int(bits, 2)) for bits in re.findall('........', netmask)])

        step1 = {'Network Bits': network, 'Host Bits': '32 - {} = {}'.format(network, host)}
        step2 = {'Netmask Binary': '.'.join([byte for byte in re.findall('........', netmask)])}
        self.netmask_steps = (step1, step2)

    # Calculate Netmask from assignable IP range
    def calculate_netmask_from_ip_range(self):
        ip_range = self.ip_range.split('-')
        front = int(''.join(['{0:08b}'.format(int(bits)) for bits in ip_range[0].split('.')]), 2)
        back = int(''.join(['{0:08b}'.format(int(bits)) for bits in ip_range[1].split('.')]), 2)
        host = len(bin(front ^ back)[2:])
        network = 32 - host
        netmask = ('1' * network) + ('0' * host)
        self.netmask = '.'.join([str(int(bits, 2)) for bits in re.findall('........', netmask)])

        step1 = {'Front': '.'.join(['{0:08b}'.format(int(bits)) for bits in ip_range[0].split('.')]),
                 'Back': '.'.join(['{0:08b}'.format(int(bits)) for bits in ip_range[1].split('.')])}
        step2 = {'Comparison': '.'.join([byte for byte in re.findall('........', netmask)])}
        self.netmask_steps = (step1, step2)

    """ NETWORK ADDRESS"""
    # Calculate network address from CIDR
    def calculate_network_address_from_cidr(self):
        self.network_address = self.cidr_address.split('/')[0]

    # Calculate network address from assignable IP range
    def calculate_network_address_from_ip_range(self):
        ip_range = self.ip_range.split('-')
        network = ip_range[0].split('.')
        network[-1] = str(int(network[-1])-1)
        self.network_address = '.'.join(network)

        step1 = {'Front - 1': '{} - 1'.format(ip_range[0])}
        self.network_address_steps = (step1, )

    """ BROADCAST ADDRESS """
    # Calculate broadcast address from CIDR
    def calculate_broadcast_address_from_cidr(self):
        network_address, network_bits = self.cidr_address.split('/')
        address_bits = ''.join(['{0:08b}'.format(int(bits)) for bits in network_address.split('.')])
        binary = [bit for bit in address_bits]
        binary[int(network_bits):] = ['1']*(32-int(network_bits))
        self.broadcast_address = '.'.join([str(int(bits, 2)) for bits in re.findall('........', ''.join(binary))])

        step1 = {'Network Binary': '.'.join(['{0:08b}'.format(int(bits)) for bits in network_address.split('.')]),
                 'CIDR': network_bits}
        step2 = {'Broadcast Binary': '.'.join(byte for byte in re.findall('........', ''.join(binary)))}
        self.broadcast_address_steps = (step1, step2)

    # Calculate broadcast address from assignable IP range
    def calculate_broadcast_address_from_ip_range(self):
        ip_range = self.ip_range.split('-')
        broadcast = ip_range[1].split('.')
        broadcast[-1] = str(int(broadcast[-1]) + 1)
        self.broadcast_address = '.'.join(broadcast)

        step1 = {'Back + 1': '{} + 1'.format(ip_range[1])}
        self.broadcast_address_steps = (step1, )

    """ ASSIGNABLE IP RANGE """
    # Calculate assignable IP range from CIDR
    def calculate_ip_range_from_cidr(self):
        network_address, network_bits = self.cidr_address.split('/')
        front = network_address.split('.')
        back = ''.join(['{0:08b}'.format(int(bits)) for bits in front])
        front[-1] = str(int(front[-1]) + 1)
        front = '.'.join(front)
        binary = [bit for bit in back]
        binary[int(network_bits):-1] = ['1'] * (32 - int(network_bits) - 1)
        back2 = '.'.join([str(int(bits, 2)) for bits in re.findall('........', ''.join(binary))])
        self.ip_range = front + '-' + back2

        step1 = {'Front': '{} + 1'.format(network_address)}
        step2 = {'Network Binary': back, 'CIDR': network_bits}
        step3 = {'Back Binary': ('.'.join([byte for byte in re.findall('........', ''.join(binary))]))}
        self.ip_range_steps = (step1, step2, step3)

    # Calculate assignable IP range from network address and broadcast address
    def calculate_ip_range_from_network_broadcast(self):
        front = self.network_address.split('.')
        front[-1] = str(int(front[-1]) + 1)
        back = self.broadcast_address.split('.')
        back[-1] = str(int(back[-1]) - 1)
        self.ip_range = '.'.join(front) + '-' + '.'.join(back)

        step1 = {'Front': '{} + 1'.format(self.network_address)}
        step2 = {'Back': '{} - 1'.format(self.broadcast_address)}
        self.ip_range_steps = (step1, step2)

    """ TOTAL HOST COUNT """
    # Calculate total host count from CIDR
    def calculate_total_host_count_from_cidr(self):
        cidr = self.cidr_address.split('/')[1]
        host_bits = (32 - int(cidr))
        self.total_host_count = 2 ** host_bits

        step1 = {'CIDR': cidr}
        step2 = {'Host Bits': '32 - {} = {}'.format(cidr, host_bits)}
        self.total_host_count_steps = (step1, step2)

    # Calculate total host count from Netamsk
    def calculate_total_host_count_from_netmask(self):
        host_bits = (''.join(['{0:08b}'.format(int(bits)) for bits in self.netmask.split('.')])).count('0')
        self.total_host_count = 2 ** host_bits

        step1 = {'Netmask Binary': '.'.join(['{0:08b}'.format(int(bits)) for bits in self.netmask.split('.')])}
        step2 = {'Host Bits': host_bits}
        self.total_host_count_steps = (step1, step2)

    # Calculate total host count from assignable IP range
    def calculate_total_host_count_from_ip_range(self):
        ip_range = self.ip_range.split('-')
        front = int(''.join(['{0:08b}'.format(int(bits)) for bits in ip_range[0].split('.')]), 2)
        back = int(''.join(['{0:08b}'.format(int(bits)) for bits in ip_range[1].split('.')]), 2)
        host_bits = len(bin(front ^ back)[2:])
        self.total_host_count = 2 ** host_bits

        step1 = {'Front': '.'.join(['{0:08b}'.format(int(bits)) for bits in ip_range[0].split('.')]),
                 'Back': '.'.join(['{0:08b}'.format(int(bits)) for bits in ip_range[1].split('.')])}
        step2 = {'Comparison': '.'.join([byte for byte in re.findall('........',
                                                                     ('1'*(32 - host_bits)+'0'*host_bits))])}
        step3 = {'Host Bits': host_bits}
        self.total_host_count_steps = (step1, step2, step3)

    """ ASSIGNABLE HOST COUNT """
    # Calculate assignable host count from total host count
    def calculate_assignable_host_count(self):
        self.assignable_host_count = int(self.total_host_count) - 2

    # Calculate assignable host count from CIDR
    def calculate_assignable_host_count_from_cidr(self):
        cidr = self.cidr_address.split('/')[1]
        host_bits = (32 - int(cidr))
        self.assignable_host_count = (2 ** host_bits) - 2

        step1 = {'CIDR': cidr}
        step2 = {'Host Bits': '32 - {} = {}'.format(cidr, host_bits)}
        self.assignable_host_count_steps = (step1, step2)

    # Calculate assignable host count from Netmask
    def calculate_assignable_host_count_from_netmask(self):
        host_bits = (''.join(['{0:08b}'.format(int(bits)) for bits in self.netmask.split('.')])).count('0')
        self.assignable_host_count = (2 ** host_bits) - 2

        step1 = {'Netmask Binary': '.'.join(['{0:08b}'.format(int(bits)) for bits in self.netmask.split('.')])}
        step2 = {'Host Bits': host_bits}
        self.assignable_host_count_steps = (step1, step2)

    # Calculate assignable host count from assignable IP range
    def calculate_assignable_host_count_from_ip_range(self):
        ip_range = self.ip_range.split('-')
        front = int(''.join(['{0:08b}'.format(int(bits)) for bits in ip_range[0].split('.')]), 2)
        back = int(''.join(['{0:08b}'.format(int(bits)) for bits in ip_range[1].split('.')]), 2)
        host_bits = len(bin(front ^ back)[2:])
        self.assignable_host_count = (2 ** host_bits) - 2

        step1 = {'Front': '.'.join(['{0:08b}'.format(int(bits)) for bits in ip_range[0].split('.')]),
                 'Back': '.'.join(['{0:08b}'.format(int(bits)) for bits in ip_range[1].split('.')])}
        step2 = {'Comparison': '.'.join([byte for byte in re.findall('........',
                                                                     ('1' * (32 - host_bits) + '0' * host_bits))])}
        step3 = {'Host Bits': host_bits}
        self.assignable_host_count_steps = (step1, step2, step3)

    """ Verify formatting of implemented variables """
    def verify_cidr_address(self):
        if type(self.cidr_address) is str and len(self.cidr_address.split('/')) == 2:
            try:
                ipaddress.ip_network(self.cidr_address)
                return True
            except ValueError:
                return False
        else:
            return False

    def verify_network_address(self):
        return validate_ip(self.network_address)

    def verify_netmask(self):
        if validate_ip(self.netmask):
            netmask_binary = ''.join(['{0:08b}'.format(int(bits)) for bits in self.netmask.split('.')])
            return netmask_binary.count('01') == 0
        else:
            return False

    def verify_broadcast(self):
        return validate_ip(self.broadcast_address)

    def verify_ip_range(self):
        if type(self.ip_range) is str:
            ip_range = self.ip_range.split('-')
            if len(ip_range) == 2:
                return validate_range(ip_range[0], ip_range[1])
            else:
                return False
        else:
            return False

    def verify_total_host_count(self):
        possible_counts = [2**cidr for cidr in range(0, 33)]
        if validate_int(self.total_host_count) and int(self.total_host_count) in possible_counts:
            return True
        else:
            return False

    def verify_assignable_host_count(self):
        possible_counts = [abs((2 ** cidr) - 2) for cidr in range(0, 33)]
        if validate_int(self.assignable_host_count) and int(self.assignable_host_count) in possible_counts:
            return True
        else:
            return False

    def verify_variable_use(self):
        if self.cidr_address != '' \
                or self.network_address != '' \
                or self.netmask != '' \
                or self.broadcast_address != '' \
                or self.ip_range != '' \
                or self.total_host_count != '' \
                or self.assignable_host_count != '':
            return True
        else:
            return False

    def verify_variables(self):
        verifications = []

        # Verify CIDR Address
        if self.cidr_address != '':
            verifications.append(self.verify_cidr_address())
        # Verify Netmask
        if self.netmask != '':
            verifications.append(self.verify_netmask())
        # Verify Network Address
        if self.network_address != '':
            verifications.append(self.verify_network_address())
        # Verify Broadcast Address
        if self.broadcast_address != '':
            verifications.append(self.verify_broadcast())
        # Verify IP range
        if self.ip_range != '':
            verifications.append(self.verify_ip_range())
        # Verify Total Host Count
        if self.total_host_count != '':
            verifications.append(self.verify_total_host_count())
        # Verify Assignable Host Count
        if self.assignable_host_count != '':
            verifications.append(self.verify_assignable_host_count())
        # Verify that there is a variable
        verifications.append(self.verify_variable_use())

        return all(verifications)

    def general_calculation(self):
        variables = [self.cidr_address, self.netmask, self.network_address, self.broadcast_address, self.ip_range,
                     self.total_host_count, self.assignable_host_count]
        count = 0
        while any(variable == '' for variable in variables) and count < 10:
            if self.cidr_address == '' and self.network_address != '':
                try:
                    self.calculate_cidr_from_ip_range()
                except ValueError:
                    try:
                        self.calculate_cidr_from_netmask()
                    except ValueError:
                        pass
            if self.netmask == '':
                try:
                    self.calculate_netmask_from_cidr()
                except IndexError:
                    try:
                        self.calculate_netmask_from_ip_range()
                    except ValueError:
                        pass
            if self.network_address == '' and self.cidr_address == '':
                try:
                    self.calculate_network_address_from_ip_range()
                except ValueError:
                    pass
            if self.network_address == '' and self.cidr_address != '':
                try:
                    self.calculate_network_address_from_cidr()
                except ValueError:
                    pass
            if self.broadcast_address == '':
                try:
                    self.calculate_broadcast_address_from_cidr()
                except ValueError:
                    try:
                        self.calculate_broadcast_address_from_ip_range()
                    except IndexError:
                        pass
            if self.ip_range == '':
                try:
                    self.calculate_ip_range_from_cidr()
                except ValueError:
                    try:
                        self.calculate_ip_range_from_network_broadcast()
                    except ValueError:
                        pass
            if self.total_host_count == '':
                try:
                    self.calculate_total_host_count_from_cidr()
                except IndexError:
                    try:
                        self.calculate_total_host_count_from_ip_range()
                    except ValueError:
                        try:
                            self.calculate_total_host_count_from_netmask()
                        except ValueError:
                            pass
            if self.assignable_host_count == '':
                try:
                    self.calculate_assignable_host_count()
                except (IndexError, TypeError, ValueError):
                    try:
                        self.calculate_assignable_host_count_from_cidr()
                    except IndexError:
                        try:
                            self.calculate_assignable_host_count_from_ip_range()
                        except ValueError:
                            try:
                                self.calculate_assignable_host_count_from_netmask()
                            except ValueError:
                                pass
            if self.assignable_host_count == 0:
                self.ip_range = 'n/a'
            variables = [self.cidr_address, self.netmask, self.network_address, self.broadcast_address, self.ip_range,
                         self.total_host_count, self.assignable_host_count]
            count += 1

    def reset_variables(self):
        self.__init__()
        pass


def validate_ip(address):
    try:
        ipaddress.ip_address(str(address))
        return True
    except ValueError:
        return False


def validate_range(front, back):
    try:
        return ipaddress.IPv4Address(str(front)) < ipaddress.IPv4Address(str(back))
    except ipaddress.AddressValueError:
        return False


def validate_int(count):
    try:
        int(count)
        return True
    except ValueError:
        return False
