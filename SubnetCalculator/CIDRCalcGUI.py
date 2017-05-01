# Title:     Subnet Calculator: CIDR Calculator GUI
# Date:      04-12-2017


from SubnetCalculator.SubnetCalculator import Subnet
from SubnetCalculator.HelpSubnetCalcGUI import HelpGUI
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import LabelFrame


class CIDRCalcGUI:
    def __init__(self):
        self.subnet = Subnet()

        self.cidr = Tk()
        self.cidr.wm_title('CIDR Calculator')

        self.cidr_from_netmask = LabelFrame(self.cidr, text='CIDR: Network Address & Netmask')
        self.net_address_label = Label(self.cidr_from_netmask, text='Network Address:')
        self.netmask_label = Label(self.cidr_from_netmask, text='Netmask:')
        self.net_address_entry = Entry(self.cidr_from_netmask, width=25)
        self.netmask_entry = Entry(self.cidr_from_netmask, width=25)

        self.cidr_from_ip_range = LabelFrame(self.cidr, text='CIDR: Network Address & Assignable IP Range')
        self.net_address_label2 = Label(self.cidr_from_ip_range, text='Network Address:')
        self.ip_range_label = Label(self.cidr_from_ip_range, text='Assignable IP Range:')
        self.net_address_entry2 = Entry(self.cidr_from_ip_range, width=25)
        self.ip_range_entry = Entry(self.cidr_from_ip_range, width=25)

        self.learning_steps = LabelFrame(self.cidr, text='Learning Steps')

        self.calculate = Button(self.cidr_from_netmask, text='Calculate', command=lambda: self.get_cidr_from_netmask())
        self.calculate2 = Button(self.cidr_from_ip_range, text='Calculate',
                                 command=lambda: self.get_cidr_from_ip_range())

        self.cidr_from_netmask.grid(row=0)
        self.cidr_from_ip_range.grid(row=1)
        self.learning_steps.grid(row=2, sticky='W')

        self.net_address_label.grid(row=0, column=0, sticky='W')
        self.net_address_entry.grid(row=1, column=0)
        self.netmask_label.grid(row=0, column=1, sticky='W')
        self.netmask_entry.grid(row=1, column=1)
        self.calculate.grid(row=1, column=2)

        self.net_address_label2.grid(row=0, column=0, sticky='W')
        self.net_address_entry2.grid(row=1, column=0)
        self.ip_range_label.grid(row=0, column=1, sticky='W')
        self.ip_range_entry.grid(row=1, column=1)
        self.calculate2.grid(row=1, column=2)

        # self.cidr.mainloop()

    def get_cidr_from_netmask(self):
        if self.subnet.cidr_address != '':
            self.clear_and_reset()
        else:
            self.subnet.network_address = self.net_address_entry.get()
            self.subnet.netmask = self.netmask_entry.get()

            if self.subnet.network_address != '' and self.subnet.netmask != '' and self.subnet.verify_variables():
                self.subnet.calculate_cidr_from_netmask()
                steps = self.subnet.cidr_address_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                network = Label(self.learning_steps, text='Network Address: {}'.format(self.subnet.network_address))
                netmask = Label(self.learning_steps, text='NetMask: {}'.format(self.subnet.netmask))
                step2 = Label(self.learning_steps, text='Step 2:')
                binary = Label(self.learning_steps, text='Netmask Binary: {}'.format(steps[0]['Netmask Binary']))
                step3 = Label(self.learning_steps, text='Step 3:')
                count = Label(self.learning_steps, text="(Count 0's from Step 2)")
                cidr = Label(self.learning_steps, text='CIDR: {}'.format(steps[1]['CIDR']))
                step4 = Label(self.learning_steps, text='Step 4:')
                cidr_address = Label(self.learning_steps, text='CIDR Address: {}'.format(self.subnet.cidr_address))

                step1.grid(row=0, column=0, sticky='W')
                network.grid(row=0, column=1, sticky='W')
                netmask.grid(row=0, column=2, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                binary.grid(row=1, column=1, columnspan=2, sticky='W')
                step3.grid(row=2, column=0, sticky='W')
                count.grid(row=2, column=1, sticky='W')
                cidr.grid(row=2, column=2, sticky='W')
                step4.grid(row=3, column=0, sticky='W')
                cidr_address.grid(row=3, column=1, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def get_cidr_from_ip_range(self):
        if self.subnet.cidr_address != '':
            self.clear_and_reset()
        else:
            self.subnet.network_address = self.net_address_entry2.get()
            self.subnet.ip_range = self.ip_range_entry.get()

            if self.subnet.network_address != '' and self.subnet.ip_range != '' and self.subnet.verify_variables():
                self.subnet.calculate_cidr_from_ip_range()
                steps = self.subnet.cidr_address_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                network = Label(self.learning_steps, text='Network Address: {}'.format(self.subnet.network_address))
                ip_range = Label(self.learning_steps, text='Assignable IP Range: {}'.format(self.subnet.ip_range))
                step2 = Label(self.learning_steps, text='Step 2:')
                front = Label(self.learning_steps, text='Front: {}'.format(steps[0]['Front']))
                back = Label(self.learning_steps, text=' Back: {}'.format(steps[0]['Back']))
                step3 = Label(self.learning_steps, text='Step 3:')
                comparison = Label(self.learning_steps, text='Comparison: {}'.format(steps[1]['Comparison']))
                step4 = Label(self.learning_steps, text='Step 4:')
                cidr = Label(self.learning_steps, text='CIDR: {}'.format(steps[2]['CIDR']))
                step5 = Label(self.learning_steps, text='Step 5:')
                cidr_address = Label(self.learning_steps, text='CIDR Address: {}'.format(self.subnet.cidr_address))

                step1.grid(row=0, column=0, sticky='W')
                network.grid(row=0, column=1, sticky='W')
                ip_range.grid(row=1, column=1, sticky='W')
                step2.grid(row=2, column=0, sticky='W')
                front.grid(row=2, column=1, sticky='W')
                back.grid(row=3, column=1, sticky='W')
                step3.grid(row=4, column=0, sticky='W')
                comparison.grid(row=4, column=1, columnspan=2, sticky='W')
                step4.grid(row=5, column=0, sticky='W')
                cidr.grid(row=5, column=1, sticky='W')
                step5.grid(row=6, column=0, sticky='W')
                cidr_address.grid(row=6, column=1, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def clear_and_reset(self):
        self.net_address_entry.delete(0, 'end')
        self.netmask_entry.delete(0, 'end')
        self.net_address_entry2.delete(0, 'end')
        self.ip_range_entry.delete(0, 'end')
        self.subnet.reset_variables()
        for child in self.learning_steps.winfo_children():
            child.destroy()

    def generate_main(self):
        self.cidr.mainloop()
