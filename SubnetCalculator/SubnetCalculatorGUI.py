# Title:     Subnet Calculator: Subnet Calculator GUI
# Date:      04-04-2017


from SubnetCalculator.GenSubnetCalcGUI import GenSubnetCalcGUI
from SubnetCalculator.CIDRCalcGUI import CIDRCalcGUI
from SubnetCalculator.NetCalcGUI import NetCalcGUI
from SubnetCalculator.NetmaskCalcGUI import NetmaskCalcGUI
from SubnetCalculator.BroadcastCalcGUI import BroadcastCalcGUI
from SubnetCalculator.IPRangeCalcGUI import IPRangeCalcGUI
from SubnetCalculator.TotalHostCalcGUI import TotalHostCalcGUI
from SubnetCalculator.AssignableHostCountCalcGUI import AssignHostCalcGUI
from tkinter import Tk
from tkinter import Button


class SubnetCalculatorGUI:
    def __init__(self):
        self.calculator = Tk()
        self.calculator.wm_title('Subnet Calculator')
        self.general_calculator = Button(self.calculator, text='General Subnet Calculator', width=50,
                                         command=lambda: GenSubnetCalcGUI().generate_main())
        self.cidr_calculator = Button(self.calculator, text='CIDR Calculator', width=50,
                                      command=lambda: CIDRCalcGUI().generate_main())
        self.network_address_calculator = Button(self.calculator, text='Network Address Calculator', width=50,
                                                 command=lambda: NetCalcGUI().generate_main())
        self.netmask_calculator = Button(self.calculator, text='Netmask Calculator', width=50,
                                         command=lambda: NetmaskCalcGUI().generate_main())
        self.broadcast_address_calculator = Button(self.calculator, text='Broadcast Address Calculator', width=50,
                                                   command=lambda: BroadcastCalcGUI().generate_main())
        self.ip_range_calculator = Button(self.calculator, text='Assignable IP Range Calculator', width=50,
                                          command=lambda: IPRangeCalcGUI().generate_main())
        self.total_host_calculator = Button(self.calculator, text='Total Host Count Calculator', width=50,
                                            command=lambda: TotalHostCalcGUI().generate_main())
        self.assignable_host_calculator = Button(self.calculator, text='Assignable Host Count Calculator', width=50,
                                                 command=lambda: AssignHostCalcGUI().generate_main())

        self.general_calculator.pack()
        self.cidr_calculator.pack()
        self.network_address_calculator.pack()
        self.netmask_calculator.pack()
        self.broadcast_address_calculator.pack()
        self.ip_range_calculator.pack()
        self.total_host_calculator.pack()
        self.assignable_host_calculator.pack()

        self.calculator.mainloop()
