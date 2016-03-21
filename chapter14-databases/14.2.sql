# Open Requests: Write a SQL to get a list of all buildings and the number
# of open requests (Requests in which status equals 'Open').

select Buildings.BuildingID, count(Requests.RequestID)
from Buildings left join Apartments on Buildings.BuildingID = Apartments.BuildingID left join Requests on Apartments.AptID = Requests.AptID
group by Requests.Status
having Requests.Status = "Open"