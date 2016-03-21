# Multiple Apartments: Write a SQL query to get a list of tenants who are
# renting more than one apartment.

select AptTenants.TenantID, Tenants.TenantName
from Tenants left join AptTenants on Tenants.TenantID = AptTenants.TenantID
group by AptTenants.TenantID, Tenants.TenantName
having count(AptTenants.AptID) > 1