weather=(1,0,0,0,1,1,0)
sunny=0
rainy=0
for i in weather:
    if weather[i]==0:
        sunny=sunny+1
    else:
        rainy=rainy+1
if (sunny > rainy):
    print("good weather")
else:
    print("bad weather")
