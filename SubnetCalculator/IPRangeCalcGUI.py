# Title:     Subnet Calculator: Assignable IP Range Calculator GUI
# Date:      04-15-2017


from SubnetCalculator.SubnetCalculator import Subnet
from SubnetCalculator.HelpSubnetCalcGUI import HelpGUI
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import LabelFrame
import ipaddress


class IPRangeCalcGUI:
    def __init__(self):
        self.subnet = Subnet()

        self.range = Tk()
        self.range.wm_title('Assignable IP Range Calculator')

        self.ip_range_from_cidr = LabelFrame(self.range, text='Assignable IP Range: CIDR Address')
        self.cidr_label = Label(self.ip_range_from_cidr, text='CIDR Address:', width=25)
        self.cidr_entry = Entry(self.ip_range_from_cidr, width=25)

        self.ip_range_from_network_broadcast = LabelFrame(self.range, text='Assignable IP Range: Network '
                                                                           'Address, Broadcast Address')
        self.network = Label(self.ip_range_from_network_broadcast, text='Network Address:', width=25)
        self.broadcast = Label(self.ip_range_from_network_broadcast, text='Broadcast Address:', width=25)
        self.network_entry = Entry(self.ip_range_from_network_broadcast, width=25)
        self.broadcast_entry = Entry(self.ip_range_from_network_broadcast, width=25)

        self.learning_steps = LabelFrame(self.range, text='Learning Steps')

        self.calculate = Button(self.ip_range_from_cidr, text='Calculate',
                                command=lambda: self.get_ip_range_from_cidr())
        self.calculate2 = Button(self.ip_range_from_network_broadcast, text='Calculate',
                                 command=lambda: self.get_ip_range_from_network_broadcast())

        self.ip_range_from_cidr.grid(row=0)
        self.ip_range_from_network_broadcast.grid(row=1)
        self.learning_steps.grid(row=2, sticky='W')

        self.cidr_label.grid(row=0, column=0, sticky='W')
        self.cidr_entry.grid(row=0, column=1)
        self.calculate.grid(row=0, column=2)

        self.network.grid(row=0, column=0, sticky='W')
        self.broadcast.grid(row=0, column=1, sticky='W')
        self.network_entry.grid(row=1, column=0)
        self.broadcast_entry.grid(row=1, column=1)
        self.calculate2.grid(row=1, column=2)

        # self.broadcast.mainloop()

    def get_ip_range_from_cidr(self):
        if self.subnet.ip_range != '':
            self.clear_and_reset()
        else:
            self.subnet.cidr_address = self.cidr_entry.get()

            if self.subnet.verify_variables():
                self.subnet.calculate_ip_range_from_cidr()
                steps = self.subnet.ip_range_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                cidr_address = Label(self.learning_steps, text='CIDR Address: {}'.format(self.subnet.cidr_address))
                step2 = Label(self.learning_steps, text='Step 2:')
                front = Label(self.learning_steps, text='Front: {}'.format(steps[0]['Front']))
                step3 = Label(self.learning_steps, text='Step 3:')
                cidr = Label(self.learning_steps, text='CIDR: {}'.format(steps[1]['CIDR']))
                host = Label(self.learning_steps, text='Host Bits: 32 - {} = {}'.format(steps[1]['CIDR'],
                                                                                        (32 - int(steps[1]['CIDR']))))
                step4 = Label(self.learning_steps, text='Step 4:')
                net_binary = Label(self.learning_steps, text='Network Binary: {}'.format(steps[1]['Network Binary']))
                step5 = Label(self.learning_steps, text='Step 5:')
                back_binary = Label(self.learning_steps,
                                    text='Back Binary (Broadcast - 1): {}'.format(steps[2]['Back Binary']))
                step6 = Label(self.learning_steps, text='Step 6:')
                ip_range = Label(self.learning_steps, text='Assignable IP Range: {}'.format(self.subnet.ip_range))

                step1.grid(row=0, column=0, sticky='W')
                cidr_address.grid(row=0, column=1, columnspan=2, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                front.grid(row=1, column=1, columnspan=2, sticky='W')
                step3.grid(row=2, column=0, sticky='W')
                cidr.grid(row=2, column=1, sticky='W')
                host.grid(row=2, column=2, sticky='W')
                step4.grid(row=3, column=0, sticky='W')
                net_binary.grid(row=3, column=1, columnspan=2, sticky='W')
                step5.grid(row=4, column=0, sticky='W')
                back_binary.grid(row=4, column=1, columnspan=2, sticky='W')
                step6.grid(row=5, column=0, sticky='W')
                ip_range.grid(row=5, column=1, columnspan=2, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def get_ip_range_from_network_broadcast(self):
        if self.subnet.ip_range != '':
            self.clear_and_reset()
        else:
            self.subnet.network_address = self.network_entry.get()
            self.subnet.broadcast_address = self.broadcast_entry.get()

            if self.subnet.network_address != '' and self.subnet.broadcast_address != '' \
                    and self.subnet.verify_variables() \
                    and (ipaddress.IPv4Address(self.subnet.network_address) + 2) \
                            < ipaddress.IPv4Address(self.subnet.broadcast_address):
                self.subnet.calculate_ip_range_from_network_broadcast()
                steps = self.subnet.ip_range_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                network = Label(self.learning_steps, text='Network Address: {}'.format(self.subnet.network_address))
                broadcast = Label(self.learning_steps,
                                  text='Broadcast Address: {}'.format(self.subnet.broadcast_address))
                step2 = Label(self.learning_steps, text='Step 2:')
                front = Label(self.learning_steps, text='Front: {}'.format(steps[0]['Front']))
                step3 = Label(self.learning_steps, text='Step 3:')
                back = Label(self.learning_steps, text='Back: {}'.format(steps[1]['Back']))
                step4 = Label(self.learning_steps, text='Step 4:')
                ip_range = Label(self.learning_steps, text='Assignable IP Range: {}'.format(self.subnet.ip_range))

                step1.grid(row=0, column=0, sticky='W')
                network.grid(row=0, column=1, sticky='W')
                broadcast.grid(row=0, column=2, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                front.grid(row=1, column=1, sticky='W')
                step3.grid(row=2, column=0, sticky='W')
                back.grid(row=2, column=1, sticky='W')
                step4.grid(row=3, column=0, sticky='W')
                ip_range.grid(row=3, column=1, columnspan=2, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def clear_and_reset(self):
        self.cidr_entry.delete(0, 'end')
        self.network_entry.delete(0, 'end')
        self.broadcast_entry.delete(0, 'end')
        self.subnet.reset_variables()
        for child in self.learning_steps.winfo_children():
            child.destroy()

    def generate_main(self):
        self.range.mainloop()
