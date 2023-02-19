import re

""" comprueba que la ip este dada en formato x.x.x.x y que los octetos vayan de 0 - 255 """
def verifyIp(ip):
    """ verificacion de la ip """
    if re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", ip):  # verifica el formato correcto de la ip
        if not len([True for x in ip.split(".") if int(x) <= 255 and int(x) >= 0]) == 4:  # comprueba que los octetos esten entre 0 y 255
            print(f"\033[31;1m{ip}\033[0m es una dirección no válida, los octetos deben estar entre 0 y 255, con formato 10.10.4.5")
            return False

    else:
        print(f"\033[31;1m{ip}\033[0m es una dirección no válida, los octetos deben estar entre 0 y 255, con formato 10.10.4.5")
        return False

    return True

""" calcula los bits necesarios para las subredes/hosts que se requieren """
def necessaryBits(required):
    bits = 0
    for i in range(32):
        x = 2 ** i - 2
        if x >= required:
            bits = i
            break

    return bits

""" calcula la nueva mascara de red """
def getMask(mask, bits, mode="net"):
    octets = mask.split(".")
    n_mask = []

    for o in octets:
        if int(o) == 0:  # genera el nuevo octeto en el primer oct que sea 0
            n_oct = "1" * bits + "0" * (8 - bits)
            n_mask.append(str(int(n_oct, 2)))
            break

        else:
            n_mask.append(o)

    while(len(n_mask) < 4):  # completa el octeto
        n_mask.append(str(int("0" * 8, 2)))

    return ".".join(n_mask)

def main():
    """
    ip_base = input("IP base (ej. 200.35.2.0): ")
    mask = input("Mascara (ej. 255.255.255.254): ")
    subnets = input("Cuántas subredes necesitas? (n, para no calcular): ")
    hosts = input("Cuántos hosts necesitas? (n, para no calcular): ")
    """
    ip_base = "200.35.2.0"
    mask = "255.255.255.0"
    subnets = "6"
    hosts = "20"

    s_bits = h_bits = None

    if verifyIp(ip_base) and verifyIp(mask):
        if subnets != "n":
            try:
                s_bits = necessaryBits(int(subnets))
                print(f"subnet bits: {s_bits}")
                n_mask = getMask(mask, s_bits) 
                print(f"new mask: {n_mask}")
            except:
                print(f"\033[31;1m'{subnets}' no válido\033[0m, ingresa un números enteros en subnets y hosts")

        if hosts != "n":
            try:
                h_bits = necessaryBits(int(hosts))
                print(f"host bits: {h_bits}")
            except:
                print(f"\033[31;1m'{hosts}' no válido\033[0m, ingresa un números enteros en subnets y hosts")
    
    

if __name__ == "__main__":
    main()
