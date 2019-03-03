import math

def scalarMult(a, b):
    return a[0] * b[0] + a[1] + b[1]

def diffVector(a, b):
    return (b[0] - a[0], b[1] - a[1])

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

def rotate_around_point_highperf(xy, degrees, origin=(0, 0)):
    """Rotate a point around a given point.
    
    I call this the "high performance" version since we're caching some
    values that are needed >1 time. It's less readable than the previous
    function but it's faster.

    https://gist.github.com/LyleScott/e36e08bfb23b1f87af68c9051f985302
    """
    radians = math.radians(degrees)
    [x, y] = xy
    offset_x, offset_y = origin
    adjusted_x = (x - offset_x)
    adjusted_y = (y - offset_y)
    cos_rad = math.cos(radians)
    sin_rad = math.sin(radians)
    qx = offset_x + cos_rad * adjusted_x + sin_rad * adjusted_y
    qy = offset_y + -sin_rad * adjusted_x + cos_rad * adjusted_y

    return (qx, qy)

def normalize(v):
    mag = math.sqrt(scalarMult(v, v))
    return (v[0] / mag, v[1] / mag)

def pointInRectangle(cp, cr, ra, rb, rc, rd):
    # https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection
    # 0 ≤ AP·AB ≤ AB·AB and 0 ≤ AP·AD ≤ AD·AD
    ap = diffVector(ra, cp)
    ab = diffVector(ra, rb)
    ad = diffVector(ra, rd)
    apab = scalarMult(ap, ab)
    abab = scalarMult(ab, ab)
    apad = scalarMult(ap,ad)
    adad = scalarMult(ad,ad)
    return 0 <= apab <= abab and 0 <= apad <= adad

def intersectCircle(cp, cr, p1, p2):
    # https://math.stackexchange.com/questions/275529/check-if-line-intersects-with-circles-perimeter
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    cx = cp[0]
    cy = cp[1]

    x1 -= cx
    x2 -= cx
    y1 -= cy
    y2 -= cy
    dx = x2 - x1
    dy = y2 - y1
    dr_squared = dx**2 + dy**2
    D = x1*y2 - x2*y1
    return cr**2 * dr_squared > D**2


def rectangleCircle(cp, cr, r):
    # https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection
    [ra, rb, rc, rd] = r
    return pointInRectangle(cp, cr, ra, rb, rc, rd) or intersectCircle(cp, cr, ra, rb) or intersectCircle(cp, cr, rb, rc) or intersectCircle(cp, cr, rc, rd) or intersectCircle(cp, cr, rd, ra)

def twoRectangle(r1, r2):
    # Checks if the two polygons are intersecting.
    # https://stackoverflow.com/questions/10962379/how-to-check-intersection-between-2-rotated-rectangles
    for polygon in (r1, r2):
        for i1 in range(0, 4):
            i2 = (i1 + 1) % 4
            p1 = polygon[i1]
            p2 = polygon[i2]

            normal = (p2[1] - p1[1], p1[0] - p2[0])

            minA = None
            maxA = None

            for p in r1:
                projected = scalarMult(normal, p)
                if(minA == None or projected < minA):
                    minA = projected
                if(maxA == None or projected > maxA):
                    maxA = projected
            
            minB = None
            maxB = None
            for p in r2:
                projected = scalarMult(normal, p)
                if(minB == None or projected < minB):
                    minB = projected
                if(maxB == None or projected > maxB):
                    maxB = projected

            if(maxA < minB or maxB < minA):
                return False

    return True

def twoCircle(c1p, c1r, c2p, c2r):
    # https://stackoverflow.com/questions/8367512/how-do-i-detect-intersections-between-a-circle-and-any-other-circle-in-the-same
    # (R0 - R1)^2 <= (x0 - x1)^2 + (y0 - y1)^2 <= (R0 + R1)^2
    q1 = (c1r - c2r) ** 2
    q2 = (c1p[0] - c2p[0]) ** 2 + (c1p[1] - c2p[1]) ** 2
    q3 = (c1r + c2r) ** 2
    return q1 <= q2 and q2 <= q3