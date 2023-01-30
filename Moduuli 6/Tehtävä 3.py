def gallonat_litroiksi(gallonat):
    return gallonat * 3.785
while True:
    gallonat = float(input("Syötä bensiinin määrä gallonoina"))
    if gallonat < 0:
        break
    litrat = gallonat_litroiksi(gallonat)
    print(f"{gallonat} galloona on {litrat} litraa")
