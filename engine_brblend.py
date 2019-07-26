import pyodbc
import csv

def cnpj_for(codi_emp, nome_for):
    connection = pyodbc.connect("DSN=soma")
    cursor = connection.cursor()
    cursor.execute(f"SELECT MAX(cgce_for) "
                   f"  FROM bethadba.effornece "
                   f" WHERE codi_emp = {codi_emp} "
                   f"   AND nome_for LIKE '%{nome_for}%'"
                   f"")
    data = cursor.fetchone()
    cursor.close()
    connection.close()

    return data

entrada = 'temp\\pagtos_agrupados.csv'
saida = open('saida\\pagtos_agrupados.csv', 'w')
with open(entrada, 'rt') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        if str(row[10]) == 'Nome Fornecedor':
            continue
        else:
            _codi_emp = int(row[12])

            _nome_for = str(row[10]).replace('  ', ' ')
            _nome_for_ori = _nome_for
			_nome_for = _nome_for[0:21]

            _cnpj_for = str(cnpj_for(_codi_emp, _nome_for))
            _cnpj_for = _cnpj_for.replace(' ', '').replace('(', '').replace(')', '').replace(',', '').replace('None', "'")

            result = (f"{row[0]};{_cnpj_for};{row[2]};{row[3]};{row[4]};{row[5]};{row[6]};{row[7]};{row[8]}"
                      f";{row[9]};{_nome_for_ori};{row[11]};{row[12]}\n")
        saida.write(result)

saida.close()