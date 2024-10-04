#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
class RatioAnalysis:
    def __init__(self, total_assets, total_liabilities, current_assets, current_liabilities, net_income, sales, shareholders_equity):
        self.total_assets = total_assets
        self.total_liabilities = total_liabilities
        self.current_assets = current_assets
        self.current_liabilities = current_liabilities
        self.net_income = net_income
        self.sales = sales
        self.shareholders_equity = shareholders_equity

    # 1. Current Ratio: Current Assets / Current Liabilities
    def current_ratio(self):
        return self.current_assets / self.current_liabilities if self.current_liabilities else 0

    # 2. Quick Ratio: (Current Assets - Inventory) / Current Liabilities
    def quick_ratio(self, inventory):
        return (self.current_assets - inventory) / self.current_liabilities if self.current_liabilities else 0

    # 3. Debt to Equity Ratio: Total Liabilities / Shareholders' Equity
    def debt_to_equity_ratio(self):
        return self.total_liabilities / self.shareholders_equity if self.shareholders_equity else 0

    # 4. Return on Assets (ROA): Net Income / Total Assets
    def return_on_assets(self):
        return self.net_income / self.total_assets if self.total_assets else 0

    # 5. Return on Equity (ROE): Net Income / Shareholders' Equity
    def return_on_equity(self):
        return self.net_income / self.shareholders_equity if self.shareholders_equity else 0

    # 6. Gross Profit Margin: (Sales - Cost of Goods Sold) / Sales
    def gross_profit_margin(self, cogs):
        return (self.sales - cogs) / self.sales if self.sales else 0

    # 7. Net Profit Margin: Net Income / Sales
    def net_profit_margin(self):
        return self.net_income / self.sales if self.sales else 0

    # 8. Asset Turnover Ratio: Sales / Total Assets
    def asset_turnover_ratio(self):
        return self.sales / self.total_assets if self.total_assets else 0

# Example usage
if __name__ == "__main__":
    # Sample data (replace with actual values)
    total_assets = 500000
    total_liabilities = 200000
    current_assets = 150000
    current_liabilities = 50000
    net_income = 50000
    sales = 300000
    shareholders_equity = 300000
    inventory = 40000
    cogs = 180000

    # Initialize the RatioAnalysis class
    ratios = RatioAnalysis(total_assets, total_liabilities, current_assets, current_liabilities, net_income, sales, shareholders_equity)

    # Calculate and print various financial ratios
    print("Current Ratio:", ratios.current_ratio())
    print("Quick Ratio:", ratios.quick_ratio(inventory))
    print("Debt to Equity Ratio:", ratios.debt_to_equity_ratio())
    print("Return on Assets (ROA):", ratios.return_on_assets())
    print("Return on Equity (ROE):", ratios.return_on_equity())
    print("Gross Profit Margin:", ratios.gross_profit_margin(cogs))
    print("Net Profit Margin:", ratios.net_profit_margin())
    print("Asset Turnover Ratio:", ratios.asset_turnover_ratio())


# In[ ]:




