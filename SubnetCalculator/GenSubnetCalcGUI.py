# Title:     Subnet Calculator: General Subnet Calculator GUI
# Date:      04-12-2017


from SubnetCalculator.SubnetCalculator import Subnet
from SubnetCalculator.HelpSubnetCalcGUI import HelpGUI
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button


class GenSubnetCalcGUI:
    def __init__(self):
        self.subnet = Subnet()

        self.general_calculator = Tk()
        self.general_calculator.wm_title('General Subnet Calculator')

        self.cidr_label = Label(self.general_calculator, text='CIDR Address:')
        self.network_label = Label(self.general_calculator, text='Network Address:')
        self.netmask_label = Label(self.general_calculator, text='Netmask:')
        self.broadcast_label = Label(self.general_calculator, text='Broadcast Address:')
        self.ip_range_label = Label(self.general_calculator, text='Assignable IP Range:')
        self.total_host_label = Label(self.general_calculator, text='Total Host Count:')
        self.assignable_host_label = Label(self.general_calculator, text='Assignable Host Count:')

        self.cidr_entry = Entry(self.general_calculator, width=25)
        self.network_entry = Entry(self.general_calculator, width=25)
        self.netmask_entry = Entry(self.general_calculator, width=25)
        self.broadcast_entry = Entry(self.general_calculator, width=25)
        self.ip_range_entry = Entry(self.general_calculator, width=25)
        self.total_host_entry = Entry(self.general_calculator, width=25)
        self.assignable_host_entry = Entry(self.general_calculator, width=25)

        self.calculate = Button(self.general_calculator, text='Calculate', command=lambda: self.get_entries())

        self.cidr_label.grid(row=0, column=0, sticky='E')
        self.network_label.grid(row=1, column=0, sticky='E')
        self.netmask_label.grid(row=2, column=0, sticky='E')
        self.broadcast_label.grid(row=3, column=0, sticky='E')
        self.ip_range_label.grid(row=4, column=0, sticky='E')
        self.total_host_label.grid(row=5, column=0, sticky='E')
        self.assignable_host_label.grid(row=6, column=0, sticky='E')

        self.cidr_entry.grid(row=0, column=1)
        self.network_entry.grid(row=1, column=1)
        self.netmask_entry.grid(row=2, column=1)
        self.broadcast_entry.grid(row=3, column=1)
        self.ip_range_entry.grid(row=4, column=1)
        self.total_host_entry.grid(row=5, column=1)
        self.assignable_host_entry.grid(row=6, column=1)

        self.calculate.grid(row=7, columnspan=2)

        # self.general_calculator.mainloop()

    def clear_entries(self):
        self.cidr_entry.delete(0, 'end')
        self.network_entry.delete(0, 'end')
        self.netmask_entry.delete(0, 'end')
        self.broadcast_entry.delete(0, 'end')
        self.ip_range_entry.delete(0, 'end')
        self.total_host_entry.delete(0, 'end')
        self.assignable_host_entry.delete(0, 'end')

    def get_entries(self):
        if self.subnet.cidr_address != '':
            self.clear_entries()
            self.subnet.reset_variables()
        else:
            self.subnet.cidr_address = self.cidr_entry.get()
            self.subnet.network_address = self.network_entry.get()
            self.subnet.netmask = self.netmask_entry.get()
            self.subnet.broadcast_address = self.broadcast_entry.get()
            self.subnet.ip_range = self.ip_range_entry.get()
            self.subnet.total_host_count = self.total_host_entry.get()
            self.subnet.assignable_host_count = self.assignable_host_entry.get()

            self.clear_entries()

            if self.subnet.verify_variables():
                self.subnet.general_calculation()

                self.cidr_entry.insert(0, self.subnet.cidr_address)
                self.network_entry.insert(0, self.subnet.network_address)
                self.netmask_entry.insert(0, self.subnet.netmask)
                self.broadcast_entry.insert(0, self.subnet.broadcast_address)
                self.ip_range_entry.insert(0, self.subnet.ip_range)
                self.total_host_entry.insert(0, str(self.subnet.total_host_count))
                self.assignable_host_entry.insert(0, str(self.subnet.assignable_host_count))

            else:
                self.clear_entries()
                self.subnet.reset_variables()
                HelpGUI()

    def generate_main(self):
        self.general_calculator.mainloop()
