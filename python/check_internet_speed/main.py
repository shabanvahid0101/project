import speedtest as st

def speed_test():
    test=st.Speedtest()
    down_speed=test.download()
    down_speed=round(down_speed/10**6,2)
    print(f"download speed is :{down_speed} mb")
    
    up_speed=test.upload()
    up_speed=round(up_speed/10**6,2)
    print(f"uploud speed is :{up_speed} mb")
    
    ping=test.results.ping
    print(f"ping is :{ping} mls")

    
speed_test()