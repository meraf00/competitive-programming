class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:        
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
                
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])                
        
        return dp[n1][n2]
    

"""
[1662,1143,1301,1329,443,848,1984,182,1778,837,23,556,1552,1141,116,1939,783,1246,355,1595,248,1387,898,1325,1358,592,1973,951,1836,972,1249,436,1025,371,1052,1661,866,1854,895,763,1855,1507,919,1215,1298,546,1019,328,1183,1467,1146,1328,1002,1214,382,1350,1877,371,931,1287,615,1390,959,1348,1501,1844,1606,1720,1864,1537,545,589,448,1953,1072,301,1204,1223,1726,1536,310,954,313,663,809,691,802,9,615,1213,122,152,6,590,595,1695,1225,1322,1280,1271,1683,1599,349,734,109,1078,1573,1758,938,645,66,1176,1809,822,1154,196,1242,66,10,1567,694,1581,1318,125,456,845,1063,1922,1777,1719,882,1955,1031,622,1330,1456,1784,598,46,1146,946,1925,302,1661,1717,314,279,944,107,1158,211,674,1152,166,818,1523,1113,1813,1672,1564,1650,761,832,5,1809,1352,530,1274,1514,1939,1822,126,1633,1569,1023,745,1145,1778,51,190,1445,1028,276,295,1726,1347,473,989,702,1411,1923,386,1860,1667,1160,1984,478,30,1572,1497]
[1492,333,643,1901,1641,774,315,1703,753,517,1365,1764,1485,1990,584,609,1840,264,1600,158,529,329,858,603,1904,1020,818,674,516,884,1866,1732,732,1982,630,647,382,652,631,391,1696,1166,715,925,672,836,1675,416,1939,1119,98,1876,498,1404,12,1855,1872,757,1585,650,431,482,332,1287,792,8,318,179,1484,897,181,697,1389,1595,748,1771,1703,38,788,404,1811,1385,617,454,1116,759,771,1382,1906,1761,1945,1523,1325,1077,126,1965,1267,621,1596,779,282,823,201,81,1653,657,1993,1711,866,1172,410,1448,682,1546,1311,1388,997,515,1316,937,18,972,762,237,248,1801,217,1079,1526,923,590,654,49,94,990,1489,835,1646,1688,1022,80,490,1708,4,422,773,129,1376,1032,924,1344,743,1891,311,1049,114,1651,48,1158,1161,398,625,358,891,96,1288,1519,180,1352,629,1134,597,1813,1111,1293,1088,806,1286,389,971,857,279,592,1617,891,686,474,104,265,1890,20,1856,1858,181,626,917,463,859,1324,1413]
"""