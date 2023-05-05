#from micropython import const

adc_lut = [0, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 129, 129, 129, 130, 131, 132, 132, 133, 134, 134, 134, 137, 139, 140, 142, 143, 144, 144, 144, 147, 146, 147, 151, 150, 153, 145, 152, 153, 158, 157, 160, 159, 158, 161, 164, 163, 164, 165, 164, 169, 162, 168, 173, 170, 165, 172, 167, 178, 172, 166, 178, 173, 185, 186, 187, 185, 173, 187, 183, 189, 186, 191, 197, 193, 190, 195, 201, 188, 203, 205, 206, 207, 202, 203, 198, 200, 200, 201, 202, 209, 210, 212, 220, 221, 216, 217, 218, 219, 220, 214, 222, 223, 224, 225, 220, 235, 229, 238, 239, 240, 218, 234, 227, 236, 229, 230, 230, 231, 248, 233, 234, 226, 243, 228, 229, 255, 230, 249, 250, 250, 243, 234, 244, 255, 265, 257, 268, 231, 241, 262, 263, 254, 255, 266, 277, 278, 269, 270, 271, 262, 284, 264, 254, 276, 277, 267, 279, 280, 281, 283, 284, 296, 297, 277, 289, 267, 280, 280, 293, 306, 307, 296, 285, 310, 275, 287, 276, 302, 303, 279, 304, 318, 306, 308, 282, 309, 311, 298, 299, 314, 315, 303, 304, 332, 333, 320, 321, 323, 324, 325, 340, 326, 328, 343, 330, 331, 332, 348, 334, 335, 336, 323, 339, 325, 341, 342, 328, 329, 346, 346, 364, 349, 366, 367, 368, 337, 354, 371, 356, 373, 374, 375, 360, 377, 345, 363, 364, 381, 348, 384, 367, 368, 352, 388, 372, 391, 375, 394, 378, 379, 380, 363, 400, 383, 402, 385, 386, 406, 389, 409, 391, 411, 393, 413, 395, 415, 416, 379, 418, 381, 402, 402, 403, 405, 406, 407, 348, 409, 369, 411, 411, 433, 413, 435, 395, 437, 438, 439, 419, 421, 422, 423, 444, 382, 447, 427, 406, 429, 451, 431, 431, 411, 411, 456, 413, 458, 437, 394, 439, 395, 440, 419, 442, 443, 445, 423, 448, 449, 473, 451, 476, 477, 479, 480, 458, 482, 460, 461, 462, 487, 416, 489, 491, 492, 469, 494, 422, 496, 473, 449, 450, 501, 427, 503, 479, 505, 506, 482, 508, 459, 511, 460, 513, 488, 515, 490, 491, 518, 519, 520, 495, 522, 523, 498, 526, 527, 502, 503, 530, 505, 533, 534, 508, 536, 510, 511, 540, 541, 542, 543, 516, 546, 547, 548, 550, 522, 496, 553, 554, 555, 528, 529, 502, 531, 532, 533, 534, 535, 537, 480, 539, 511, 541, 542, 543, 544, 574, 516, 577, 548, 579, 580, 581, 583, 584, 585, 586, 557, 589, 590, 591, 592, 593, 595, 596, 566, 567, 599, 538, 570, 571, 572, 605, 542, 607, 576, 545, 546, 516, 548, 581, 582, 550, 584, 585, 586, 619, 620, 556, 622, 623, 591, 625, 592, 626, 594, 595, 596, 630, 597, 632, 533, 633, 534, 635, 535, 637, 604, 638, 571, 640, 607, 642, 609, 611, 646, 578, 614, 615, 650, 582, 653, 584, 620, 621, 587, 658, 624, 660, 626, 627, 628, 665, 666, 632, 597, 634, 671, 672, 637, 674, 639, 640, 641, 679, 606, 681, 645, 683, 685, 686, 687, 688, 689, 690, 691, 692, 656, 620, 696, 660, 699, 662, 626, 664, 703, 704, 667, 707, 632, 709, 634, 712, 637, 715, 677, 717, 679, 719, 603, 682, 643, 723, 724, 646, 687, 688, 689, 651, 651, 692, 733, 734, 695, 656, 697, 698, 739, 741, 742, 702, 703, 704, 705, 706, 748, 708, 710, 751, 711, 712, 754, 756, 716, 716, 759, 760, 720, 762, 764, 765, 766, 725, 768, 769, 686, 686, 687, 688, 732, 775, 776, 735, 779, 780, 781, 739, 740, 741, 699, 786, 700, 745, 746, 748, 705, 794, 707, 752, 753, 798, 711, 800, 801, 757, 758, 804, 760, 761, 762, 808, 764, 765, 767, 813, 814, 725, 726, 817, 819, 820, 775, 822, 824, 779, 826, 735, 828, 830, 831, 786, 740, 834, 788, 836, 837, 745, 793, 794, 842, 843, 844, 750, 846, 847, 848, 801, 850, 803, 804, 854, 855, 856, 857, 810, 762, 860, 861, 766, 766, 865, 721, 867, 868, 869, 822, 823, 872, 824, 875, 827, 878, 780, 880, 881, 882, 883, 884, 835, 787, 837, 839, 840, 891, 842, 893, 894, 794, 896, 898, 899, 849, 901, 852, 904, 803, 907, 805, 909, 807, 911, 860, 861, 862, 863, 916, 917, 762, 919, 920, 921, 870, 923, 872, 873, 874, 927, 928, 929, 878, 931, 827, 934, 882, 883, 884, 939, 833, 888, 889, 944, 945, 892, 947, 948, 949, 842, 951, 952, 953, 954, 901, 956, 957, 795, 959, 905, 962, 963, 909, 910, 801, 968, 859, 970, 971, 972, 974, 975, 920, 921, 922, 923, 812, 982, 870, 984, 985, 986, 931, 988, 989, 820, 991, 878, 936, 994, 995, 996, 997, 941, 1000, 887, 1004, 949, 949, 950, 895, 1011, 897, 1016, 902, 1020, 1021, 1023, 1025, 967, 969, 1030, 912, 914, 915, 976, 1036, 978, 979, 1040, 1041, 1042, 1042, 923, 984, 925, 866, 988, 868, 990, 991, 1052, 931, 1054, 872, 995, 996, 1058, 1059, 999, 1000, 1062, 1064, 1065, 1005, 1067, 946, 1070, 1071, 1072, 1011, 1074, 1013, 1076, 1077, 1078, 1017, 1018, 1081, 1082, 958, 1084, 1085, 1023, 961, 899, 1026, 1090, 1028, 1092, 1094, 1095, 1096, 1034, 1099, 1037, 1101, 1039, 1040, 977, 1106, 1042, 1108, 1045, 981, 1111, 983, 1049, 1115, 1116, 1052, 1118, 989, 1055, 1121, 1057, 1059, 1059, 1126, 1127, 1128, 1129, 1130, 1131, 1066, 1133, 1068, 1069, 1136, 1137, 1006, 1074, 1009, 1143, 1144, 1145, 1079, 1147, 1148, 1150, 1151, 1085, 1153, 1086, 1155, 1156, 1158, 1159, 1160, 1161, 960, 1164, 1165, 1166, 1167, 1032, 1169, 1102, 1171, 1035, 1036, 1105, 1106, 1175, 1176, 1178, 1110, 1180, 1112, 1182, 1183, 1115, 1184, 1185, 1117, 1187, 1188, 1120, 982, 1122, 1123, 1194, 1196, 1127, 1198, 1199, 1130, 1201, 1131, 1202, 1133, 1134, 1134, 1136, 1207, 1208, 1138, 1068, 1069, 1140, 1141, 1213, 1214, 1215, 1002, 1217, 1074, 1147, 1220, 1221, 1150, 1151, 1152, 1225, 1227, 1228, 1229, 1231, 1087, 1233, 1234, 1235, 1236, 1237, 1238, 1094, 1168, 1169, 1243, 1171, 1245, 1099, 1174, 1101, 1175, 1250, 1251, 1252, 1253, 1180, 1255, 1182, 1183, 1183, 1258, 1185, 1038, 1113, 1114, 1263, 1264, 1191, 1192, 1192, 1119, 1270, 1197, 1198, 1274, 1276, 1127, 1279, 1204, 1205, 1282, 1283, 1284, 1285, 1287, 1288, 1290, 1215, 1216, 1294, 1218, 1220, 1297, 1221, 1222, 1300, 1224, 1148, 1226, 1304, 1228, 1306, 1307, 1308, 1154, 1310, 1233, 1234, 1157, 1314, 1159, 1316, 1316, 1318, 1319, 1242, 1321, 1088, 1323, 1325, 1326, 1248, 1328, 1329, 1330, 1252, 1332, 1255, 1255, 1257, 1336, 1338, 1260, 1340, 1262, 1263, 1264, 1265, 1267, 1268, 1349, 1190, 1271, 1272, 1192, 1355, 1356, 1357, 1358, 1279, 1279, 1281, 1362, 1363, 1364, 1284, 1204, 1367, 1124, 1370, 1289, 1290, 1373, 1374, 1375, 1295, 1296, 1133, 1380, 1381, 1300, 1383, 1302, 1385, 1386, 1305, 1306, 1141, 1390, 1226, 1392, 1228, 1312, 1395, 1313, 1398, 1232, 1400, 1235, 1319, 1404, 1321, 1406, 1324, 1324, 1409, 1326, 1411, 1328, 1414, 1331, 1416, 1333, 1165, 1420, 1337, 1338, 1254, 1340, 1341, 1427, 1172, 1258, 1345, 1431, 1432, 1434, 1435, 1265, 1437, 1353, 1439, 1355, 1441, 1356, 1357, 1444, 1359, 1360, 1361, 1449, 1363, 1364, 1452, 1280, 1367, 1455, 1369, 1457, 1371, 1459, 1461, 1462, 1463, 1464, 1378, 1291, 1467, 1381, 1382, 1471, 1472, 1473, 1386, 1475, 1212, 1477, 1479, 1391, 1393, 1306, 1484, 1307, 1486, 1398, 1488, 1489, 1490, 1491, 1402, 1493, 1494, 1495, 1406, 1407, 1319, 1319, 1500, 1501, 1502, 1233, 1324, 1415, 1506, 1416, 1237, 1419, 1511, 1512, 1513, 1334, 1516, 1517, 1518, 1428, 1429, 1521, 1431, 1523, 1433, 1342, 1526, 1345, 1437, 1438, 1439, 1532, 1349, 1534, 1535, 1444, 1537, 1538, 1540, 1541, 1450, 1544, 1545, 1361, 1548, 1364, 1550, 1551, 1367, 1553, 1461, 1555, 1463, 1277, 1464, 1466, 1466, 1468, 1469, 1564, 1376, 1566, 1567, 1473, 1568, 1570, 1571, 1572, 1479, 1574, 1575, 1577, 1578, 1484, 1580, 1581, 1487, 1489, 1394, 1586, 1587, 1493, 1494, 1591, 1592, 1497, 1594, 1595, 1501, 1597, 1502, 1599, 1504, 1505, 1602, 1603, 1604, 1509, 1607, 1511, 1512, 1513, 1514, 1612, 1516, 1420, 1518, 1422, 1618, 1619, 1328, 1621, 1622, 1624, 1625, 1528, 1628, 1629, 1532, 1631, 1632, 1535, 1536, 1635, 1636, 1637, 1639, 1541, 1641, 1642, 1346, 1347, 1645, 1448, 1647, 1350, 1649, 1650, 1552, 1652, 1654, 1655, 1656, 1657, 1558, 1660, 1361, 1662, 1663, 1664, 1564, 1465, 1567, 1367, 1670, 1671, 1470, 1572, 1371, 1676, 1575, 1576, 1679, 1680, 1681, 1682, 1581, 1684, 1685, 1686, 1585, 1586, 1689, 1690, 1589, 1693, 1489, 1592, 1593, 1492, 1595, 1596, 1700, 1701, 1497, 1704, 1499, 1706, 1605, 1709, 1710, 1608, 1712, 1713, 1714, 1715, 1716, 1510, 1719, 1616, 1721, 1619, 1619, 1621, 1517, 1727, 1728, 1625, 1626, 1627, 1523, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1742, 1637, 1638, 1744, 1746, 1747, 1642, 1749, 1644, 1751, 1646, 1753, 1648, 1649, 1649, 1650, 1651, 1759, 1653, 1760, 1654, 1762, 1763, 1764, 1658, 1765, 1659, 1554, 1768, 1555, 1662, 1556, 1665, 1558, 1773, 1559, 1560, 1561, 1454, 1671, 1780, 1673, 1782, 1675, 1784, 1785, 1786, 1788, 1789, 1790, 1791, 1685, 1685, 1796, 1797, 1798, 1689, 1691, 1692, 1692, 1803, 1475, 1805, 1696, 1807, 1698, 1699, 1700, 1591, 1482, 1813, 1814, 1705, 1706, 1707, 1819, 1820, 1821, 1712, 1602, 1824, 1715, 1827, 1717, 1718, 1719, 1831, 1721, 1834, 1724, 1724, 1613, 1838, 1839, 1504, 1841, 1842, 1843, 1731, 1844, 1846, 1847, 1736, 1624, 1850, 1740, 1741, 1855, 1630, 1744, 1858, 1746, 1860, 1748, 1863, 1864, 1752, 1866, 1754, 1869, 1756, 1871, 1872, 1759, 1874, 1875, 1876, 1877, 1764, 1879, 1880, 1767, 1768, 1654, 1884, 1770, 1657, 1887, 1773, 1889, 1776, 1777, 1893, 1894, 1896, 1897, 1898, 1784, 1901, 1902, 1903, 1789, 1673, 1791, 1792, 1909, 1678, 1911, 1796, 1797, 1915, 1448, 1917, 1918, 1919, 1920, 1569, 1922, 1923, 1924, 1925, 1809, 1810, 1929, 1930, 1931, 1814, 1816, 1817, 1936, 1937, 1819, 1939, 1940, 1941, 1705, 1706, 1826, 1834, 1947, 1949, 1831, 1951, 1594, 1953, 1955, 1836, 1956, 1838, 1960, 1961, 1842, 1963, 1844, 1965, 1846, 1967, 1728, 1848, 1970, 1971, 1972, 1852, 1853, 1975, 1976, 1857, 1978, 1979, 1860, 1982, 1861, 1863, 1985, 1986, 1866, 1866, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1631, 1998, 1877, 2000, 1878, 2002, 2003, 2004, 2005, 1884, 2008, 1886, 2011, 1889, 1890, 1891, 2015, 1893, 2017, 1895, 2019, 2020, 1774, 2022, 2023, 1901, 2026, 1903, 2028, 1781, 1906, 2031, 1783, 1908, 2033, 1909, 1661, 1661, 1662, 1537, 1911, 1787, 1788, 1913, 2038, 2038, 1914, 2039, 1915, 1915, 1916, 2041, 2041, 2042, 1793, 1668, 1793, 2044, 1669, 1795, 1795, 1795, 2046, 1546, 1671, 2047, 1672, 1798, 1924, 1799, 2051, 2052, 1928, 2055, 2056, 1805, 1932, 2059, 2060, 1936, 2063, 2064, 1812, 1940, 2067, 1815, 1943, 2071, 2072, 2073, 1947, 1821, 2076, 1823, 2078, 2079, 1570, 2081, 2082, 1955, 2084, 2085, 2087, 1960, 2089, 2091, 2092, 2093, 2094, 2095, 1968, 2097, 1841, 1970, 2100, 1844, 1973, 1845, 1717, 2105, 1848, 2107, 2108, 1721, 2110, 2111, 2112, 2113, 2114, 2115, 2117, 1988, 2119, 2121, 1992, 2123, 2125, 1995, 2127, 1998, 1868, 2130, 1869, 2132, 2133, 2003, 2004, 2136, 2007, 2008, 2009, 2141, 2011, 2144, 2145, 2146, 2147, 2148, 2018, 2151, 2020, 2154, 2155, 2156, 2158, 2159, 2027, 2029, 2029, 2163, 2164, 2165, 1900, 2167, 1902, 1770, 2037, 2038, 1906, 2040, 2175, 2176, 2043, 2178, 2179, 2047, 2182, 2183, 2184, 2185, 1918, 2053, 2189, 2055, 2191, 2192, 2059, 1925, 2060, 2196, 1928, 2063, 1929, 2066, 2202, 2203, 2204, 2205, 2070, 1936, 2208, 2074, 2211, 2212, 2213, 2214, 2215, 1944, 1945, 2218, 2219, 1948, 1948, 2223, 2087, 2088, 2226, 2090, 2228, 2229, 1956, 2095, 2233, 2235, 2236, 2237, 2100, 2101, 2240, 2241, 2242, 2243, 2244, 2245, 2108, 1972, 1973, 2250, 2112, 2251, 2253, 2115, 2116, 2256, 2118, 2119, 2259, 2121, 2261, 2262, 2264, 2265, 2266, 2268, 2269, 2270, 2131, 2272, 2273, 2274, 2275, 2276, 2278, 2138, 2280, 2140, 2141, 2283, 2144, 2144, 2286, 2147, 2007, 2289, 2290, 2292, 2293, 2011, 2295, 2296, 2298, 2299, 2159, 2018, 2160, 2303, 2304, 2305, 2306, 2165, 1882, 2167, 2167, 2026, 2169, 2170, 2171, 2172, 2316, 2031, 2317, 2318, 2176, 2320, 2178, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2186, 2330, 2188, 2189, 2190, 2048, 2336, 2337, 2050, 2195, 2052, 2341, 2054, 2343, 2200, 2201, 2202, 2348, 2348, 2349, 2205, 2207, 2352, 2353, 2354, 2356, 2357, 2358, 2360, 2215, 2362, 2364, 2220, 2366, 2368, 2223, 2224, 2079, 2079, 2080, 2374, 2228, 2229, 2231, 2231, 2232, 2380, 2234, 2382, 2383, 2237, 2385, 2386, 2240, 2388, 2389, 2242, 2391, 2097, 2393, 2394, 2248, 2249, 2398, 2251, 2252, 2253, 2402, 2255, 2405, 2406, 2408, 1963, 2411, 2412, 2116, 2117, 2415, 2416, 2119, 2419, 2420, 2122, 2422, 2423, 2424, 2425, 2426, 2427, 2429, 2280, 2431, 2132, 2133, 2434, 2285, 2286, 2438, 2288, 2440, 2441, 2292, 2143, 2445, 2295, 2145, 2297, 2450, 2300, 2452, 2453, 2303, 2455, 2456, 2457, 2458, 2307, 2157, 2309, 2462, 2311, 2312, 2465, 2467, 2163, 2469, 2318, 2319, 2321, 2475, 2323, 2171, 2478, 2480, 2021, 2482, 2482, 2330, 2484, 2485, 2486, 2334, 2335, 2490, 2491, 2338, 2493, 2340, 2341, 2496, 2343, 2344, 2499, 2346, 2193, 2503, 2350, 2041, 2507, 2198, 2044, 2510, 2356, 2202, 2358, 2514, 2516, 2361, 2518, 2519, 2520, 2210, 2522, 2523, 2525, 2526, 2527, 2371, 2372, 2373, 2530, 2532, 2533, 2221, 2378, 2380, 2381, 2539, 2540, 2541, 2542, 2544, 2545, 2546, 2548, 2549, 2551, 2553, 2554, 2555, 2240, 2558, 2401, 2402, 2561, 2562, 2404, 2405, 2406, 2407, 2408, 2567, 2410, 2569, 2570, 2253, 2572, 2573, 2096, 2575, 2576, 2577, 2578, 2579, 2420, 2581, 2423, 2584, 2585, 2586, 2588, 2589, 2430, 2591, 2431, 2593, 2594, 2595, 2596, 2597, 2598, 2278, 2600, 2601, 2603, 2604, 2605, 2283, 2607, 2608, 2447, 2610, 2449, 2450, 2613, 2453, 2616, 2617, 2619, 2620, 2621, 2623, 2461, 2625, 2463, 2627, 2465, 2629, 2630, 2468, 2633, 2471, 2635, 2473, 2311, 2638, 2476, 2641, 2642, 2643, 2644, 2481, 2646, 2647, 2320, 2649, 2650, 2487, 2653, 2654, 2491, 2656, 2657, 2658, 2659, 2496, 2497, 2663, 2334, 2665, 2666, 2502, 2669, 2505, 2340, 2672, 2342, 2674, 2675, 2344, 2677, 2678, 2513, 2680, 2681, 2516, 2517, 2685, 2686, 2521, 2688, 2689, 2357, 2691, 2692, 2693, 2527, 2696, 2362, 2698, 2699, 2365, 2701, 2535, 2368, 2536, 2538, 2539, 2708, 2541, 2711, 2712, 2545, 2715, 2716, 2549, 2718, 2719, 2552, 2721, 2723, 2724, 2725, 2726, 2728, 2559, 2561, 2731, 2563, 2733, 2565, 2566, 2567, 2399, 2569, 2740, 2741, 2742, 2573, 2744, 2745, 2747, 2577, 2749, 2750, 2580, 2752, 2753, 2754, 2584, 2757, 2758, 2759, 2760, 2590, 2592, 2592, 2765, 2766, 2595, 2597, 2426, 2770, 2427, 2600, 2773, 2602, 2603, 2776, 2432, 2778, 2779, 2435, 2781, 2609, 2610, 2784, 2613, 2787, 2788, 2616, 2791, 2792, 2793, 2795, 2796, 2797, 2799, 2800, 2801, 2628, 2803, 2804, 2631, 2632, 2807, 2808, 2809, 2635, 2462, 2812, 2639, 2640, 2815, 2642, 2817, 2818, 2819, 2820, 2822, 2823, 2824, 2649, 2826, 2476, 2652, 2829, 2303, 2831, 2656, 2130, 2834, 2483, 2484, 2661, 2662, 2839, 2488, 2841, 2843, 2844, 2845, 2669, 2670, 2848, 2672, 2850, 2851, 2852, 2854, 2855, 2679, 2857, 2681, 2860, 2861, 2506, 2863, 2864, 2508, 2865, 2866, 2689, 2690, 2691, 2513, 2336, 2872, 2873, 2696, 2876, 2877, 2699, 2879, 2880, 2881, 2882, 2524, 2705, 2884, 2706, 2886, 2707, 2530, 2889, 2890, 2891, 2892, 2893, 2714, 2895, 2536, 2717, 2897, 2898, 2899, 2900, 2902, 2722, 2904, 2905, 2906, 2908, 2909, 2910, 2911, 2731, 2732, 2914, 2915, 2916, 2917, 2918, 2919, 2920, 2739, 2922, 2741, 2924, 2925, 2926, 2927, 2928, 2747, 2747, 2931, 2568, 2933, 2935, 2936, 2937, 2938, 2939, 2574, 2941, 2942, 2943, 2944, 2763, 2947, 2765, 2766, 2950, 2952, 2586, 2954, 2955, 2957, 2958, 2959, 2776, 2961, 2962, 2963, 2964, 2781, 2782, 2968, 2969, 2970, 2417, 2973, 2604, 2976, 2977, 2608, 2794, 2609, 2981, 2982, 2983, 2799, 2986, 2987, 2802, 2803, 2990, 2991, 2805, 2620, 2993, 2994, 2808, 2996, 2997, 2998, 2813, 3000, 3002, 3003, 2817, 3005, 3005, 3006, 3007, 3008, 3010, 3011, 3012, 3013, 2827, 3015, 2453, 3017, 3018, 3019, 3020, 3022, 3023, 3024, 3025, 3026, 3027, 2651, 3029, 3030, 2842, 2654, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 2851, 3041, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 2860, 3051, 3052, 2863, 2674, 3056, 2868, 2870, 3063, 3066, 2688, 2880, 2690, 2882, 2884, 2885, 3077, 3078, 3079, 3080, 3081, 2890, 3084, 2892, 3086, 3087, 3088, 3089, 3090, 3091, 3092, 3093, 3094, 2902, 3096, 3097, 3098, 3099, 2907, 3101, 3102, 3103, 2911, 3105, 2912, 3106, 2914, 2915, 2723, 3111, 3112, 2920, 2921, 3116, 3117, 3118, 3119, 2925, 3121, 3121, 2928, 2929, 3125, 3126, 3127, 2933, 2934, 3130, 3131, 3132, 3133, 3134, 3135, 3136, 2942, 3138, 2748, 3140, 3142, 3143, 2556, 3145, 3146, 3147, 3148, 3149, 3150, 2759, 3152, 2956, 3155, 3156, 3157, 2961, 3159, 3159, 3160, 2964, 2965, 3163, 3164, 3165, 3166, 3167, 2971, 3169, 3170, 3171, 3172, 3173, 2976, 3175, 3176, 3177, 2980, 2782, 3179, 3180, 3181, 2786, 2985, 3184, 2986, 2788, 3186, 2989, 3189, 2792, 3191, 3192, 3193, 2995, 2996, 2997, 3197, 3198, 3000, 3000, 3201, 3202, 3003, 3004, 3205, 3206, 3207, 2808, 3209, 3211, 3212, 3213, 3214, 3215, 3015, 3216, 3017, 3219, 3220, 3221, 2820, 3023, 3023, 3225, 2824, 3026, 3027, 2826, 3230, 2828, 3030, 3031, 3233, 3234, 3235, 3236, 3237, 3237, 3238, 3239, 3240, 2838, 3242, 3243, 3244, 3246, 3247, 3248, 3046, 3249, 3250, 3049, 3049, 3253, 3254, 3051, 3255, 3256, 2851, 2649, 3055, 3057, 3057, 3058, 3059, 2856, 3061, 3265, 3062, 3063, 3064, 3268, 3269, 3270, 3271, 3271, 3272, 3273, 3275, 3276, 3277, 3278, 3074, 3280, 3281, 3281, 3282, 3283, 3284, 3080, 3286, 3287, 3288, 2674, 3085, 3085, 3292, 2676, 3293, 3089, 3295, 3090, 3297, 2681, 3299, 3300, 3301, 3096, 3304, 3098, 3306, 3307, 3307, 3102, 3309, 3310, 3105, 3312, 3313, 3107, 3314, 3315, 3316, 3316, 3317, 3318, 3319, 3113, 3321, 3321, 2908, 3116, 3116, 2910, 3326, 3119, 2912, 3328, 3121, 3330, 3331, 3124, 3333, 3126, 3335, 3128, 3337, 3338, 3130, 3340, 3341, 3133, 3342, 3343, 3344, 3345, 3137, 3347, 3347, 3348, 3140, 2723, 3351, 3352, 3144, 3354, 3355, 3356, 3357, 3148, 3359, 3359, 3150, 3361, 3152, 3153, 2943, 3155, 2945, 3156, 3157, 3158, 3159, 3370, 3160, 3161, 3372, 3373, 3374, 3375, 3165, 3166, 3377, 3378, 3379, 3379, 3380, 3381, 3382, 2960, 3383, 3173, 3385, 3174, 3386, 3176, 3176, 3177, 3389, 3179, 2967, 2968, 3181, 3393, 2758, 3182, 3395, 3396, 3184, 3398, 3398, 3399, 3400, 3188, 3189, 3402, 3190, 3404, 3405, 3405, 3406, 3407, 3407, 3408, 3409, 3409, 3410, 2985, 3412, 2986, 3413, 3414, 3201, 3202, 3203, 3417, 3418, 3205, 2992, 2993, 3207, 3421, 3208, 3209, 3210, 3210, 2997, 3426, 3426, 2999, 3214, 3429, 3216, 3431, 3432, 3433, 3219, 3434, 3221, 3221, 3222, 3437, 3438, 3224, 3225, 3226, 3441, 3442, 3443, 3443, 3444, 3445, 3230, 3231, 3447, 3233, 3234, 3450, 3451, 3237, 3022, 3454, 3239, 3456, 3024, 3457, 3458, 3026, 2811, 3244, 3461, 3462, 3463, 3247, 3464, 3249, 3466, 3467, 3468, 3469, 3469, 3470, 3254, 3255, 3256, 3040, 3257, 3258, 3259, 3477, 3260, 3478, 3479, 3263, 3045, 3264, 3482, 3483, 3047, 3485, 3268, 3268, 3269, 3488, 3271, 3271, 3272, 3490, 3491, 3055, 3492, 3493, 3494, 3276, 3495, 3496, 3497, 3497, 3498, 3499, 3500, 3500, 3501, 3502, 3502, 3503, 3504, 3504, 3505, 3506, 3507, 3508, 3509, 3510, 3511, 3512, 3513, 3514, 3515, 3516, 3517, 3517, 3518, 3519, 3520, 3521, 3522, 3522, 3523, 3524, 3525, 3526, 3526, 3527, 3528, 3529, 3529, 3530, 3531, 3532, 3533, 3533, 3534, 3535, 3535, 3536, 3537, 3537, 3538, 3539, 3539, 3540, 3540, 3541, 3542, 3542, 3543, 3544, 3544, 3545, 3546, 3547, 3547, 3548, 3549, 3550, 3550, 3551, 3552, 3552, 3553, 3555, 3555, 3556, 3557, 3558, 3558, 3559, 3560, 3561, 3562, 3562, 3563, 3564, 3565, 3565, 3566, 3567, 3568, 3568, 3569, 3570, 3570, 3571, 3572, 3572, 3573, 3574, 3574, 3575, 3576, 3577, 3578, 3578, 3579, 3580, 3580, 3581, 3582, 3583, 3583, 3584, 3584, 3585, 3586, 3586, 3587, 3588, 3588, 3589, 3590, 3591, 3591, 3592, 3593, 3593, 3594, 3595, 3595, 3596, 3597, 3597, 3598, 3599, 3599, 3600, 3601, 3601, 3602, 3602, 3603, 3604, 3604, 3605, 3606, 3606, 3607, 3608, 3608, 3609, 3610, 3610, 3611, 3612, 3612, 3613, 3614, 3614, 3615, 3616, 3616, 3617, 3618, 3618, 3619, 3620, 3621, 3622, 3623, 3624, 3625, 3626, 3626, 3627, 3628, 3629, 3629, 3630, 3631, 3631, 3632, 3633, 3633, 3634, 3635, 3636, 3636, 3637, 3638, 3639, 3639, 3640, 3641, 3642, 3642, 3643, 3644, 3644, 3645, 3646, 3647, 3647, 3648, 3648, 3649, 3650, 3650, 3651, 3652, 3652, 3653, 3654, 3654, 3655, 3656, 3656, 3657, 3658, 3659, 3659, 3660, 3661, 3661, 3662, 3663, 3663, 3664, 3665, 3665, 3666, 3666, 3667, 3668, 3668, 3669, 3670, 3670, 3671, 3672, 3673, 3674, 3674, 3675, 3676, 3676, 3677, 3677, 3678, 3679, 3679, 3680, 3680, 3681, 3682, 3682, 3683, 3683, 3684, 3685, 3686, 3686, 3687, 3688, 3689, 3690, 3691, 3692, 3692, 3693, 3694, 3694, 3695, 3695, 3696, 3696, 3697, 3698, 3698, 3699, 3699, 3700, 3701, 3701, 3702, 3703, 3703, 3704, 3704, 3705, 3706, 3707, 3707, 3708, 3708, 3709, 3710, 3710, 3711, 3711, 3712, 3713, 3713, 3714, 3715, 3716, 3716, 3717, 3718, 3718, 3719, 3720, 3720, 3721, 3722, 3722, 3723, 3724, 3724, 3725, 3726, 3726, 3727, 3728, 3728, 3729, 3729, 3730, 3731, 3731, 3732, 3733, 3733, 3734, 3735, 3736, 3736, 3737, 3738, 3739, 3739, 3740, 3741, 3741, 3742, 3743, 3743, 3744, 3744, 3745, 3745, 3746, 3746, 3747, 3748, 3748, 3749, 3749, 3750, 3751, 3751, 3752, 3753, 3753, 3754, 3755, 3755, 3756, 3756, 3757, 3758, 3758, 3759, 3759, 3760, 3760, 3761, 3761, 3762, 3762, 3763, 3763, 3764, 3764, 3765, 3765, 3766, 3766, 3767, 3768, 3768, 3769, 3769, 3770, 3771, 3771, 3772, 3772, 3773, 3773, 3774, 3774, 3775, 3776, 3776, 3777, 3777, 3778, 3778, 3779, 3779, 3780, 3780, 3781, 3782, 3782, 3783, 3784, 3784, 3785, 3785, 3786, 3787, 3787, 3788, 3788, 3789, 3790, 3790, 3791, 3791, 3792, 3792, 3793, 3794, 3794, 3795, 3795, 3796, 3797, 3797, 3798, 3799, 3800, 3800, 3801, 3802, 3802, 3803, 3804, 3804, 3805, 3806, 3806, 3807, 3808, 3808, 3809, 3809, 3810, 3811, 3811, 3812, 3812, 3813, 3813, 3814, 3814, 3815, 3816, 3816, 3817, 3818, 3818, 3819, 3819, 3820, 3821, 3821, 3822, 3822, 3823, 3824, 3824, 3825, 3825, 3826, 3826, 3827, 3828, 3828, 3829, 3830, 3830, 3831, 3832, 3832, 3833, 3834, 3835, 3835, 3836, 3837, 3837, 3838, 3838, 3839, 3840, 3840, 3841, 3841, 3842, 3843, 3843, 3844, 3844, 3845, 3846, 3846, 3847, 3847, 3848, 3848, 3849, 3849, 3850, 3850, 3851, 3852, 3852, 3853, 3853, 3854, 3854, 3855, 3855, 3856, 3856, 3857, 3857, 3858, 3858, 3859, 3860, 3860, 3861, 3861, 3862, 3863, 3863, 3864, 3865, 3865, 3866, 3866, 3867, 3868, 3868, 3869, 3869, 3870, 3870, 3871, 3872, 3872, 3873, 3873, 3874, 3874, 3875, 3875, 3876, 3877, 3877, 3878, 3878, 3879, 3880, 3880, 3881, 3881, 3882, 3883, 3883, 3884, 3885, 3885, 3886, 3886, 3887, 3887, 3888, 3888, 3889, 3890, 3890, 3891, 3892, 3892, 3893, 3894, 3894, 3895, 3895, 3896, 3897, 3898, 3898, 3899, 3899, 3900, 3901, 3901, 3902, 3902, 3903, 3903, 3904, 3904, 3905, 3906, 3906, 3907, 3907, 3908, 3908, 3909, 3909, 3910, 3910, 3911, 3911, 3912, 3913, 3913, 3914, 3914, 3915, 3915, 3916, 3916, 3917, 3917, 3918, 3918, 3919, 3919, 3920, 3920, 3921, 3921, 3922, 3922, 3923, 3924, 3924, 3925, 3925, 3926, 3927, 3927, 3928, 3929, 3929, 3930, 3931, 3931, 3932, 3933, 3933, 3934, 3934, 3935, 3935, 3936, 3936, 3937, 3937, 3938, 3938, 3939, 3939, 3940, 3940, 3941, 3941, 3942, 3942, 3943, 3943, 3944, 3944, 3945, 3945, 3946, 3946, 3947, 3947, 3948, 3948, 3949, 3949, 3949, 3950, 3950, 3951, 3951, 3952, 3952, 3953, 3953, 3954, 3955, 3955, 3956, 3957, 3957, 3958, 3960, 3961, 3961, 3961, 3963, 3964, 3964, 3965, 3965, 3966, 3967, 3967, 3968, 3968, 3969, 3969, 3970, 3970, 3971, 3971, 3972, 3973, 3973, 3974, 3974, 3975, 3975, 3976, 3976, 3977, 3977, 3978, 3978, 3979, 3979, 3980, 3980, 3981, 3981, 3982, 3982, 3983, 3983, 3984, 3984, 3985, 3985, 3986, 3986, 3987, 3987, 3988, 3988, 3989, 3989, 3990, 3991, 3991, 3992, 3992, 3993, 3993, 3994, 3994, 3995, 3996, 3996, 3997, 3997, 3998, 3998, 3999, 3999, 4000, 4000, 4001, 4002, 4002, 4003, 4003, 4004, 4004, 4005, 4005, 4006, 4007, 4007, 4008, 4008, 4009, 4009, 4010, 4010, 4011, 4012, 4012, 4013, 4014, 4015, 4015, 4016, 4016, 4017, 4017, 4018, 4018, 4019, 4019, 4020, 4020, 4021, 4021, 4022, 4023, 4023, 4024, 4024, 4025, 4025, 4026, 4026, 4027, 4027, 4028, 4028, 4029, 4029, 4030, 4030, 4031, 4031, 4032, 4032, 4033, 4033, 4034, 4034, 4035, 4035, 4036, 4037, 4037, 4038, 4039, 4039, 4040, 4040, 4041, 4042, 4042, 4043, 4044, 4044, 4045, 4046, 4046, 4047, 4048, 4049, 4050, 4051, 4052, 4053, 4055, 4056, 4058, 4059, 4061, 4062, 4064, 4065, 4067, 4069, 4078]