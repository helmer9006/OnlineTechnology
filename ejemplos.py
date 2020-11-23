lista =[
    [{'codigo': 'cam1', 'cantidad': 2, 'valorUnitario': 80000, 'valorUnitarioC': 50000, 'valorTotal': 160000}, 
     {'codigo': 'cam2', 'cantidad': 1, 'valorUnitario': 85000, 'valorUnitarioC': 55000, 'valorTotal': 85000}], 
    [{'codigo': 'cam3', 'cantidad': 1, 'valorUnitario': 90000, 'valorUnitarioC': 60000, 'valorTotal': 90000}]
]

vbalance = 0
cbalance = 0
for elem in lista: 
    for k in elem:
       vbalance = vbalance + (k.get('cantidad') * k.get('valorUnitario'))
       cbalance = cbalance + (k.get('cantidad') * k.get('valorUnitarioC'))
tbalance = vbalance - cbalance
print (tbalance)