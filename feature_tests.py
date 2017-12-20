x_avg = np.mean(x,axis=0).astype(int)
geoTest =[]
for i in geoIndex:
    geoTest.append(np.append([i],x_avg[1:]))
geoTest = np.array(geoTest)
geoY = nnModel.predict(geoTest)
geoY


mrTest =[]
for i in migrantIndex:
    mrTest.append(np.append(x_avg[:1],np.append([i],x_avg[2:])))
mrTest = np.array(mrTest)
mrY = nnModel.predict(mrTest)
mrY

regionTest =[]
for i in regionIndex:
    regionTest.append(np.append(x_avg[:2],np.append([i],x_avg[3:])))
regionTest = np.array(regionTest)
regionY = nnModel.predict(regionTest)
regionY


percentFemaleTest = []
for i in range(100):
    percentFemaleTest.append(np.append(x_avg[:3],np.append([i],x_avg[4:])))
percentFemaleTest = np.array(percentFemaleTest)
percentFemaleY = nnModel.predict(percentFemaleTest)
percentFemaleY

percentChildrenTest = []

for i in range(100):
    percentChildrenTest.append(np.append(x_avg[:5],np.append([i],x_avg[6:])))
percentChildrenTest = np.array(percentChildrenTest)
percentChildrenY = nnModel.predict(percentChildrenTest)
percentChildrenY

monthTest = []

for i in range(12):
    monthTest.append(np.append(x_avg[:6],np.append([i],x_avg[7:])))
monthTest = np.array(monthTest)
monthY = nnModel.predict(monthTest)
monthY

percentMaleTest = []

for i in range(100):
    percentMaleTest.append(np.append(x_avg[:5],np.append([i],x_avg[6:])))
percentMaleTest = np.array(percentMaleTest)
percentMaleY = nnModel.predict(percentMaleTest)
percentMaleY
