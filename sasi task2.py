def will-climbing(signal):
    current=0
    while current<len (signal)-1:
        if signal [current+1]>signal[current]:
            current+=1
            else:
                break
            return current,signal[current]
        signal=[30,45,35,70,68,60]
        index,strength=hill-climbing(signal)
        print("best tower index:",index)
        print("strongest signal:",strength)
        
