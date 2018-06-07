x = c.submit(inc, 1)
y = c.submit(dec, 2)
total = c.submit(add, x, y)

print(total)     # This is still a future
c.gather(total)   # This blocks until the computation has finished
