from turtlepoint import *
from mathexclusive import *

def startmission(p1, p2, a1, a2, radius = 60, angle = 1, distance = 1):
    setturtle()

    latit= 111320
    cords = []
    lat1 = p1[0]
    lat2 = p2[0]
    lat3 = a1[0]
    lat4 = a2[0]
    lon1 = p1[1]
    lon2 = p2[1]
    lon3 = a1[1]
    lon4 = a2[1]
    disx = lat1 - lat2
    disy = lon1 - lon2
    disty = haversine(lat1, lon1, lat2, lon1)
    distx = haversine(lat1, lon1, lat1, lon2)
    y3 = haversine(lat1, lon1, lat3, lon1) * -disy / abs(disy) * 1000
    x3 = haversine(lat1, lon1, lat1, lon3) * -disx / abs(disx) * 1000
    y4 = haversine(lat1, lon1, lat4, lon1) * -disy / abs(disy) * 1000
    x4 = haversine(lat1, lon1, lat1, lon4) * -disx / abs(disx) * 1000
    x1 = 0
    y1 = 0
    x2 = distx * -disx / abs(disx) * 1000
    y2 = disty * -disy / abs(disy) * 1000
    alpha = (atan(y2 / x2) * d - 90) % 360
    lastalpha = alpha
    last = 0

    point(x1, y1)
    point(x2, y2)
    point(x3, y3)
    point(x4, y4)

    while True:
        if last == 0:
            corx = x1 + cos(alpha * r) * radius
            cory = y1 + sin(alpha * r) * radius
            alpha = (alpha + 90) % 360
            lastalpha = alpha
            last = 1
            
        ocorx = x2 + cos(lastalpha * r) * radius
        ocory = y2 + sin(lastalpha * r) * radius
        odistx = ocorx - corx
        odisty = ocory - cory
        oalpha = atan(odisty / odistx) * d

        alpha1 = (oalpha - alpha) % 360
        alpha2 = 360 - alpha1

        if (abs(alpha - oalpha) < angle + 1):
            cords.append((ocorx, ocory))
            point(ocorx, ocory)
            break

        if (alpha1 < alpha2):
            alpha = (alpha + angle) % 360
        else:
            alpha = (alpha - angle) % 360

        corx = corx + cos(alpha * r) * distance
        cory = cory + sin(alpha * r) * distance
        
        cords.append((corx, cory))
        point(corx, cory)

    last = 0
    while True:
        if last == 0:
            corx = x2 + cos(lastalpha * r) * radius
            cory = y2 + sin(lastalpha * r) * radius
            last = 1
            
        odistx = x3 - corx
        odisty = y3 - cory
        oalpha = atan(odisty / odistx) * d

        if (odistx / abs(odistx) == -1):
            if (odisty / abs(odisty) == -1):
                oalpha += 180

        if (abs(alpha - oalpha) < angle + 1):
            cords.append((x3, y3))
            point(x3, y3)
            break

        alpha1 = (oalpha - alpha) % 360
        alpha2 = 360 - alpha1

        if (alpha1 < alpha2):
            alpha = (alpha + angle) % 360
        else:
            alpha = (alpha - angle) % 360

        corx = corx + cos(alpha * r) * distance
        cory = cory + sin(alpha * r) * distance
        
        cords.append((corx, cory))
        point(corx, cory)

    last = 0
    while True:
        if last == 0:
            corx = x3
            cory = y3
            last = 1
            
        odistx = x4 - corx
        odisty = y4 - cory
        oalpha = atan(odisty / odistx) * d

        if (odistx / abs(odistx) == -1):
            if (odisty / abs(odisty) == -1):
                oalpha += 180

        if (abs(alpha - oalpha) < angle + 1):
            cords.append((x4, y4))
            point(x4, y4)
            break

        alpha1 = (oalpha - alpha) % 360
        alpha2 = 360 - alpha1

        if (alpha1 < alpha2):
            alpha = (alpha + angle) % 360
        else:
            alpha = (alpha - angle) % 360

        corx = corx + cos(alpha * r) * distance
        cory = cory + sin(alpha * r) * distance
        
        cords.append((corx, cory))
        point(corx, cory)

    last = 0
    while True:
    
        if last == 0:
            corx = x4
            cory = y4
            last = 1
            
        ocorx = x1 - cos(lastalpha * r) * radius
        ocory = y1 - sin(lastalpha * r) * radius
        odistx = ocorx - corx
        odisty = ocory - cory
        oalpha = atan(odisty / odistx) * d

        if (odistx / abs(odistx) == -1):
            if (odisty / abs(odisty) == -1):
                oalpha += 180

        if (abs(alpha - oalpha) < angle + 1):
            cords.append((ocorx, ocory))
            point(ocorx, ocory)
            break

        alpha1 = (oalpha - alpha) % 360
        alpha2 = 360 - alpha1

        if (alpha1 < alpha2):
            alpha = (alpha + angle) % 360
        else:
            alpha = (alpha - angle) % 360

        corx = corx + cos(alpha * r) * distance
        cory = cory + sin(alpha * r) * distance
        
        cords.append((corx, cory))
        point(corx, cory)

    last = 0
    while True:
        if last == 0:
            corx = x1 - cos(lastalpha * r) * radius
            cory = y1 - sin(lastalpha * r) * radius
            last = 1
            lastalpha = (lastalpha - 90) % 360
            
        ocorx = x1 + cos(lastalpha * r) * radius
        ocory = y1 + sin(lastalpha * r) * radius
        odistx = ocorx - corx
        odisty = ocory - cory
        oalpha = atan(odisty / odistx) * d

        if (odistx / abs(odistx) == -1):
            oalpha += 180

        if (abs(alpha - oalpha) < angle + 1):
            cords.append((ocorx, ocory))
            point(ocorx, ocory)
            break

        alpha1 = (oalpha - alpha) % 360
        alpha2 = 360 - alpha1

        if (alpha1 < alpha2):
            alpha = (alpha + angle) % 360
        else:
            alpha = (alpha - angle) % 360

        corx = corx + cos(alpha * r) * distance
        cory = cory + sin(alpha * r) * distance

        cords.append((corx, cory))
        point(corx, cory)