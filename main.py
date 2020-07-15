# Creating a simple Donut Chart for business expenses at Perimeter83
import plotly.graph_objects as go

# Labels And Values Corresponding to Eachother By Their Position In The List
labels = ['Payroll','Rent','Utilities','Taxes','Insurance','Office Supplies','Transportation','Marketing','Memberships','Professional Services']

# Get user input for each value.
pay = input("\nEnter Payroll Expenses: ")
rent = input("\nEnter Rent Expenses: ")
util = input("\nEnter Utilities Expenses: ")
tax = input("\nEnter Taxes Expenses: ")
insur = input("\nEnter Insurance Expenses: ")
os = input("\nEnter Office Supplies Expenses: ")
trans = input("\nEnter Transportation Expenses: ")
mark = input("\nEnter Marketing Expenses: ")
memb = input("\nEnter Memberships Expenses: ")
ps = input("\nEnter Professional Services Expenses: ")

# Create a general list of values to be replaced by actual numbers input by the user.
values = [pay, rent, util, tax, insur, os, trans, mark, memb, ps]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.show()
