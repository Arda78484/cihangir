from turtlepoint import *
from mathexclusive import *

def startmission(p1, p2, radius = 60, detail = 1):
    setturtle()

    latit = 111320
    cords = []
    lat1 = p1[0]
    lon1 = p1[1]
    lat2 = p2[0]
    lon2 = p2[1]
    disx = lat1 - lat2
    disy = lon1 - lon2
    disty = haversine(lat1, lon1, lat2, lon1)
    distx = haversine(lat1, lon1, lat1, lon2)
    x1 = 0
    y1 = 0
    x2 = distx * -disx / abs(disx) * 1000
    y2 = disty * -disy / abs(disy) * 1000
    alpha = (atan(y2 / x2) * d - 90) % 360
    minvalue = 360
    bmax = 0

    point(x1, y1)
    point(x2, y2)

    for i in range(360 // detail):
        corx = x1 + cos(alpha * r) * radius
        cory = y1 + sin(alpha * r) * radius

        ncorx = x1 + cos(((alpha + detail) * r) % 360) * radius
        ncory = y1 + sin(((alpha + detail) * r) % 360) * radius

        dcorx = ncorx - corx
        dcory = ncory - cory

        if (dcorx != 0):
            nalpha = atan(dcory / dcorx) * d

            if (dcorx / abs(dcorx) == -1):
                nalpha += 180
            else:
                if (dcory != 0):
                    if (dcory / abs(dcory) == -1):
                        nalpha += 360
                else:
                    if (dcorx / abs(dcorx) == -1):
                        nalpha = 180
                    else:
                        nalpha = 0
        else:
            if (dcory / abs(dcory) == -1):
                nalpha = 90
            else:
                nalpha = 270

        ocorx = x2 - cos((alpha * r) % 360) * radius
        ocory = y2 - sin((alpha * r) % 360) * radius

        docorx = corx - ocorx 
        docory = cory - ocory
        
        oalpha = atan(docory / docorx) * d

        if (docorx / abs(docorx) == -1):
            if (docory / abs(docory) == 1):
                oalpha += 360
        else:
            oalpha += 180

        if (minvalue > min((oalpha - nalpha) % 360, abs(oalpha - nalpha))):
            bmax = i
            minvalue = min((oalpha - nalpha) % 360, abs(oalpha - nalpha))

        alpha = (alpha + detail) % 360

    for i in range(bmax):
        corx = x1 + cos(alpha * r) * radius
        cory = y1 + sin(alpha * r) * radius
        point(corx, cory)

        cords.append((p1[0] + corx / (latit * cos(cory / latit * r)), p1[1] + cory / latit))
        alpha = (alpha + detail) % 360

    alpha = 0

    for i in range(360 // detail - 2 * bmax):
        corx = x2 - cos((360 - alpha) * r) * radius
        cory = y2 - sin((360 - alpha) * r) * radius
        point(corx, cory)

        cords.append((p2[0] + corx / (latit * cos(cory / latit * r)), p2[1] + cory / latit))
        alpha = (alpha + detail) % 360

    alpha = (atan(y2 / x2) * d - 90) % 360

    for i in range(360 // detail - 3 * bmax):
        corx = x1 + cos((alpha + bmax * detail + 90) * r) * radius
        cory = y1 + sin((alpha + bmax * detail + 90) * r) * radius
        point(corx, cory)

        cords.append((p1[0] + corx / (latit * cos(cory / latit * r)), p1[1] + cory / latit))
        alpha = (alpha + detail) % 360

    for i in cords:
        print(i)
    turtle.exitonclick()