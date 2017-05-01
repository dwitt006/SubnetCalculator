# Title:     Subnet Calculator: Total Host Count Calculator GUI
# Date:      04-16-2017


from SubnetCalculator.SubnetCalculator import Subnet
from SubnetCalculator.HelpSubnetCalcGUI import HelpGUI
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import LabelFrame


class TotalHostCalcGUI:
    def __init__(self):
        self.subnet = Subnet()

        self.total = Tk()
        self.total.wm_title('Total Host Count Calculator')

        self.count_from_cidr = LabelFrame(self.total, text='Total Host Count: CIDR Address')
        self.cidr_label = Label(self.count_from_cidr, text='CIDR Address:', width=20)
        self.cidr_entry = Entry(self.count_from_cidr, width=25)

        self.count_from_netmask = LabelFrame(self.total, text='Total Host Count: Netmask')
        self.netmask_label = Label(self.count_from_netmask, text='Netmask:', width=20)
        self.netmask_entry = Entry(self.count_from_netmask, width=25)

        self.count_from_ip_range = LabelFrame(self.total, text='Total Host Count: Assignable IP Range')
        self.ip_range_label = Label(self.count_from_ip_range, text='Assignable IP Range:', width=20)
        self.ip_range_entry = Entry(self.count_from_ip_range, width=25)

        self.learning_steps = LabelFrame(self.total, text='Learning Steps')

        self.calculate = Button(self.count_from_cidr, text='Calculate', command=lambda: self.get_count_from_cidr())
        self.calculate2 = Button(self.count_from_netmask, text='Calculate',
                                 command=lambda: self.get_count_from_netmask())
        self.calculate3 = Button(self.count_from_ip_range, text='Calculate',
                                 command=lambda: self.get_count_from_ip_range())

        self.count_from_cidr.grid(row=0)
        self.count_from_netmask.grid(row=1)
        self.count_from_ip_range.grid(row=2)
        self.learning_steps.grid(row=3, sticky='W')

        self.cidr_label.grid(row=0, column=0, sticky='W')
        self.cidr_entry.grid(row=0, column=1)
        self.calculate.grid(row=0, column=2)

        self.netmask_label.grid(row=0, column=0, sticky='W')
        self.netmask_entry.grid(row=0, column=1)
        self.calculate2.grid(row=0, column=2)

        self.ip_range_label.grid(row=0, column=0, sticky='W')
        self.ip_range_entry.grid(row=0, column=1)
        self.calculate3.grid(row=0, column=2)

        # self.total.mainloop()
        pass

    def get_count_from_cidr(self):
        if self.subnet.total_host_count != '':
            self.clear_and_reset()
        else:
            self.subnet.cidr_address = self.cidr_entry.get()

            if self.subnet.verify_variables():
                self.subnet.calculate_total_host_count_from_cidr()
                steps = self.subnet.total_host_count_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                cidr_address = Label(self.learning_steps, text='CIDR Address: {}'.format(self.subnet.cidr_address))
                step2 = Label(self.learning_steps, text='Step 2:')
                cidr = Label(self.learning_steps, text='CIDR: {}'.format(steps[0]['CIDR']))
                step3 = Label(self.learning_steps, text='Step 3:')
                host = Label(self.learning_steps, text='Host Bits: {}'.format(steps[1]['Host Bits']))
                step4 = Label(self.learning_steps, text='Step 4:')
                count = Label(self.learning_steps,
                              text='Total Host Count: 2{} = {}'.format(exponent(steps[1]['Host Bits'].split(' ')[-1]),
                                                                       self.subnet.total_host_count))

                step1.grid(row=0, column=0, sticky='W')
                cidr_address.grid(row=0, column=1, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                cidr.grid(row=1, column=1, sticky='W')
                step3.grid(row=2, column=0, sticky='W')
                host.grid(row=2, column=1, sticky='W')
                step4.grid(row=3, column=0, sticky='W')
                count.grid(row=3, column=1, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def get_count_from_netmask(self):
        if self.subnet.total_host_count != '':
            self.clear_and_reset()
        else:
            self.subnet.netmask = self.netmask_entry.get()

            if self.subnet.verify_variables():
                self.subnet.calculate_total_host_count_from_netmask()
                steps = self.subnet.total_host_count_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                netmask = Label(self.learning_steps, text='Netmask: {}'.format(self.subnet.netmask))
                step2 = Label(self.learning_steps, text='Step 2:')
                netmask_binary = Label(self.learning_steps,
                                       text='Netmask Binary: {}'.format(steps[0]['Netmask Binary']))
                step3 = Label(self.learning_steps, text='Step 3:')
                host = Label(self.learning_steps, text='Host Bits: {}'.format(steps[1]['Host Bits']))
                step4 = Label(self.learning_steps, text='Step 4:')
                count = Label(self.learning_steps,
                              text='Total Host Count: 2{} = {}'.format(exponent(str(steps[1]['Host Bits'])),
                                                                       self.subnet.total_host_count))

                step1.grid(row=0, column=0, sticky='W')
                netmask.grid(row=0, column=1, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                netmask_binary.grid(row=1, column=1, sticky='W')
                step3.grid(row=2, column=0, sticky='W')
                host.grid(row=2, column=1, sticky='W')
                step4.grid(row=3, column=0, sticky='W')
                count.grid(row=3, column=1, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def get_count_from_ip_range(self):
        if self.subnet.total_host_count != '':
            self.clear_and_reset()
        else:
            self.subnet.ip_range = self.ip_range_entry.get()

            if self.subnet.verify_variables():
                self.subnet.calculate_total_host_count_from_ip_range()
                steps = self.subnet.total_host_count_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                ip_range = Label(self.learning_steps, text='Assignable IP Range: {}'.format(self.subnet.ip_range))
                step2 = Label(self.learning_steps, text='Step 2:')
                front = Label(self.learning_steps, text='Front: {}'.format(steps[0]['Front']))
                back = Label(self.learning_steps, text=' Back: {}'.format(steps[0]['Back']))
                step3 = Label(self.learning_steps, text='Step 3:')
                comparison = Label(self.learning_steps, text='Comparison: {}'.format(steps[1]['Comparison']))
                step4 = Label(self.learning_steps, text='Step 4:')
                host = Label(self.learning_steps, text='Host Bits: {}'.format(steps[2]['Host Bits']))
                step5 = Label(self.learning_steps, text='Step 5:')
                count = Label(self.learning_steps,
                              text='Total Host Count: 2{} = {}'.format(exponent(str(steps[2]['Host Bits'])),
                                                                       self.subnet.total_host_count))

                step1.grid(row=0, column=0, sticky='W')
                ip_range.grid(row=0, column=1, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                front.grid(row=1, column=1, sticky='W')
                back.grid(row=2, column=1, sticky='W')
                step3.grid(row=3, column=0, sticky='W')
                comparison.grid(row=3, column=1, sticky='W')
                step4.grid(row=4, column=0, sticky='W')
                host.grid(row=4, column=1, sticky='W')
                step5.grid(row=5, column=0, sticky='W')
                count.grid(row=5, column=1, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def clear_and_reset(self):
        self.cidr_entry.delete(0, 'end')
        self.netmask_entry.delete(0, 'end')
        self.ip_range_entry.delete(0, 'end')
        self.subnet.reset_variables()
        for child in self.learning_steps.winfo_children():
            child.destroy()

    def generate_main(self):
        self.total.mainloop()


def exponent(string_of_numbers):
    sup = str.maketrans('0123456789',
                        u'\u2070'u'\xb9'u'\xb2'u'\xb3'u'\u2074'u'\u2075'u'\u2076'u'\u2077'u'\u2078'u'\u2079')
    return string_of_numbers.translate(sup)
