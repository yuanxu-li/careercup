# 14.3 Close All Requests: Building #11 is undergoing a major renovation.
# Implement a query to close all requests from apartments in this building.

update Requests
set Status = "Closed"
where Requests.AptID in
(select AptID from Apartments where BuildingID = 11)