# 1a, Not Less
if 12 < 12:
    print("Less")
else:
    print("Not Less")

# 1b, Greater than
Var1, Var2 = 25.12, 15.00
if Var1 <= Var2:
    print("Less or equal")
else:
    print("Greater than")

# 2a, X = 12.5
Y, X = 15.0, 25.0
if Y == X - 10.0:
    X /= 2.0

else:
    X -= 10
print(X)

# 2b, X = 15.0
Y = 10.0
X = 25.0
if Y == X - 10.0:
    X /= 2.0

else:
    X -= 10
print(X)

# 2c, X = 30.0
Y = 15.0
X = 5 * Y if (Y < 15.0) and (Y >= 0.0) else 2 * Y
print(X)

# 2d, X = 50.0
Y = 10.0
X = 5 * Y if (Y < 15.0) and (Y >= 0.0) else 2 * Y
print(X)

# 2e, X = 144.0
Y = 36.0
if (Y < 15.0) and (Y >= 0.0):
    X = 5 * Y
elif Y > 20:
    X = 4 * Y
else:
    X = 2 * Y

print(X)

# 2f, X = -10
Y = -5
if (Y < 15.0) and (Y >= 0.0):
    X = 5 * Y
elif Y > 20:
    X = 4 * Y
else:
    X = 2 * Y

print(X)

# 2g, X = 0
Y = 67
if (Y < 15.0) and (Y >= 0.0):
    X = 5 * Y
elif Y > 20:
    X = 4 * Y if Y < 30 else 0 * Y
else:
    X = 2 * Y

print(X)
