import qrcode
from qrcode.constants import ERROR_CORRECT_L

def gerar_qrcode(input_infos,name_doc,qr_length):
    qr_length = int(qr_length)
    if qr_length is None or qr_length < 5:
        borda = 5
    else:
        borda = qr_length
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=borda,
    )
    qr.add_data(input_infos)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(name_doc)
    print(f"O QR Code de {name_doc} foi salvo na pasta local.")

def gerar_qr_wifi(ssid,password,security):
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"
    qr.add_data(wifi_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"Wi-Fi {ssid}.png")
    print(f"O QR Code do wi-fi {ssid} foi salvo na pasta local.")

def gerar_qr_contato(name,number,email):
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    contact_info = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{number}\nEMAIL:{email}\nEND:VCARD"
    qr.add_data(contact_info)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"QR Code do contato {name}.png")
    print(f"O QR Code do contato {name} foi salvo na pasta local.")

while True:
    print("\n#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+# GERADOR DE QR CODES #+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#")
    infos = input("O que deseja gerar em QR Code? Wi-Fi ou Contato, para outros como links, mensagens etc, basta colar aqui.\nR.: ")
    try:
        if infos in ['wifi','wi-fi','WiFi','Wi-Fi','WIFI']:
            ssid_name = input("Nome da rede Wi-Fi: ")
            pass_wifi = input("Senha da rede Wi-Fi: ")
            sec_factor = input("Módulo de proteção (WEP, WPA, WPA2, WPA2-AES, WPA2-TKIP): ")
            gerar_qr_wifi(ssid_name, pass_wifi, sec_factor)

        elif infos in ['contato','Contato']:
            contact_name = input("Nome do contato: ")
            contact_number = input("Número do contato: ")
            contact_email = input("E-mail do contato: ")
            gerar_qr_contato(contact_name,contact_number,contact_email)

        else:
            nome_qr = input("Qual nome gostaria de salvar a imagem?\nR.: ") + ".png"
            tamanho_qr = input("Qual tamanho gostaria para o QR? (Mínimo 5)\nR.: ")
            gerar_qrcode(infos, nome_qr, tamanho_qr)

    except Exception as erro:
        print(f"Ocorreu um erro. {erro}")

    continuar = input("Desejar continuar usando a aplicação? (s/n) \nR.: ")
    if continuar not in ['s','sim']:
        print("Obrigado por utilizar a aplicação!")
        break