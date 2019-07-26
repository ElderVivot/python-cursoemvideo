import pyodbc

cnxn = pyodbc.connect("DSN=soma")
cursor = cnxn.cursor()
cursor.execute("SELECT codi_for, nome_for, cgce_for, codi_cta FROM bethadba.effornece WHERE codi_emp = 81")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()