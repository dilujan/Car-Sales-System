from UI.UpgradeUI import UpgradeUI


class OfficeStaffUpgradeUI(UpgradeUI):
    
    # This class inherits UpgradeUI class
    # The back method implement by here
    # Open office staff dashboard again
    def back(self):
        self.window.destroy()
        from UI.OfficeStaffDashboard import OfficeStaffDashBoard
        OfficeStaffDashBoard()
