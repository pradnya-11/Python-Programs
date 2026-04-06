
#item price is 50, quantity is 40, calculate bill amount its having offer of 10% discount #

ip=50
qty=40
ta= ip*qty
td= ta*10/100
ba= ta-td

print("Item Price=", ip)
print("Quantity", qty)
print("Total Amount=", ta)
print("Total Discount=",td)
print("Bill Amount=", ba)
