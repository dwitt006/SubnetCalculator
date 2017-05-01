# Title:     Subnet Calculator: Broadcast Calculator GUI
# Date:      04-13-2017


from SubnetCalculator.SubnetCalculator import Subnet
from SubnetCalculator.HelpSubnetCalcGUI import HelpGUI
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import LabelFrame


class BroadcastCalcGUI:
    def __init__(self):
        self.subnet = Subnet()

        self.broadcast = Tk()
        self.broadcast.wm_title('Broadcast Address Calculator')

        self.broadcast_from_cidr = LabelFrame(self.broadcast, text='Broadcast Address: CIDR Address')
        self.cidr_label = Label(self.broadcast_from_cidr, text='CIDR Address:', width=20)
        self.cidr_entry = Entry(self.broadcast_from_cidr, width=25)

        self.broadcast_from_ip_range = LabelFrame(self.broadcast, text='Broadcast Address: Assignable IP Range')
        self.ip_range_label = Label(self.broadcast_from_ip_range, text='Assignable IP Range:', width=20)
        self.ip_range_entry = Entry(self.broadcast_from_ip_range, width=25)

        self.learning_steps = LabelFrame(self.broadcast, text='Learning Steps')

        self.calculate = Button(self.broadcast_from_cidr, text='Calculate',
                                command=lambda: self.get_broadcast_from_cidr())
        self.calculate2 = Button(self.broadcast_from_ip_range, text='Calculate',
                                 command=lambda: self.get_broadcast_from_ip_range())

        self.broadcast_from_cidr.grid(row=0)
        self.broadcast_from_ip_range.grid(row=1)
        self.learning_steps.grid(row=2, sticky='W')

        self.cidr_label.grid(row=0, column=0, sticky='W')
        self.cidr_entry.grid(row=0, column=1)
        self.calculate.grid(row=0, column=2)

        self.ip_range_label.grid(row=0, column=0, sticky='W')
        self.ip_range_entry.grid(row=0, column=1)
        self.calculate2.grid(row=0, column=2)

        # self.broadcast.mainloop()

    def get_broadcast_from_cidr(self):
        if self.subnet.broadcast_address != '':
            self.clear_and_reset()
        else:
            self.subnet.cidr_address = self.cidr_entry.get()

            if self.subnet.verify_variables():
                self.subnet.calculate_broadcast_address_from_cidr()
                steps = self.subnet.broadcast_address_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                cidr_address = Label(self.learning_steps, text='CIDR Address: {}'.format(self.subnet.cidr_address))
                step2 = Label(self.learning_steps, text='Step 2:')
                cidr = Label(self.learning_steps, text='CIDR: {}'.format(steps[0]['CIDR']))
                host = Label(self.learning_steps, text='Host Bits: 32 - {} = {}'.format(steps[0]['CIDR'],
                                                                                        (32 - int(steps[0]['CIDR']))))
                step3 = Label(self.learning_steps, text='Step 3:')
                net_binary = Label(self.learning_steps, text='Network Binary: {}'.format(steps[0]['Network Binary']))
                step4 = Label(self.learning_steps, text='Step 4:')
                broadcast_binary = Label(self.learning_steps,
                                         text='Broadcast Binary: {}'.format(steps[1]['Broadcast Binary']))
                step5 = Label(self.learning_steps, text='Step 5:')
                broadcast = Label(self.learning_steps,
                                  text='Broadcast Address: {}'.format(self.subnet.broadcast_address))

                step1.grid(row=0, column=0, sticky='W')
                cidr_address.grid(row=0, column=1, columnspan=2, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                cidr.grid(row=1, column=1, sticky='W')
                host.grid(row=1, column=2, sticky='W')
                step3.grid(row=2, column=0, sticky='W')
                net_binary.grid(row=2, column=1, columnspan=2, sticky='W')
                step4.grid(row=3, column=0, sticky='W')
                broadcast_binary.grid(row=3, column=1, columnspan=2, sticky='W')
                step5.grid(row=4, column=0, sticky='W')
                broadcast.grid(row=4, column=1, columnspan=2, sticky='W')
            else:
                self.clear_and_reset()
                HelpGUI()

    def get_broadcast_from_ip_range(self):
        if self.subnet.broadcast_address != '':
            self.clear_and_reset()
        else:
            self.subnet.ip_range = self.ip_range_entry.get()

            if self.subnet.verify_variables():
                self.subnet.calculate_broadcast_address_from_ip_range()
                steps = self.subnet.broadcast_address_steps

                step1 = Label(self.learning_steps, text='Step 1:')
                ip_range = Label(self.learning_steps, text='Assignable IP Range: {}'.format(self.subnet.ip_range))
                step2 = Label(self.learning_steps, text='Step 2:')
                back = Label(self.learning_steps, text='(Back + 1): {}'.format(steps[0]['Back + 1']))
                step3 = Label(self.learning_steps, text='Step 3:')
                broadcast = Label(self.learning_steps,
                                  text='Broadcast Address: {}'.format(self.subnet.broadcast_address))

                step1.grid(row=0, column=0, sticky='W')
                ip_range.grid(row=0, column=1, sticky='W')
                step2.grid(row=1, column=0, sticky='W')
                back.grid(row=1, column=1, sticky='W')
                step3.grid(row=2, column=0, sticky='W')
                broadcast.grid(row=2, column=1, sticky='W')
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
        self.broadcast.mainloop()
