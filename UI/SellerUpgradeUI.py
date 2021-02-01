from UI.UpgradeUI import UpgradeUI


class SellerUpgradeUI(UpgradeUI):

    # This class inherits UpgradeUI class
    # The back method implement by here
    # Open office seller dashboard again
    def back(self):
        self.window.destroy()
        from UI.SellerDashboard import SellerDashboard
        SellerDashboard()
