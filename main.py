wifi_connect()

while(1):
    v_dust = read_dust_volt()
    if v_dust >= v_no_dust:
        dust = ((v_dust - v_no_dust)/v_sens) * 100
    else:
        dust = 0

    print("Dust :", dust, "ug/mmm")
    publish_data("dust", dust)
    delay(60)