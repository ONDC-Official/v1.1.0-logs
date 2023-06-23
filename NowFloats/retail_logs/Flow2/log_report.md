**/select**
- /context/action must be equal to constant (select)
- context.action should be select

**/on_select**
- Timestamp for /select api cannot be greater than or equal to /on_select api
- provider.id mismatches in /on_search and /on_select

**/init**
- /context/action must be equal to constant (init)
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- /message/order/fulfillments/0/end/location/address/locality must NOT have fewer than 3 characters
- context.action should be init
- Provider Id mismatches in /select and /init
- Provider.locations[0].id mismatches in /select and /init
- billing/created_at should match context.timestamp
- billing/updated_at should match context.timestamp
- address.building should be more than 3 chars
- address.name should be more than 3 chars
- address.locality should be more than 3 chars
- gps coordinates in fulfillments[0].end.location mismatch in /select & /init
- address.area_code in fulfillments[0].end.location mismatch in /select & /init

**/on_init**
- /billing/address must have required property 'building'
- Timestamp for init api cannot be greater than or equal to on_init api
- Provider Id mismatches in /on_search and /on_init
- provider_location.id mismatches in /on_search and /on_init
- gps coordinates in fulfillments[0].end.location mismatch in /select & /on_init
- address.area_code in fulfillments[0].end.location mismatch in /select & /on_init
- Quoted Price in /on_init INR 2010.85 does not match with the quoted price in /on_select INR undefined
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /context/action must be equal to constant (confirm)
- /message/order/billing/address must have required property 'building'
- context.action should be confirm
- Provider Id mismatches in /on_search and /confirm
- provider.locations[0].id mismatches in /on_search and /confirm
- fulfillments[0].end.location.address.area_code is not matching with area_code in /select
- order.created_at timestamp should match context.timestamp
- Discrepancies between the quote object in /on_select and /confirm
- Quoted Price in /confirm INR 2010.85 does not match with the quoted price in /on_select INR undefined

**/on_confirm**
- /billing/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'building'
- Timestamp for /confirm api cannot be greater than or equal to /on_confirm api
- Provider Id mismatches in /on_search and /on_confirm
- provider.locations[0].id mismatches in /on_search and /on_confirm
- items[0].fulfillment_id mismatches for Item e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 in /on_select and /on_confirm
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- fulfillments[0].end.location gps is not matching with gps in /select
- fulfillments[0].end.location.address.area_code is not matching with area_code in /select
- Discrepancies between the quote object /on_select and /on_confirm
- Quoted Price in /on_confirm 2010.85 does not match with the quoted price in /on_select undefined

**/status**
-  must have required property 'context'
-  must have required property 'message'

