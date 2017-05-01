# Title:     Subnet Calculator: Netmask Calculator GUI
# Date:      04-13-2017


from SubnetCalculator.SubnetCalculator import Subnet
from SubnetCalculator.HelpSubnetCalcGUI import HelpGUI
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import LabelFrame


class NetmaskCalcGUI:
    def __init__(self):
        self.subnet = Subnet()

        self.net = Tk()
        self.net.wm_title('Netmask Calculator')

        self.netmask_from_cidr = LabelFrame(self.net, text='Netmask: CIDR Address')
        self.cidr_label = Label(self.netmask_from_cidr, text='CIDR Address:', width=20)
        self.cidr_entry = Entry(self.netmask_from_cidr, width=25)

        self.netmask_from_ip_range = LabelFrame(self.net, text='Netmask: Assignable IP Range')
        self.ip_range_label = Label(self.netmask_from_ip_range, text='Assignable IP Range:', width=20)
        self.ip_range_entry = Entry(self.netmask_from_ip_range, width=25)

        self.learning_steps = LabelFrame(self.net, text='Learning Steps')

        self.calculate = Button(self.netmask_from_cidr, text='Calculate', command=lambda: self.get_net_from_cidr())
        self.calculate2 = Button(self.netmask_from_ip_range, text='Calculate',
                                 command=lambda: self.get_net_from_ip_range())

        self.netmask_from_cidr.grid(row=0)
        self.netmask_from_ip_range.grid(row=1)
        self.learning_steps.grid(row=2, sticky='W')

        self.cidr_label.grid(row=0, column=0, sticky='W')
        self.cidr_entry.grid(row=0, column=1)
        self.calculate.grid(row=0, column=2)

        self.ip_range_label.grid(row=0, column=0, sticky='W')
        self.ip_range_entry.grid(row=0, column=1)
        self.calculate2.grid(row=0, column=2)

        # self.net.mainloop()

    def get_net_from_cidr(self):
        if self.subnet.netmask != '':
            self.clear_and_reset()
        else:
            self.subnet.cidr_address = self.cidr_entry.get()

            if self.subnet.verify_variables():
                self.subnet.calculate_netmask_from_cidr()
                steps = self.subnet.netmask_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                cidr_address = Label(self.learning_steps, text='CIDR Address: {}'.format(self.subnet.cidr_address))
                step2 = Label(self.learning_steps, text='Step 2:')
                net_bits = Label(self.learning_steps, text='Network Bits: {}'.format(steps[0]['Network Bits']))
                host_bits = Label(self.learning_steps, text='Host Bits: {}'.format(steps[0]['Host Bits']))
                step3 = Label(self.learning_steps, text='Step 3:')
                mask_binary = Label(self.learning_steps, text='Netmask Binary: {}'.format(steps[1]['Netmask Binary']))
                step4 = Label(self.learning_steps, text='Step 4:')
                netmask = Label(self.learning_steps, text='Netmask: {}'.format(self.subnet.netmask))

                step1.grid(row=0, column=0, sticky='W')
                cidr_address.grid(row=0, column=1, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                net_bits.grid(row=1, column=1, sticky='W')
                host_bits.grid(row=1, column=2, sticky='W')
                step3.grid(row=2, column=0, sticky='W')
                mask_binary.grid(row=2, column=1, columnspan=2, sticky='W')
                step4.grid(row=3, column=0, sticky='W')
                netmask.grid(row=3, column=1, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def get_net_from_ip_range(self):
        if self.subnet.netmask != '':
            self.clear_and_reset()
        else:
            self.subnet.ip_range = self.ip_range_entry.get()

            if self.subnet.verify_variables():
                self.subnet.calculate_netmask_from_ip_range()
                steps = self.subnet.netmask_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                ip_range = Label(self.learning_steps, text='Assignable IP Range: {}'.format(self.subnet.ip_range))
                step2 = Label(self.learning_steps, text='Step 2:')
                front = Label(self.learning_steps, text='Front: {}'.format(steps[0]['Front']))
                back = Label(self.learning_steps, text=' Back: {}'.format(steps[0]['Back']))
                step3 = Label(self.learning_steps, text='Step 3:')
                comparison = Label(self.learning_steps, text='Comparison: {}'.format(steps[1]['Comparison']))
                step4 = Label(self.learning_steps, text='Step 4:')
                netmask = Label(self.learning_steps, text='Netmask: {}'.format(self.subnet.netmask))

                step1.grid(row=0, column=0, sticky='W')
                ip_range.grid(row=0, column=1, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                front.grid(row=1, column=1, sticky='W')
                back.grid(row=2, column=1, sticky='W')
                step3.grid(row=3, column=0, sticky='W')
                comparison.grid(row=3, column=1, sticky='W')
                step4.grid(row=4, column=0, sticky='W')
                netmask.grid(row=4, column=1, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def clear_and_reset(self):
        self.cidr_entry.delete(0, 'end')
        self.ip_range_entry.delete(0, 'end')
        self.subnet.reset_variables()
        for child in self.learning_steps.winfo_children():
            child.destroy()

    def generate_main(self):
        self.net.mainloop()
