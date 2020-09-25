#  Lifo- last in first out like browser..

browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print (browsing_session)

last = browsing_session.pop()
print(last)
print("redirect",browsing_session[-1])

# to check if it is empty
# falsing value=> 0, '',[]
if not browsing_session:
    print(browsing_session[-1])

