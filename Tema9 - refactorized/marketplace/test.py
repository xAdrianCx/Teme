

lst = {"43fe15f506025c15bf4480781e2fc888": {
      "id_comanda": "43fe15f506025c15bf4480781e2fc888",
      "detalii_comanda": [
        {
          "sare": 1
        },
        {
          "piper": 3
        },
        {
          "nuci": 5
        }
      ],
      "data_inregistrare": "2022-04-08T20:17:59.171097+03:00"
    }
  }

lst2 = ""
for i in range(len(lst["43fe15f506025c15bf4480781e2fc888"]["detalii_comanda"])):
	for j in lst["43fe15f506025c15bf4480781e2fc888"]["detalii_comanda"][i].keys():
		if j == 'piper':
			lst2 = i
del lst["43fe15f506025c15bf4480781e2fc888"]["detalii_comanda"][lst2]
lst2 = int(lst2)
print(lst2)
print(lst)

	
				   