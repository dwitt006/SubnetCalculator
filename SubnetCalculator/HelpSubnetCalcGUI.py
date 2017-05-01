# Title:     Subnet Calculator GUI
# Date:      04-12-2017


from tkinter import Tk
from tkinter import Label
from tkinter import Button


class HelpGUI:
    def __init__(self):
        self.helper = Tk()
        self.helper.wm_title('Help')

        self.cidr_label = Label(self.helper, text='CIDR Address:')
        self.network_label = Label(self.helper, text='Network Address:')
        self.netmask_label = Label(self.helper, text='Netmask:')
        self.broadcast_label = Label(self.helper, text='Broadcast Address:')
        self.ip_range_label = Label(self.helper, text='Assignable IP Range:')
        self.total_host_label = Label(self.helper, text='Total Host Count:')
        self.assignable_host_label = Label(self.helper, text='Assignable Host Count:')

        self.cidr_ex = Label(self.helper, text='\t152.2.136.0/26')
        self.network_ex = Label(self.helper, text='\t152.2.136.0')
        self.netmask_ex = Label(self.helper, text='\t255.255.255.192')
        self.broadcast_ex = Label(self.helper, text='\t152.2.136.63')
        self.ip_range_ex = Label(self.helper, text='\t152.2.136.1-152.2.136.62')
        self.total_host_ex = Label(self.helper, text='\t64')
        self.assignable_host_ex = Label(self.helper, text='\t62')

        self.ex_label = Label(self.helper, text='Example: Proper Input Format')
        self.close = Button(self.helper, text='OK', command=lambda: self.helper.destroy())

        self.cidr_label.grid(row=1, column=0, sticky='E')
        self.network_label.grid(row=2, column=0, sticky='E')
        self.netmask_label.grid(row=3, column=0, sticky='E')
        self.broadcast_label.grid(row=4, column=0, sticky='E')
        self.ip_range_label.grid(row=5, column=0, sticky='E')
        self.total_host_label.grid(row=6, column=0, sticky='E')
        self.assignable_host_label.grid(row=7, column=0, sticky='E')

        self.cidr_ex.grid(row=1, column=1, sticky='W')
        self.network_ex.grid(row=2, column=1, sticky='W')
        self.netmask_ex.grid(row=3, column=1, sticky='W')
        self.broadcast_ex.grid(row=4, column=1, sticky='W')
        self.ip_range_ex.grid(row=5, column=1, sticky='W')
        self.total_host_ex.grid(row=6, column=1, sticky='W')
        self.assignable_host_ex.grid(row=7, column=1, sticky='W')

        self.ex_label.grid(row=0, columnspan=2)
        self.close.grid(row=8, columnspan=2)

        self.helper.mainloop()
