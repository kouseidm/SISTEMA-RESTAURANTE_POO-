bebidas = {
        1: ["Chicha morada", 18.00],
        "2. Chicha de jora": 18.00,
        "3. CocaCola": 10.00,
        "4. InkaCola": 10.00,
        "5. Jugo natural": 10.00,
        "6. Cafe": 6.00,
        "7. Pisco Sour": 20.00,
        "8. Chilcano de pisco": 18.00   
    }

pedidos = []

opcion = int(input("Igresar la opcion: "))
if 1<= opcion <= 10:
    pedido = bebidas[opcion]
    print (pedido)
    
    