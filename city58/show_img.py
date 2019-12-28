import matplotlib.pyplot as plt
import re

str = """"

        <pt x="731" y="1392" on="1"/>
        <pt x="1030" y="1392" on="1"/>
        <pt x="1079" y="1532" on="0"/>
        <pt x="1125" y="1678" on="1"/>
        <pt x="1277" y="1636" on="1"/>
        <pt x="1233" y="1511" on="0"/>
        <pt x="1190" y="1392" on="1"/>
        <pt x="1955" y="1392" on="1"/>
        <pt x="1961" y="1278" on="1"/>
        <pt x="1955" y="1250" on="1"/>
        <pt x="1138" y="1250" on="1"/>
        <pt x="1047" y="1001" on="0"/>
        <pt x="959" y="776" on="1"/>
        <pt x="1291" y="776" on="1"/>
        <pt x="1297" y="797" on="0"/>
        <pt x="1294" y="789" on="1"/>
        <pt x="1291" y="1120" on="1"/>
        <pt x="1337" y="1122" on="0"/>
        <pt x="1337" y="1123" on="1"/>
        <pt x="1443" y="1120" on="1"/>
        <pt x="1447" y="966" on="1"/>
        <pt x="1443" y="776" on="1"/>
        <pt x="1496" y="778" on="1"/>
        <pt x="1941" y="776" on="1"/>
        <pt x="1944" y="704" on="1"/>
        <pt x="1941" y="632" on="1"/>
        <pt x="1577" y="638" on="1"/>
        <pt x="1443" y="632" on="1"/>
        <pt x="1443" y="-14" on="1"/>
        <pt x="1443" y="-248" on="0"/>
        <pt x="1207" y="-248" on="1"/>
        <pt x="1073" y="-248" on="0"/>
        <pt x="951" y="-246" on="1"/>
        <pt x="939" y="-164" on="0"/>
        <pt x="921" y="-80" on="1"/>
        <pt x="1061" y="-96" on="0"/>
        <pt x="1165" y="-96" on="1"/>
        <pt x="1291" y="-96" on="0"/>
        <pt x="1291" y="30" on="1"/>
        <pt x="1291" y="632" on="1"/>
        <pt x="1200" y="638" on="1"/>
        <pt x="785" y="632" on="1"/>
        <pt x="787" y="724" on="0"/>
        <pt x="789" y="698" on="1"/>
        <pt x="785" y="778" on="1"/>
        <pt x="888" y="1004" on="0"/>
        <pt x="979" y="1250" on="1"/>
        <pt x="731" y="1250" on="1"/>
        <pt x="737" y="1317" on="0"/>
        <pt x="736" y="1376" on="1"/>
      </contour>
      <contour>
        <pt x="685" y="454" on="1"/>
        <pt x="743" y="102" on="0"/>
        <pt x="497" y="56" on="1"/>
        <pt x="419" y="42" on="0"/>
        <pt x="295" y="54" on="1"/>
        <pt x="279" y="136" on="0"/>
        <pt x="251" y="222" on="1"/>
        <pt x="349" y="198" on="0"/>
        <pt x="435" y="206" on="1"/>
        <pt x="573" y="218" on="0"/>
        <pt x="525" y="460" on="1"/>
        <pt x="497" y="622" on="0"/>
        <pt x="345" y="820" on="1"/>
        <pt x="435" y="1116" on="0"/>
        <pt x="509" y="1402" on="1"/>
        <pt x="249" y="1402" on="1"/>
        <pt x="249" y="-276" on="1"/>
        <pt x="99" y="-276" on="1"/>
        <pt x="99" y="1542" on="1"/>
        <pt x="366" y="1545" on="1"/>
        <pt x="675" y="1542" on="1"/>
        <pt x="675" y="1402" on="1"/>
        <pt x="539" y="954" on="0"/>
        <pt x="503" y="846" on="1"/>
        <pt x="667" y="630" on="0"/>
      </contour>
      <contour>
        <pt x="1563" y="384" on="1"/>
        <pt x="1689" y="478" on="1"/>
        <pt x="1877" y="222" on="0"/>
        <pt x="1995" y="24" on="1"/>
        <pt x="1865" y="-64" on="1"/>
        <pt x="1693" y="226" on="0"/>
      </contour>
      <contour>
        <pt x="987" y="462" on="1"/>
        <pt x="1117" y="382" on="1"/>
        <pt x="949" y="134" on="0"/>
        <pt x="797" y="-58" on="1"/>
        <pt x="663" y="32" on="1"/>
        <pt x="829" y="216" on="0"/>
"""
str2 = '''
<contour>
        <pt x="720" y="1381" on="1"/>
        <pt x="1019" y="1381" on="1"/>
        <pt x="1068" y="1521" on="0"/>
        <pt x="1114" y="1667" on="1"/>
        <pt x="1266" y="1625" on="1"/>
        <pt x="1222" y="1500" on="0"/>
        <pt x="1179" y="1381" on="1"/>
        <pt x="1944" y="1381" on="1"/>
        <pt x="1949" y="1379" on="1"/>
        <pt x="1944" y="1239" on="1"/>
        <pt x="1686" y="1244" on="0"/>
        <pt x="1846" y="1242" on="1"/>
        <pt x="1127" y="1239" on="1"/>
        <pt x="1036" y="990" on="0"/>
        <pt x="948" y="765" on="1"/>
        <pt x="1280" y="765" on="1"/>
        <pt x="1280" y="1109" on="1"/>
        <pt x="1349" y="1114" on="1"/>
        <pt x="1432" y="1109" on="1"/>
        <pt x="1434" y="845" on="1"/>
        <pt x="1432" y="765" on="1"/>
        <pt x="1505" y="770" on="0"/>
        <pt x="1762" y="769" on="1"/>
        <pt x="1930" y="765" on="1"/>
        <pt x="1930" y="621" on="1"/>
        <pt x="1432" y="621" on="1"/>
        <pt x="1436" y="490" on="1"/>
        <pt x="1432" y="-25" on="1"/>
        <pt x="1432" y="-259" on="0"/>
        <pt x="1196" y="-259" on="1"/>
        <pt x="1062" y="-259" on="0"/>
        <pt x="940" y="-257" on="1"/>
        <pt x="928" y="-175" on="0"/>
        <pt x="910" y="-91" on="1"/>
        <pt x="1050" y="-107" on="0"/>
        <pt x="1154" y="-107" on="1"/>
        <pt x="1280" y="-107" on="0"/>
        <pt x="1280" y="19" on="1"/>
        <pt x="1280" y="621" on="1"/>
        <pt x="774" y="621" on="1"/>
        <pt x="779" y="736" on="0"/>
        <pt x="778" y="744" on="1"/>
        <pt x="774" y="767" on="1"/>
        <pt x="877" y="993" on="0"/>
        <pt x="968" y="1239" on="1"/>
        <pt x="720" y="1239" on="1"/>
        <pt x="722" y="1364" on="0"/>
        <pt x="723" y="1381" on="1"/>
      </contour>
      <contour>
        <pt x="674" y="443" on="1"/>
        <pt x="732" y="91" on="0"/>
        <pt x="486" y="45" on="1"/>
        <pt x="408" y="31" on="0"/>
        <pt x="284" y="43" on="1"/>
        <pt x="268" y="125" on="0"/>
        <pt x="240" y="211" on="1"/>
        <pt x="338" y="187" on="0"/>
        <pt x="424" y="195" on="1"/>
        <pt x="562" y="207" on="0"/>
        <pt x="514" y="449" on="1"/>
        <pt x="486" y="611" on="0"/>
        <pt x="334" y="809" on="1"/>
        <pt x="424" y="1105" on="0"/>
        <pt x="498" y="1391" on="1"/>
        <pt x="238" y="1391" on="1"/>
        <pt x="242" y="379" on="1"/>
        <pt x="238" y="-287" on="1"/>
        <pt x="185" y="-283" on="1"/>
        <pt x="88" y="-287" on="1"/>
        <pt x="90" y="920" on="0"/>
        <pt x="90" y="713" on="1"/>
        <pt x="88" y="1531" on="1"/>
        <pt x="585" y="1534" on="1"/>
        <pt x="664" y="1531" on="1"/>
        <pt x="664" y="1391" on="1"/>
        <pt x="528" y="943" on="0"/>
        <pt x="492" y="835" on="1"/>
        <pt x="656" y="619" on="0"/>
      </contour>
      <contour>
        <pt x="1552" y="373" on="1"/>
        <pt x="1678" y="467" on="1"/>
        <pt x="1866" y="211" on="0"/>
        <pt x="1984" y="13" on="1"/>
        <pt x="1854" y="-75" on="1"/>
        <pt x="1682" y="215" on="0"/>
      </contour>
      <contour>
        <pt x="976" y="451" on="1"/>
        <pt x="1106" y="371" on="1"/>
        <pt x="938" y="123" on="0"/>
        <pt x="786" y="-69" on="1"/>
        <pt x="652" y="21" on="1"/>
        <pt x="818" y="205" on="0"/>
      </contour>
'''

x = [int(i) for i in re.findall(r'<pt x="(.*?)" y=', str2)]
y = [int(i) for i in re.findall(r'y="(.*?)" on=', str2)]
print(x)
print(y)
plt.plot(x, y)
plt.fill(x, y, 'black')
# plt.fill(x_n, y, 'black')
plt.show()