
def WCI(T, V):

    return 13.12 + 0.6215*T - 11.37*pow(V, 0.16) + 0.3965*T*pow(V, 0.16)

T, V = input("Enter temperature and wind speed: ").split()

print(WCI(int(T), int(V)))